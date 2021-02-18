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
