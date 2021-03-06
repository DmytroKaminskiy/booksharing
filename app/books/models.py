from django.db import models
from django.core.cache import cache

from books import model_choices as mch

# author (str), title, published (year), review (text)

# int -34, -23459873458734, 238742395834



# 1  create author model with fields (first_name, last_name, date_of_birth,
# date_of_death, country, gender, native_language) - pay attention on dataTypes
# https://docs.djangoproject.com/en/3.1/ref/models/fields/
class Author(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=128)
    gender = models.BooleanField(null=True)
    native_language = models.CharField(max_length=64)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        # args - tuple
        # kwargs - dict
        print('START SAVE')
        # self.first_name = self.first_name.capitalize()
        # self.last_name = self.last_name.capitalize()
        super().save(*args, **kwargs)
        print('END SAVE')

    # def save(self, force_insert=False, force_update=False, using=None,
    #          update_fields=None):
    #     super().save(
    #         force_insert=force_insert, force_update=force_update, using=using,
    #         update_fields=update_fields
    #     )


class Category(models.Model):
    name = models.CharField(max_length=64)

    CACHE_OBJECTS_LIST = 'CategoryList'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self._refresh_cache_objects_list()

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        self._refresh_cache_objects_list()

    @classmethod
    def _refresh_cache_objects_list(cls):
        from books.api.serializers import CategorySerializer  # noqa

        cache.delete(cls.CACHE_OBJECTS_LIST)
        queryset = cls.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        response_data = serializer.data
        cache.set(Category.CACHE_OBJECTS_LIST, response_data, 60 * 60 * 24 * 7)

    def __str__(self):
        return self.name


class Book(models.Model):  # DO NOT TOUCH ME
    title = models.CharField(max_length=128)
    publish_year = models.PositiveSmallIntegerField()
    review = models.CharField(max_length=512)
    condition = models.PositiveSmallIntegerField(null=True)
    # category = FK
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                               null=True, default=None)
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE,
                               null=True, default=None)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL,
                               null=True, default=None)

    # @property
    # def author_full_name(self):
    #     return f"{self.author.first_name} {self.author.last_name}"

    def __str__(self):
        return f"{self.id} {self.title} {self.author_id}"


# add Model Category

class RequestBook(models.Model):

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    recipient = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    status = models.PositiveSmallIntegerField(choices=mch.REQUEST_STATUSES)
