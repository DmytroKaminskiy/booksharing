import csv

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, UpdateView, DeleteView, ListView,
    TemplateView, View,
)
from django.http import HttpResponse

from books.forms import BookForm
from books.models import Book, RequestBook
from books.utils import display


class FormUserKwargMixin:
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class Index(TemplateView):
    template_name = 'index.html'


class BookList(ListView):
    queryset = Book.objects.all().select_related('author')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.exclude(user=self.request.user)


class MyBooksList(LoginRequiredMixin, ListView):
    queryset = Book.objects.all().select_related('author')
    template_name = 'books/my_books.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


class MyRequestedBooks(LoginRequiredMixin, ListView):
    queryset = RequestBook.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(recipient=self.request.user)


class RequestedBooks(LoginRequiredMixin, ListView):
    queryset = RequestBook.objects.all()
    template_name = 'books/requested_book_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(book__user=self.request.user)


class BookCreate(FormUserKwargMixin, CreateView):
    model = Book
    success_url = reverse_lazy('books:my-books')
    form_class = BookForm


class BookUpdate(FormUserKwargMixin, UpdateView):
    model = Book
    success_url = reverse_lazy('books:my-books')
    form_class = BookForm


class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('books:list')


class RequestBookCreate(LoginRequiredMixin, View):

    def get(self, request, book_id):
        book = get_object_or_404(Book, pk=book_id)
        if not RequestBook.objects.filter(book=book, recipient=request.user).exists():
            RequestBook.objects.create(book=book, recipient=request.user, status=10)
        return redirect('books:list')


class RequestBookConfirm(LoginRequiredMixin, View):

    def get(self, request, request_id):
        request_obj = get_object_or_404(RequestBook, pk=request_id, status=10)  # TODO
        request_obj.status = 20
        request_obj.save(update_fields=('status', ))
        return redirect('books:requested-books')


class DownloadCSVBookView(View):

    HEADERS = (
        'id',
        'title',
        'author.full_name',
        'author.get_full_name',
        'publish_year',
        'condition',
    )

    def get(self, request):
        # Create the HttpResponse object with the appropriate CSV header.
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

        writer = csv.writer(response)

        writer.writerow(self.HEADERS)

        for book in Book.objects.all().select_related('author').iterator():  # TODO add only method!
            writer.writerow([
                display(book, header)
                for header in self.HEADERS
            ])

        return response


# response = req.get(...)
# response.read()
