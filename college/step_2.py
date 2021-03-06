from college import Student, Group, Teacher

# students = Student.import_from_file('students.src')
# [print(el) for el in students]
students_23 = Student.import_from_file('23_group.src')
group_23 = Group('23', 'Информационные системы 09.02.07')
group_23.add_students(students_23)
[print(el, el.group) for el in students_23]
print('*' * 30)
students_33 = Student.import_from_file('33_group.src')
group_33 = Group('33', 'Прикладная информатика 09.02.05')
group_33.add_students(students_33)
[print(el, el.group) for el in students_33]

print('*' * 30)
teacher = Teacher.import_from_file('teacher.src')
[print(el) for el in teacher]
