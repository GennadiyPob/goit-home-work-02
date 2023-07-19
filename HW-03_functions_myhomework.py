'''
#-01 Написати функцію привітання.

def greeting():
    print("Hello World")

greeting()

'''
'''
#-02 Написати функцію привітання.

def invite_to_event(username):
    return (f'Dear {username}, we have the honor to invite you to our event.')

invite_to_event(input('Enter username ')) 
'''
'''
#-03 Розрахунок вартості подорожі в таксі

trip_quantity = 0
def sum_trip(distance):
    global trip_quantity
    trip_quantity += 1
    sum = 40 + 10 * distance
    return sum 

sum_trip(int(input('Enter distance : '))) 
'''
'''
#HW-03 Розрахунок вартості подорожі в таксі

base_rate = 40
price_per_km = 10
total_trip = 0
path = 0
sum = 0

def trip_price(path):
    global total_trip
    total_trip += 1
    sum = base_rate + price_per_km * path
    return sum

sum = trip_price(path)
'''
'''
#HW-04 Розрахунок вартості товару зі знижкою

def discount_price(price):
    
    def apply_discount(discount): 
        nonlocal price
        price = price * (1 - discount)

    apply_discount(discount)
    return price

price = float(input('Enter price :'))
discount = float(input('Discount : '))
print(discount_price(price))
'''
'''
#HW-05 Повертає повне ім'я користувача

def full_name(first_name, middle_name, last_name):
    if middle_name == '':
        return first_name + ' ' + last_name
    else:
        return first_name + ' ' +  middle_name + ' ' + last_name  

first_name = input('Enter first name : ')
middle_name = input('Enter middle name : ')
last_name = input('Enter last name : ')

print(full_name(first_name, middle_name, last_name))

'''
'''
#HW-06 Функція форматування рядка

def format_string(string, length):
    if len(string) >= length:
        return string 
    else:
        space = (length - len(string))//2
        new_string = ' '*space + string
        return new_string

string = input('Enter string :')
length = int(input('Enter length :'))

print(format_string(string, length)) 

'''
'''
#HW-07 Робота з довільною кількістю аргументів

def first(size, *arguments): #Збирання аргументів в кортеж  
    return size + len(arguments)

def second(size, **comments): #Збирання аргументів в словник
    return size + len(comments)
'''
'''
#Найбільший спільний дільник GCD

first = int(input('Enter first number : '))
second = int(input('Enter second number :'))

gcd = min(first, second)

while gcd >= 2:
    if first % gcd == 0 and second % gcd == 0:
        break 
    gcd -= 1 

print('Найбільший common divider gcd = ', gcd)
'''
'''
#Код Цезаря Виконує шифрування введеного повідомлення

message = input('Enter your message : ') #Вводимо повідомлення 
offset = int(input('Enter offset : '))   #Вводимо число на яке буде виконуватися зміщення
encoded_message = ''

for ch in message:       #Перебираємо всі введені символи що є вихідному повідомленні
    if ch.isupper:       #Перевіряємо чи символ ВЕЛИКИЙ і заходимо в цикл   
        pos = ord(ch)    #Приймаємо номер позиції символа
        
'''
'''
def fibonacci(n):
    # 0,1,1,2,3,5,8,13,..
    return n if n == 1 or n == 0 else fibonacci(n-2) + fibonacci(n-1)

print(fibonacci(8))
'''
'''
def factorial(n):
    print(n)
    if n == 0 or n ==1:
        return n
    else:
        return n * factorial(n-1)
'''