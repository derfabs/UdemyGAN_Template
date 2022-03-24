students = {"Ben": 1, "Jan": 2, "Peter": 1, "Melissa": 4}
print(students)

# Werte lesen
student1 = students["Ben"]
print(student1)

# Werte ersetzen
students["Ben"] = 6
print(students)

# Neuer Eintrag
students["Julia"] = 1

# Element entfernen
students.pop("Julia")
print(students)

# Keys
for student in students:
    print(student)

# Values
for student_grade in students.values():
    print(student_grade)

# Keys&Values
for key, value in students.items():
    print(student_grade)
