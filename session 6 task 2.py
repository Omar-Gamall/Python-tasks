import pandas as pd

# Data dictionary with lowercase keys and string values
student_info_source = {
    'name': ['alice', 'bob', 'charlie', 'david', 'eva'],
    'age': [20, 22, 19, 21, 20],
    'grade': ['a', 'b', 'a', 'c', 'b'],
    'marks': [85, 78, 92, 65, 74]
}
# DataFrame using the modified data
class_roster = pd.DataFrame(student_info_source)

print("original class roster:")
print(class_roster)


print("\nfirst 3 students in the roster:")
print(class_roster.head(3))

print("\nstudent names and their marks:")
# Accessing columns using lowercase names
print(class_roster[['name', 'marks']])

print("\nstudents who achieved an 'a' grade:")
# Filtering using lowercase column name and value
top_students = class_roster[class_roster['grade'] == 'a']
print(top_students)