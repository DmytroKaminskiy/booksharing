from django.core.management.base import BaseCommand
from faker import Faker
import random
from datetime import datetime

from books.models import Book, Author, Category


class Command(BaseCommand):
    help = 'Generate Random Data'  # noqa

    '''
    class Book(models.Model):  # DO NOT TOUCH ME
    author = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    publish_year = models.PositiveSmallIntegerField()
    review = models.CharField(max_length=512)
    condition = models.PositiveSmallIntegerField()
    '''

    def handle(self, *args, **options):
        fake = Faker()

        # generate Categories
        for _ in range(20):
            Category.objects.create(name=fake.word())

        # create authors
        authors = []
        for _ in range(1_000):
            first_name = fake.name()
            last_name = fake.word()
            authors.append(Author(
                first_name=first_name,
                last_name=last_name,
            ))

        Author.objects.bulk_create(authors)

        # create books with random author
        books_list = []

        for _ in range(10_000):
            author = Author.objects.order_by('?').last()
            title = fake.word()
            publish_year = random.randint(0, datetime.now().year)
            review = fake.text()
            condition = random.randint(1, 5)

            books_list.append(Book(
                author=author,
                title=title,
                publish_year=publish_year,
                review=review,
                condition=condition,
            ))

        Book.objects.bulk_create(books_list)
