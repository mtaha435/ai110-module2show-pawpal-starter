# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?
Scheduler, pet task, pet, basic attributes like name species priority
**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.
no
---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?
total time availability!!, task duration. i treated it like a os process scheduler.
**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?
greedy priority sort algo-> puts HP tasks first even if LP tasks are super quick
---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?
design brainstorming, putting in some code, a desc, goes a long waay
**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?
didn't take all the brainstorming ideas for the uml, some seemed unnecessary
---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?
priority testing, test if the scheduler ignored prorities in edge cases
**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?
pretty confident, not sure what other cases to add.

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?
all of it

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
reread everything ai spits