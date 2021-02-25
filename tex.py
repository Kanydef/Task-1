
# def speak(text):
#     def wrisper(t):
#         return t.lower() + ' ....'
#     return wrisper(text)

# speak('hello world')

# def get_speak_func(text, volume):
#     def whisper():
#         return text.lower() + '...'
#     def yell():
#         return text.upper() + '!'
#     if volume > 0.5:
#         return yell
#     else:
#         return whisper

# print(get_speak_func('hello', 0.7)())

# def get_speak_func(text, volume):
# #     def whisper():
# #         return text.lower() + '...'
# #     def yell():
# #         return text.uimport 

# # import random

# # def guess(num):
# #     for i in range(num):
# #         if i==random.randint(0,num):
# #             return f'yes , {i}'
# #         return 'no'
# # print(guess(5))


# # po = [1,2,3,4]
# # 1 in po
# # print(1 in po))

# # po = [3,5,6,7]
# # print(id(po))

# # import sys

# # print(sys.getrefcount(po))


# def bread(fun):
#     def wraper():
#         print("хлеб")
#         fun()
#         print("хлеб")
#     return wraper

# def salat(fun):
#     def wraper():
#         print("salat")
#         fun()
#         print("salat")
#     return wraper
# @bread
# @salat
# def say():
#     print('мясо')
# # say=bread(salat(say))
# say()

# class Car:
#     def __init__(self, name, poroda):
#         self.__poroda = poroda
#         self.__name =  name
#     def protect(self)

# a = Car('mi', 'cim')
# print(a.__name)

# class Lion:
#     def __init__(self, name):
#         self.name = name

#     def __repl__(self):
#         return f'the line name-{self.name}'

#     def __str__(self):
#         return f'name-{self.name}'

# name = Lion('misha')
# print(name)



 
