"""
first_name = 'Jason'
second_name = 'Braun'
full_name = first_name + ' ' + second_name
print(full_name)


def amount_payment(payments):
    total_payment = sum(payment for payment in payments if payment > 0)
    return total_payment

# Приклад використання функції
payments = [100, -50, 200, -75, 50, -25]
total_payment = amount_payment(payments)
print("Сума платежу наприкінці місяця:", total_payment)

"""

def amount_payment(payment):
    list_of_payments = [pay_1, pay_2, pay_3]
    sum = 0
    for value in list_of_payments:
        if value > 0:
            sum += value
    return sum
    
#amount_payment(payment)
list_of_payments = [200, -100, 50]
amount_payment(sum)

    