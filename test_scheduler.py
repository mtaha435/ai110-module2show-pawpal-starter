from app import Pet, PetTask, DailyScheduler

def test_priority_sorting():
    pet = Pet("Mochi", "Dog")
    sched = DailyScheduler("Jordan", pet, available_hours=1)
    
    # Add a low priority task then a high one
    sched.add_task(PetTask("Walk", 30, "low"))
    sched.add_task(PetTask("Meds", 10, "high"))
    
    plan, _ = sched.generate_schedule()
    # The high priority 'Meds' should be the first item
    assert plan[0]['activity'] == "Meds"

def test_time_limit():
    pet = Pet("Mochi", "Dog")
    sched = DailyScheduler("Jordan", pet, available_hours=0.5) # 30 mins only
    sched.add_task(PetTask("Long Walk", 60, "high"))
    
    plan, total_m = sched.generate_schedule()
    assert len(plan) == 0  # Should skip because 60 > 30