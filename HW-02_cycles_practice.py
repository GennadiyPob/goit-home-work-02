"""
#Задача 15 з модуля 2 автоперевірки
#Калькулятор
result = None
operand = None
operator = None
wait_for_number = True

while True:
    user_input = input('Wait for input : ') #Очкуємо введення числа, але може бути введено будь-що 

    if wait_for_number and result is None: #Перевіряємо чи введено число, а result=None. Результат має переводити в число. 
        try:
            result = float(user_input) #Присвоюємо значення введеного символа result. Пишемо float 
            wait_for_number = False #Вже не потрібно чекати число. Тому змінюємо значення на False-            

        except ValueError:   #Перевірка на введення НЕ числа.  
            print(f'{user_input} is not number. Try again') #Якщо не число, то повідомляємо про це.  
    elif user_input == "=": #Перевірка на введення знаку =
        print(result)
        break

    elif not wait_for_number: #Перевірка на введення знаку + - * /
        if user_input == "+" or user_input == "-" or user_input == "*" or user_input == "/":
            operator = user_input
            wait_for_number = True #Зміна з False на True для очікування нової цифри
        else: #Перевіряємо чи введений оператор. Якщо ні, то висвічуємо повідомлення...
            print(f'{user_input} is not "+", "-", "*", "/". Try again')    

    elif wait_for_number:
        try:
            operand = float(user_input)
            result = eval(f'{result} {operator} {operand}') #Динамічне виконання виразів
            operand = None      #Обнулення значень для наступних розрахунків.
            operator = None     #Обнулення значень для наступних розрахунків.
            wait_for_number = False 
        except ZeroDivisionError:
            operand = None
            continue
        except ValueError:   #Перевірка на введення НЕ числа.  
            print(f'{user_input} is not number. Try again') #Якщо не число, то повідомляємо про це. 

"""
"""
result = eval('10 - 6')
print(result)
"""

'''
#Виведення парних чисел 
for number in range(1, 21):
    if number % 2 == 0:
        print(number)
''' 

''' 
#Порівняння двох строк
string_one = input('Enter string : ')
string_two = input('Enter string to compare : ')

for char in string_one:
    if char not in string_two:
        print(False)
        break
else:
    print(True)

'''  

'''
#Fobinacci

a, b = 0, 1
for _ in range(15): #
    print(a)
    a, b = b, a + b
'''


#Перевірка чи число є просте
"""
while True:
    is_prime = True 
        
    try:
        user_input = int(input('Enter number : '))
        
        if user_input < 0:
            break
                
        for i in range(2, int(user_input**0.5) + 1):
            if user_input % i == 0:
                is_prime = False
                break

        else:
            print(is_prime)

    except ValueError:
        print('Not natural number') 
""" 

#Чи є число поліндром: читається в обох напрямках 121

'''


number = int(input('Enter three-digit number : '))

hunderd = number // 100  # Ділимо на 100 без остачі. 121 // 100  = 1. 
units = number % 10      # Визначаєм залишок від ділення на 10: 121 % 10  = 1. 
if hunderd == units:
    print('Is polindrom')
else:
    print('Not polindrom')
'''
'''
#Дано координати точок. Визначити дістанцію між двома точками.
x1_coord = float(input('Enter the x coordinate of the first point'))
y1_coord = float(input('Enter the y coordinate of the first point'))
x2_coord = float(input('Enter the x coordinate of the second point'))
y2_coord = float(input('Enter the y coordinate of the second point'))

distance = round(((x2_coord - x1_coord)**2 + (y2_coord - y1_coord)**2)**0.5, 2)

if dustance < 5:
    print('Distance less than 5')
else:
    print(f'Distance {distance}')
'''


'''
# Вводимо два числа k,l. Якщо вони не рівні то менше з них замінює більше. Інакше обидва замінюємо на 0.


k = int(input('Enter k : '))
l = int(input('Enter l : '))
if k != l:
    if k < l:
        k = l 
    else:
        l = k
else:
    k, l = 0, 0

print(f'k equal to {k}, l equal to {l}')
'''


'''  
#Перевірити день, місяць і рік на коректність введення.

day = int('Enter day : ')
month = int('Enter month : ')
year = int('Enter year : ')

is_lep_year = False

if month <= 0 or month > 12:
    print('Month should be from 1 to 12')

if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    if day <= 1 or day> 31:
        print('Day should be from 1 to 31')

    if day <= 1 or day> 30:
        print('Day should be from 1 to 30')

if month == 2:
    if year % 400 == 0:
        is_leap_year = True
    if year % 100 == 0:
        is_leap_year = False
    if year % 4 == 0:
        is_leap_year = True
    else:
        is_leap_year = False

    if is_leap_year:
        if day <= 1 or day > 29:
          print('Day should be from 1 to 29')  
    else: 
        if day <= 1 or day > 28:
          print('Day should be from 1 to 28') 

'''       
'''
#Порівняння трикутників
from math import sqrt, pow # імпорт квадратного кореня та степені
  
side1 = float(input('Enter first side of triangle : '))
side2 = float(input('Enter second side of triangle : '))  
side3 = float(input('Enter third side of triangle : '))
triangle_type = None

if (side1 + side2) > side3 and (side1 + side3) > side2 and (side2 + side3) > side1:

    if side1 == side2 and side3 == side2 and side3 == side1:
        triangle_type = 'equilateral'
    elif side1 == side2 or side3 == side1 and side3 == side2:
        triangle_type = 'isosceles'
    elif sqrt(pow(side1, 2) + pow(side2, 2)) == side3 or\
        sqrt(pow(side2, 2) + pow(side3, 2)) == side1 or\
        sqrt(pow(side1, 2) + pow(side3, 2)) == side2:
        triangle_type = 'rigth-angled'
    else:
        triangle_type = 'differential'
    
    print(triangle_type)

else:
    print('Not triangle')
'''




'''
#Розрахунок складних відсотків по депозиту
 
percent = 0.06
deposit = 100
year = 10 
waiting_year = 10

print(round(deposit * (1 + percent / 12 ) ** (12 *10),2))

for year in range(1, waiting_year + 1):
    new_deposit = deposit * ( 1 + percent / 12 ) ** 12
    deposit = new_deposit

print(round(new_deposit,2))
'''
'''
#Користувач вводить строку. Перевірити чи є строка паліндром.

line = input('Enter string')
print(line)
print(line[::-1]) 

if line == line[::-1]:
    print('Is palindrome')
else:
    print('Not palindrom')
'''


    

