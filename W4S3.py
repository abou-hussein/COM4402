# # activity 1
# nums = [3, 6, 9, 12]
#
# first_number = nums [0]
# last_number = nums [-1]
#
# print (first_number)
# print (last_number)

# #activity 2
# colors = ["black", "white", "red", "blue"]
#
# new_color = "pink"
# colors.append(new_color)
#
# print (colors)

#activity 3
#
# person = {
#     "name": "Sam",
#     "city": "London"
# }
# person ["age"] = 20
# person ["city"] =  "Bolton"
#
# age = int(input ("Enter your age: "))
# person ["age"] = age
# print (person)
# for key, value in person. items():
#     print (key, ":", value)

#activity 4

courses = {
    "python": {
        "students": ["Ali", "Sara", "Tom", "Ali"],
        "max_size": 3
    },
    "datasci": {
        "students": ["Sara", "Imran"],
        "max_size": 2
    }
}
# 1. For each course, print the set of unique student names (so each name appears once).
# 2. For each course, check if the number of unique students is greater than `max_size`
# and print `"FULL"` or `"OK"`.
# 3. Build a dictionary `student_counts` mapping each student name to
# how many different courses they are enrolled in (use a dict plus sets or lists).
student_counts = {}

for course_name, course_info in courses.items():
    # 1. Unique students
    unique_students = set(course_info["students"])
    print(f"{course_name} unique students:", unique_students)

    # 2. Check if course is FULL or OK
    if len(unique_students) > course_info["max_size"]:
        print("Status: FULL")
    else:
        print("Status: OK")

    # 3. Count how many courses each student is in
    for student in unique_students:
        student_counts[student] = student_counts.get(student, 0) + 1

    print()  # blank line for readability

print("Student counts:", student_counts)