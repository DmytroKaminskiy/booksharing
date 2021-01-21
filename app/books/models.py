from django.db import models

# author (str), title, published (year), review (text)

# int -34, -23459873458734, 238742395834


class Book(models.Model):  # DO NOT TOUCH ME
    author = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    publish_year = models.PositiveSmallIntegerField()
    review = models.CharField(max_length=512)
    condition = models.PositiveSmallIntegerField()


# 1  create author model with fields (first_name, last_name, date_of_birth,
# date_of_death, country, gender, native_language) - pay attention on dataTypes, https://docs.djangoproject.com/en/3.1/ref/models/fields/
class Author:
    pass

# 2 показать список всех авторов по path /books/author/list/
