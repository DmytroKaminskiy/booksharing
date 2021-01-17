from django.shortcuts import render
from django.http import HttpResponse

import string
import random


# /hello-world/
# def hello_world():
#     return "Hello World"
# from flask import request


def generate_password(length: int = 10) -> str:
    password = ''
    for _ in range(length):
        password += random.choice(string.ascii_letters)
    return password


def hello_world(request):  # /hello-world/
    length = int(request.GET.get('length') or 10)
    password = generate_password(length)
    return HttpResponse(password)
