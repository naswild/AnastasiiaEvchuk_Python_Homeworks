from student import Student
from course_group import CourseGroup

student = Student('Alex', 'Malov', 22, 'Python')
classmate1 = Student('Alice', 'Kopot', 23, 'Python')
classmate2 = Student('Mary', 'Smit', 21, 'Python')
classmate3 = Student('Artem', 'Logov', 25, 'Python')

course_group = CourseGroup(student, [classmate1, classmate2, classmate3])
print(course_group)
