# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def __call__(self):
#         return self.name
#
#
# class Dog:
#     def __init__(self, name):
#         self.name = name
#
#
# c1 = Cat('Tom')
# d1 = Dog('Jerry')
# print(c1())
# print(d1())

t = (1, 2, [3, 4])


# t[-1].append(5)
# t[-1] = [3, 4, 5]
# print(t)
# copy vs deepcopy

# def foo(*args, **kwargs):
#     print(args)
#     print(kwargs)


# print(foo(
#     (1, 2), {3: 4}
# ))

# print(foo(
#     *(1, 2), **{3: 4}  # foo(1, 2, 3=4)
# ))

# def foo():
#     try:
#         return 1
#     finally:
#         return 2
#
# a = foo()














# def foo():
#     print(1)
#     print(1)
#     print(1)
#     return 2


#
# class Shape:
#     def area(self):
#         raise NotImplemented('Area method should be implemented')
#
# class Circle(Shape):
#     pass
#
# class Triangle(Shape):
#     pass

class Dog:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        return self.__class__(f'{self.name} {other.name}')

    def __str__(self):
        return self.name


dog_boy = Dog('Sharik')
dog_girl = Dog('Danna')

dog_child = dog_boy + dog_girl + dog_boy + dog_girl
# dog_boy.__add__(dog_girl.__add__(dog_boy.__add__(dog_girl)))

print(dog_child)
# str_value = str(dog_child)  # dog_child.__str__()

# dog_child = dog_boy.__add__(dog_girl)

"""
1. Я могу видеть список книг которые !свободны!б (мои книги)
2. Я могу запросить доступныю книгу
  - Обмен Адрессами!
  - Отметить что книга занята
3. Я могу видеть какие книги я запросил/которые у меня запросили

4. Сменить статус после отправки/получения (подтвердить/отменить)


ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDFx9ngchJm6Xquij/7LXHYHE9u6aq/cbNoj/ahrETuF0jD9es0QbC/CizMQh7th2BnTBKcm5E2kQuynEdTew52XLwmYSFRkJ44FWeNra0XJZxjPQHij0IDj39r96pbKgFKvw12DAeoWJMl8hJAPHiPJcEMIXEYvHSs6DcJmqZQIVqOL3uJ/pDUQS+1V6CnhI+jJGNL87yP/HvIb2F9s4OZ6ftuaHUDphauIn3hU5gATvmQ+9mlz5LTazum5dSfRjOzTQ7gILqq7Mee+fPgkvBxsBX/4Z/3gWPGVOM8nlEOILpD4dPospYqAHCyERFkIvJjSVUBnYJ6my/4EzlJKpHr dmytrokaminskiy@dmytrokaminskiy-All-Series

"""

# t = (1, 2, [3, 4])
# t[-1].append(5)
# print(t)
# #
# t[-1] = [3, 4, 5]

#
# def foo(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
# foo((1, 2), {'3': 4})
# foo(*(1, 2), **{'3': 4})

d1 = {1: 1}
d2 = {2: 2}

d3 = {**d1, **d2}
# d3.update(d1)
# d3.update(d2)

# 1 + 1
# '1' + '1'
# # __add__
# # __enter__ __exit__  with .. as ..:

# def foo():
#     counter = 0
#     while True:
#         print(f'FOO {counter}')
#         yield counter
#         counter += 1
#
# for c in foo():
#     print(c)

# gen = foo()
# gen.__next__()
# gen.__next__()
# gen.__next__()

# https://www.youtube.com/watch?v=ZGfv_yRLBiY&ab_channel=%D0%9E%D0%BB%D0%B5%D0%B3%D0%9C%D0%BE%D0%BB%D1%87%D0%B0%D0%BD%D0%BE%D0%B2

# LEGB
# L - local
# E - enclosing
# G - Global
# B - built-ins min max int str
# globals() locals()

# locals()
#

# def foo():
#     a = 1
#     locals()
#     def bar():
#         locals()
#         nonlocal a
        # print(a)

# https://webdevblog.ru/chto-takoe-deskriptory-i-ih-ispolzovanie-v-python-3-6/
# a = []
# b = []
#
# print(a == b)
# print(a is b)

# https://www.atlassian.com/ru/git/tutorials/comparing-workflows/gitflow-workflow#:~:text=Gitflow%20Workflow%20%E2%80%94%20%D1%8D%D1%82%D0%BE%20%D0%BC%D0%BE%D0%B4%D0%B5%D0%BB%D1%8C%20%D1%80%D0%B0%D0%B1%D0%BE%D1%87%D0%B5%D0%B3%D0%BE,%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D1%83%20%D0%B4%D0%BB%D1%8F%20%D1%83%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F%20%D0%BA%D1%80%D1%83%D0%BF%D0%BD%D1%8B%D0%BC%D0%B8%20%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B0%D0%BC%D0%B8.
