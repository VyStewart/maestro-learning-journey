# Week 01 

## Experiments, Mistakes & Debugging Thoughts

This file holds all my raw discoveries, mistakes, fixes, and experiments from Week 1.  
Not polished — just real learning moments.

---

## 🔧 Git & VS Code Lessons (Accidental Discoveries)

### `.gitignore` discovery  
I found out that I must place the `.gitignore` file **in the repo root**, not inside a folder.  
This controls exactly which files Git will push to GitHub.

It helped me keep my repo clean by ignoring:
- venv folder  
- trash files  
- Jupyter or temp files  

This made my GitHub look clean and professional.

---

### Accidentally entering Python Shell in VS Code
I typed something that caused VS Code to open the **Python shell (`>>>`)** instead of running my script.

Symptoms:
- The RUN button didn’t work  
- My file wouldn’t execute  
- Terminal only showed `>>>`  

Fix:
```python
exit()   # or quit()


## Print Tests
- Tried printing with commas vs plus.
- Learned `print("Hi" + 5)` → TypeError.
- Learned `"Hi", 5` works without error.

## Variables
- Tested renaming variables to understand overwriting.
- Accidentally forgot quotes → NameError.
- Practiced using descriptive names.

## Math & Division
- Tested `/` vs `//` vs `%`.
- `%` surprised me at first until I saw the cycle pattern:
  - 0 → 0  
  - 1 → 1  
  - 2 → 2  
  - 3 → 0  
  - 4 → 1  
- Practiced modeling real-world costs.

## Rounding & Money Formatting
- Practiced:
  - `round()`
  - f"${total:.2f}"
- Learned when to format decimals and when not to (example: 6.5 is already clean).

## Type Casting
- Intentional mistakes to understand errors:
  - `"10" + 5` → TypeError  
  - `int("4.5")` → ValueError  
- Mixed types:
  int("25") + float("4.5") + 3

My Thoughts: 
Noted: input() always returns a string!
. Practiced converting input before calculations.
. Built:
 . cookie counter
 . gas mileage calculator
 . study minutes → hours converter

Traceback Insights
. Tracebacks are actually helpful.
. They point directly to the problem line.
. TypeError is the most common mistake in Week 1.

Personal Debugging Rules I Learned
. Check type() when unsure.
. Convert BEFORE doing math.
. Reread error messages slowly.
. Look at the exact line number.
. Don't panic — errors are normal.

End of Week Thoughts
. Errors don’t scare me anymore.
. Typing code feels natural.
. My GitHub structure looks clean and professional.
. Ready to build two projects for Week 1.
