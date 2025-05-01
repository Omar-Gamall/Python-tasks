students = [
    {"name": "Omar", "grades": [70, 80, 90]},
    {"name": "Ahmed", "grades": [60, 70, 80]},
    {"name": "Ali", "grades": [80, 90, 100]},
]

for student in students:
    name = student["name"]
    grades = student["grades"]
    average = sum(grades) / len(grades)
    print(f"{name}: {average}")