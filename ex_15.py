# Напишіть програму, яка буде виконувати найпростіші математичні операції з числами послідовно,
# приймаючи від користувача операнди (числа) та оператор.


result = 0
operand = None
operator = None
wait_for_number = True
temp = 0

# Вводимо першу змінну. Перевіряємо що введено. 
# Якщо число - вихід з циклу. Інший символ, вводимо ще раз.

while wait_for_number:
    operand_1 = input()
    try:
        result = int(operand_1)
    except ValueError:
        print(f'{operand_1} is not number. Try again...')
        continue
    wait_for_number = False

 #Перевірка чи не введено "=" - це закінченя розрахунків.
while operator != '=':

    if wait_for_number == False:
        operator = input()
        if operator not in {'+', '-', '*', '/'}:
            print(f'{operator}) is not +, -, *, / or =. Try again...')
            continue
        wait_for_number = True
        if operator == '=':
            break
    if wait_for_number:
        operand_1 = input()
        try:
            operand = int(operand_1)
        except ValueError:
            print(f'{operand_1} is not number. Try again...')
            continue
        wait_for_number = False

#Блок розрахунків

    if operator == '+':
        result += operand
         
    elif operator == '-':
        result -= operand
    
    elif operator == '*':
        result *= operand
        
    elif operator == '/':
        result = result / operand


print(f' Result = {result}')