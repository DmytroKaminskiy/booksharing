# from time import sleep, time
#
# CACHE = None
#
#
# def foo():
#     global CACHE
#
#     if CACHE is None:  # 1st run
#         sleep(2)
#         result = 'bar'
#         CACHE = result
#     else:  # 2..n run
#         result = CACHE
#
#     return result
#
# start = time()
#
# print(foo())
# print(foo())
# print(foo())
#
# print(f'took time to execute: {time() - start}')

# LEGB
# L - local
# E - enclosing
# G - global
# B - builtins (len, sum, min, int, str)
# global


# from time import time

# CACHE = {}

# predefined_values = {
#     5: 120,
#     4: 24,
#     3: 6,
# }

# def factorial(n):
#
#     if n in CACHE:
#         # print('CACHE')
#         return CACHE[n]
#
#     # print('COUNT')
#     result = 1
#
#     for num in range(1, n+1):
#         result *= num
#
#     CACHE[n] = result
#
#     return result
#
# start = time()
#
# N = 10_000
# for _ in range(10_000):
#     factorial(N)
#     factorial(N)
#     factorial(N)
#     factorial(N)
#     factorial(N)
#     factorial(N)
#
# print(f'took time to execute: {time() - start}')
from django.utils.functional import cached_property
from time import time

CACHE = {}


def add(a, b):
    key = f'cache_example::add::{a}::{b}'
    print(key)

    if key in CACHE:
        return CACHE[key]

    result = a + b
    CACHE[key] = result
    return result


def diff(a, b):
    key = f'cache_example::diff::{a}::{b}'
    print(key)

    if key in CACHE:
        return CACHE[key]

    result = a - b
    CACHE[key] = result
    return result


print(add(10, 1))
print(diff(10, 1))

# print(add(11, 12))
# print(add(111, 2))


# cached_property