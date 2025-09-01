for x in range(1, 21):
    print(f'x = {str(x)}, x2 = {x*x}')

students = ['Александр', 'Михаил', 'Мария', 'Ольга', 'Кирилл', 'Олеся', 'Виктор']
for student in students:
     print(student)

for i in range(0, len(students)):
    print(students[i])

word = 'test'
for s in word:
    print(s)

# напечатать нечетные числа
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in nums:
    if num % 2 == 1:
        print(num)
