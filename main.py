# ================================================
# DAY 3 CUMULATIVE PROJECT: STUDENT REGISTRY (REFINED)
# ================================================

# STEP 1: Tuple and unpacking
school_info = ("Merryland", "Uganda", "1995")
school, country, founded = school_info
print("School Name:", school)
print("Country:", country)
print("Founded:", founded)
print()

# STEP 2: Create registry dictionary
registry = {
    "Innocent": {"age": 20, "grade": 98, "courses": ["python", "java", "art"]},
    "Precious": {"age": 34, "grade": 34, "courses": ["python", "biology", "math"]},
    "Mercy": {"age": 55, "grade": 21, "courses": ["biology", "physics", "chemistry"]},
    "Kawala": {"age": 13, "grade": 67, "courses": ["python", "biology", "physics"]}
}

# STEP 3: Print each student neatly
print("=== Student Registry ===")
for name, info in registry.items():
    courses_str = ", ".join(info["courses"])
    print(f"Name: {name} | Age: {info['age']} | Grade: {info['grade']} | Courses: {courses_str}")
print()

# STEP 4: Create set of top students (grade > 75)
top_students = {name for name, info in registry.items() if info['grade'] > 75}
print("Top students (grade > 75):", top_students)
print()

# STEP 5: Add a new student with grade < 75, update an existing student's grade > 90
registry["Noah"] = {"age": 25, "grade": 44, "courses": ["python", "ict", "art"]}
print("Added new student: Noah (grade 44)")

# Update Mercy's grade to above 90
registry["Mercy"]["grade"] = 95
print(f"Updated Mercy's grade to {registry['Mercy']['grade']}")
print()

# STEP 6: Collect all courses into a set of unique courses
all_courses = []
for info in registry.values():
    all_courses.extend(info["courses"])
unique_courses = set(all_courses)
print(f"All courses (with duplicates): {all_courses}")
print(f"Unique courses: {unique_courses}")
print(f"Number of unique courses: {len(unique_courses)}")
print()

# STEP 7: Remove one student (Mercy) using pop()
removed = registry.pop("Mercy", None)  # None if key missing
print(f"Removed: Mercy")
print(f"Remaining students: {len(registry)}")
print()

# STEP 8: Final school summary
print("====================================")
print(f"School: {school} | {country} | {founded}")
print(f"Total Students: {len(registry)}")
print(f"Top Students: {top_students}")
print(f"Unique Courses Offered: {len(unique_courses)}")
print("====================================")
