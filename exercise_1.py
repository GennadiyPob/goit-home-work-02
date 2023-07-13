"""
Ми розробляємо кулінарний блог. І в рецептах, при написанні списку інгредієнтів, ми розділяємо їх комами,
а перед останнім ставимо союз "and", як у прикладі нижче:

2 eggs, 1 liter sugar, 1 tsp salt and vinegar

Напишіть функцію format_ingredients, яка прийматиме на вхід список з інгредієнтів
["2 eggs", "1 liter sugar", "1 tsp salt", "vinegar"] та повертатиме рядок зібраний
з його елементів в описаний вище спосіб. Ваша функція має вміти обробляти списки будь-якої довжини.

"""



#items = []
#items = ["2 eggs"]
#items = ["2 eggs", "1 liter sugar"] 
items = ["2 eggs", "1 liter sugar", "1 tsp salt"] 
#items = ["2 eggs", "1 liter sugar", "1 tsp salt", "vinegar"] 

quantity = int(len(items))
print('Quantity of items = ', quantity)

receip = str('') 
item_number = int(0)
if quantity == 0:
    receip = 'no item'
if quantity == 1:
    receip = items[0]
if quantity == 2:
    receip = items[0] + ' and ' + items[1]
if  quantity > 2:
    for item_number in (quantity - 2):
        receip += items[item_number]
        if  item_number < (quantity - 2):
            receip += ', '
        if item_number == (quantity - 2):
            receip += ' and ' + item_number[quantity-1]
        

print(receip)  