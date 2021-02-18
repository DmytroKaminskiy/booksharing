from django.db import models

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


class Book(models.Model):  # DO NOT TOUCH ME
    title = models.CharField(max_length=128)
    publish_year = models.PositiveSmallIntegerField()
    review = models.CharField(max_length=512)
    condition = models.PositiveSmallIntegerField(null=True)
    # category = FK
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE,
                               null=True, default=None)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL,
                               null=True, default=None)


# add Model Category