from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, UpdateView, DeleteView, ListView,
    TemplateView,
)

from books.models import Book


class Index(TemplateView):
    template_name = 'index.html'


class BookList(ListView):
    queryset = Book.objects.all()


class BookCreate(CreateView):
    model = Book
    success_url = reverse_lazy('books:list')
    fields = (
        'author',
        'title',
        'publish_year',
        'review',
        'condition',
    )


class BookUpdate(UpdateView):
    model = Book
    success_url = reverse_lazy('books:list')
    fields = (
        'author',
        'title',
        'publish_year',
        'review',
        'condition',
    )


class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('books:list')
