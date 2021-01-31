from books.models import Author
from django.db.models.signals import pre_save, post_save, pre_delete
from django.dispatch import receiver


@receiver(pre_save, sender=Author)
def pre_save_edit_first_name_author(sender, instance, **kwargs):
    print('PRE SIGNAL')
    instance.first_name = instance.first_name.capitalize()


# @receiver(post_save, sender=Author)
# def post_save_author(*args, **kwargs):
#     print('POST SIGNAL')


@receiver(pre_save, sender=Author)
def pre_save_edit_last_name_author(sender, instance, **kwargs):
    instance.last_name = instance.last_name.capitalize()
