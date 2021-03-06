import csv
import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, UpdateView, DeleteView, ListView,
    TemplateView, View,
)
from django.http import HttpResponse

from books.forms import BookForm
from books.models import Book, RequestBook
from books.utils import display
from books import model_choices as mch


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

    def get_success_url(self):
        messages.add_message(
            self.request, messages.INFO, 'Book Was Created')

        return super().get_success_url()


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
        if not RequestBook.objects.filter(book=book, recipient=request.user, status=mch.STATUS_IN_PROGRESS).exists():
            RequestBook.objects.create(book=book, recipient=request.user, status=mch.STATUS_IN_PROGRESS)
        return redirect('books:list')


class _ChangeRequestBaseView(LoginRequiredMixin, View):
    CURRENT_STATUS = None
    NEW_STATUS = None
    REDIRECT_NAME = None
    MESSAGE = None

    def get(self, request, request_id):
        request_obj = get_object_or_404(RequestBook, pk=request_id, status=self.CURRENT_STATUS)
        request_obj.status = self.NEW_STATUS
        request_obj.save(update_fields=('status',))

        if self.MESSAGE:
            messages.add_message(request, messages.INFO, self.MESSAGE)

        return redirect(self.REDIRECT_NAME)


class RequestBookConfirm(_ChangeRequestBaseView):
    CURRENT_STATUS = mch.STATUS_IN_PROGRESS
    NEW_STATUS = mch.STATUS_CONFIRMED
    REDIRECT_NAME = 'books:requested-books'
    MESSAGE = 'Book Request Was Confirmed!'


class RequestBookSentViaEmail(_ChangeRequestBaseView):
    CURRENT_STATUS = mch.STATUS_CONFIRMED
    NEW_STATUS = mch.STATUS_SENT_TO_RECIPIENT
    REDIRECT_NAME = 'books:requested-books'


class RequestBookReceivedBook(_ChangeRequestBaseView):
    CURRENT_STATUS = mch.STATUS_SENT_TO_RECIPIENT
    NEW_STATUS = mch.STATUS_RECIPIENT_RECEIVED_BOOK
    REDIRECT_NAME = 'books:my-requested-books'


class RequestBookSentBackToOwner(_ChangeRequestBaseView):
    CURRENT_STATUS = mch.STATUS_RECIPIENT_RECEIVED_BOOK
    NEW_STATUS = mch.STATUS_SENT_BACK_TO_OWNER
    REDIRECT_NAME = 'books:my-requested-books'


class RequestBookOwnerReceivedBack(_ChangeRequestBaseView):
    CURRENT_STATUS = mch.STATUS_SENT_BACK_TO_OWNER
    NEW_STATUS = mch.STATUS_OWNER_RECEIVED_BACK
    REDIRECT_NAME = 'books:requested-books'


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



# class BookApiList(View):
#     def get(self, request):
#         queryset = Book.objects.all()
#         results = [
#             {'id': book.id, 'title': book.title}
#             for book in queryset
#         ]
#         data = {
#             'results': results
#         }
#         return HttpResponse(json.dumps(data), content_type='application/json')
