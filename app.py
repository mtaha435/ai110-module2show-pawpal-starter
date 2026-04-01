import streamlit as st
from datetime import datetime, timedelta

# --- BACKEND LOGIC (The "System Design" part) ---

class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species

class PetTask:
    """Represents a specific care activity."""
    PRIORITY_MAP = {"high": 3, "medium": 2, "low": 1}

    def __init__(self, title, duration, priority):
        self.title = title
        self.duration = duration  # in minutes
        self.priority = priority.lower()
        self.priority_val = self.PRIORITY_MAP.get(self.priority, 1)

class DailyScheduler:
    """Handles the logic of ordering and validating tasks."""
    def __init__(self, owner_name, pet, available_hours=4):
        self.owner_name = owner_name
        self.pet = pet
        self.max_minutes = available_hours * 60
        self.tasks = []

    def add_task(self, task: PetTask):
        self.tasks.append(task)

    def generate_schedule(self, start_time_str="08:00"):
        # 1. Sort by priority (High to Low)
        sorted_tasks = sorted(self.tasks, key=lambda x: x.priority_val, reverse=True)
        
        current_time = datetime.strptime(start_time_str, "%H:%M")
        schedule_log = []
        total_time_used = 0

        for task in sorted_tasks:
            # Check if task fits in the owner's available time
            if total_time_used + task.duration <= self.max_minutes:
                end_time = current_time + timedelta(minutes=task.duration)
                
                schedule_log.append({
                    "time_slot": f"{current_time.strftime('%I:%M %p')} - {end_time.strftime('%I:%M %p')}",
                    "activity": task.title,
                    "priority": task.priority,
                    "reason": self._generate_reason(task)
                })
                
                current_time = end_time
                total_time_used += task.duration
            else:
                # Task skipped due to time constraints
                continue
                
        return schedule_log, total_time_used

    def _generate_reason(self, task):
        if task.priority == "high":
            return f"Essential {self.pet.species} care; prioritized for health/safety."
        return f"Fits within {self.owner_name}'s schedule after essential tasks."

# --- STREAMLIT UI ---

st.set_page_config(page_title="PawPal+", page_icon="🐾")

st.title("🐾 PawPal+ Assistant")

# Sidebar: Owner & Pet Info
with st.sidebar:
    st.header("Profile")
    u_name = st.text_input("Owner Name", "Jordan")
    p_name = st.text_input("Pet Name", "Mochi")
    p_species = st.selectbox("Species", ["Dog", "Cat", "Bird", "Other"])
    max_h = st.slider("Available Hours Today", 1, 12, 4)
    start_t = st.time_input("Start Time", datetime.strptime("08:00", "%H:%M"))

# Session State for Task List
if "task_list" not in st.session_state:
    st.session_state.task_list = []

# Input Section
st.subheader("Manage Care Tasks")
c1, c2, c3 = st.columns([2, 1, 1])
with c1: t_name = st.text_input("Task", placeholder="e.g. Brushing")
with c2: t_dur = st.number_input("Mins", 5, 180, 30, step=5)
with c3: t_prio = st.selectbox("Priority", ["High", "Medium", "Low"])

if st.button("Add Task"):
    st.session_state.task_list.append(PetTask(t_name, t_dur, t_prio))
    st.success(f"Added {t_name}")

# Display Table
if st.session_state.task_list:
    st.table([{"Task": t.title, "Duration": t.duration, "Priority": t.priority} for t in st.session_state.task_list])
    if st.button("Clear Tasks"):
        st.session_state.task_list = []
        st.rerun()

st.divider()

# Generation
if st.button("Generate Daily Plan", type="primary"):
    if not st.session_state.task_list:
        st.error("Add at least one task first!")
    else:
        my_pet = Pet(p_name, p_species)
        engine = DailyScheduler(u_name, my_pet, max_h)
        
        for t in st.session_state.task_list:
            engine.add_task(t)
            
        plan, total_m = engine.generate_schedule(start_t.strftime("%H:%M"))
        
        st.subheader(f"📅 {p_name}'s Schedule")
        for entry in plan:
            with st.expander(f"{entry['time_slot']} | {entry['activity']}"):
                st.write(f"**Priority:** {entry['priority'].capitalize()}")
                st.caption(f"**Reasoning:** {entry['reason']}")
        
        st.metric("Total Time Utilized", f"{total_m} mins", f"Remaining: {max_h*60 - total_m} mins")