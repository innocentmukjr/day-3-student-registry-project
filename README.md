# day-3-student-registry-project
# Day 3 Cumulative Project – Student Registry

## 📘 The Exercise Instructions

This project combines: lists, dictionaries, tuples, sets, loops, f‑strings.

**Step 1:** Create a tuple `school_info` (school name, country, year founded). Print each value using unpacking.

**Step 2:** Create a dictionary `registry` with 4 students. Each student key is their name. Value is a nested dict with `"age"`, `"grade"` (number), `"courses"` (list of 3 course names). Use real Ugandan names.

**Step 3:** Loop through registry and print each student neatly:  
`Name: Innocent | Age: 25 | Grade: 90 | Courses: Python, Math, AI`

**Step 4:** Create a set `top_students` by looping and adding students whose grade > 75. Print the set.

**Step 5:** Add a new student with grade below 75. Update an existing student's grade to above 90. Print only the updated student's details.

**Step 6:** Create a list `all_courses` from every student's courses (duplicates allowed). Convert to set `unique_courses`. Print how many unique courses.

**Step 7:** Remove one student using `pop()`. Print `"Removed: name"` and remaining student count.

**Step 8:** Print a final school summary:

---

## 🧠 My Approach

- **Step 1:** Created tuple, unpacked into three variables, printed with labels.
- **Step 2:** Nested dictionary – outer keys are student names, inner dicts contain age, grade, courses list.
- **Step 3:** Used `for key, value in registry.items():` and f‑string formatting.
- **Step 4:** Started with empty set, looped, added name if grade > 75.
- **Step 5:** Added new student via `registry["Noah"] = {...}`; updated `registry["Mercy"]["grade"] = 95`; printed whole registry (I printed full dict – instruction said "print only the updated student's details" – noted in reflection).
- **Step 6:** Created empty list, extended with each student's courses list, then converted to set and used `len()`.
- **Step 7:** Used `.pop("Mercy")` to remove and capture removed value; printed removal message and remaining count.
- **Step 8:** Used f‑strings with variables from previous steps to print formatted summary.

---

## 🚧 Challenges I Faced

- Remembering to use `.extend()` for lists (not `.append()`) when adding multiple courses at once.
- Converting a list of courses to a set – that automatically removes duplicates.
- Unpacking tuple – straightforward once I kept the variable count equal.
- The instruction for Step 5 said "Print only the updated student's details" – I printed the whole registry. A small improvement for next time.
- Making sure the final summary used the updated `top_students` set (which didn't change after removing Mercy, because Mercy's grade after update was 95 but she was removed before summary – that's fine).

---

## ✅ What I Learned

- How to combine multiple data structures in one project.
- `extend()` vs `append()` – `extend` adds each element of an iterable individually.
- Sets are perfect for deduplicating course names.
- `pop()` removes a key‑value pair and returns the value – useful for logging.
- Unpacking tuples makes code cleaner.
- A cumulative project proves I can apply everything from Day 3.

---

## 🖥️ How to Run My Code

1. Save the code as `main.py`.
2. Run `python main.py`.
3. Expected output (abbreviated):
4. 
---

## 📅 Part of My AI/ML Learning Journey

Day 3 cumulative project – my first multi‑topic project. This mimics real data pipelines: student registry as a dataset, filtering top students (grade > 75) as a query, collecting unique courses as a feature set. In ML, similar operations appear in data cleaning (deduplication), aggregation (counting unique categories), and subset selection (filtering rows). I proved I can structure data and manipulate it with core Python.

---
*First cumulative project done. On to Day 4 and beyond.*
