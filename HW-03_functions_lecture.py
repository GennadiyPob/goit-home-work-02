
#Лекція 18-07-2023

# def foo_1() -> int:
#     a: int = 4 # міні коментар
#     b: int = 8 # міні коментар
#     return a + b

# result_1: int = foo_1()
# print('result_1 = ', result_1)

# def foo_2():
#     a = 4
#     b = 8
#     return a + b

# result_2 = foo_2()
# print('result_2 = ', result_2)

# def foo_1(a: int, b: int) -> int:

#Передача параметрів в функцію

# Приклад фун-ції з необмеженою кількістю параметрів
# def print_result(*args): #(*args) - на вхід можемо приймати багато параметрів
#     for value in args:
#        print(value)  
# print_result(2,3,4,5,'',7,8, '2g3h4j') 

# def sum(*args):
#     print(args) # Надрукувати перелік (1, 2, 3, 4, '', 6, 'JADAS')
#     print(type(args)) # вивести тип значень. Буде <class 'tuple'>
#     result = 0
#     for value in args:
#         try:
#             result += float(value)
#         except ValueError:
#             continue
#     return result
# print(sum(1,2,3,4,'',6, 'JADAS'))

# word = {1: "Python", "may" : 45}
# print(word[1])
# print(word['may'])

# def result(a, *args, **kwargs):
#      print(a)
#      print(kwargs)
#      print(kwargs['may']/5)
# result(78, hello = 'Python', may = 45) # після іменних змінних вже нічого не буде.

# def multiply(a, b, c = None):
#     if c is None:
#         return a * b
#     else:
#         return a * b * c
    
# print(multiply(2, 4))    
# print(multiply(2, 4, 3))

# def greetings(**kwargs):
#     name = kwargs.get('name', 'Unknown')
#     age = kwargs.get('age', None)
#     return f'Hello {name}, you have {age} years old'
    
# print(greetings())
# print(greetings(name = 'Gena', age= '47'))


# G L O B A L

# x = 10
# def foo():
#     x = 5
#     print(x)

# foo() # в середині фунції є "свій" х = 5
# print(x) # зовні є "свій" x = 10

# x = 10
# def foo():
#     global x
#     x = 5
#     print(x)

# foo() # в середині фунції є global х = 5
# print(x) # завдяки global фун-я при виклику змінила значення зовнішньої змінної x = 5


# N O N  L O C A L
 
# password = 1234
# print(password)

# def security(password):
#     print(password)
    
#     def devide():
#         nonlocal password
#         print(password)
#         return password / 2
    
#     return devide()

# print(security(3456))


    


# def is_palindrom(word):
#     if len(word) <= 1:
#         return True
#     elif word[0] != word[-1]:
#         return False
#     else:
#         is_palindrom(word[1:-1])

# print(is_palindrom('qwertytrewq'))

# from math import pi as PI
# print(PI)












