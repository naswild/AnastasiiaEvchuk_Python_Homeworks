# task 1
employee_list = ["John Snow", "Piter Pen", "Drakula", "IvanIV", "Moana", "Juilet"]
print(f'{employee_list[1]}, {employee_list[-2]}')

# task 2
def dev_by_three(number):
   if number % 3 == 0:
       return 'Yes'
   else:
       return 'No'

numb = int(input('Введите число: '))
result = dev_by_three(numb)
print(f'Делится ли на три {numb}? - {result}')

# task 3
import math
def min_boxes(items):
   return math.ceil(num_items / 5)
num_items = int(input('Введите количество вещей: '))
result = min_boxes(num_items)
print(f'Минимальное количество коробок равно {result}')

# task 4
n = int(input('Введите число: '))
def check_divisibility(n):
   result = ''
   for num in range (1, n + 1):
       if num % 4 == 0:
           result += f'Число {num} делится и на 2, и на 4\n'
       elif num % 2 == 0:
           result += f'Число {num} делится на 2, но не на 4\n'
       else: result += str(num) + '\n'
   return result

print(check_divisibility(10))

#task 5
def quarter_of_year(mes):
    if 0 < mes <= 3:
        return 'I квартал'
    elif 3 < mes <= 6:
        return 'II квартал'
    elif 6 < mes <= 9:
        return 'III квартал'
    elif 9 < mes <= 12:
        return 'IV квартал'
    else:
        return 'Введите значение от 1 до 12'

num_mes = int(input('Введите номер месяца: '))
print(quarter_of_year(num_mes))

# task 6
lst = [17, 34, 9, 21, 13, 48, 24, 7, 81, 29, 16, 12, 42]

for number in lst:
    if number > 15 and number % 3 == 0:
        print(number)

# task 7
num_list = list(range(25, 0, -5))
print(num_list)

#task 8
var_1 = 50
var_2 = 5

old_var = var_1
var_1 = var_2
var_2 = old_var

print(f'var_1 = {var_1}, var_2 = {var_2}')