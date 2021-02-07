from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.views.generic import CreateView

from books.models import Book
from books.forms import BookForm


def index(request):
    return render(request, 'index.html')


def book_list(request):
    context = {
        'books_list': Book.objects.all(),
    }

    return render(request, 'books_list.html', context=context)


def book_create(request):
    form_data = request.POST

    if request.method == 'POST':
        form = BookForm(form_data)
        if form.is_valid():
            form.save()
            return redirect('books-list')
    elif request.method == 'GET':
        form = BookForm()

    context = {
        'message': 'BOOK CREATE',
        'form': form,
    }
    return render(request, 'books_create.html', context=context)


class BookCreate(CreateView):
    model = Book
    success_url = reverse('books-list')
    # form_class = BookForm
    # template_name = 'books_create.html'
    fields = (
        'author',
        'title',
        'publish_year',
        'review',
        'condition',
    )


def book_update(request, pk):

    # try:
    #     book_obj = Book.objects.get(pk=pk)
    # except Book.DoesNotExist:
    #     raise Http404(f'Object with id: {pk} not found')
    instance = get_object_or_404(Book, pk=pk)

    form_data = request.POST
    if request.method == 'POST':
        form = BookForm(form_data, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('books-list')
    elif request.method == 'GET':
        form = BookForm(instance=instance)

    context = {
        'message': 'BOOK UPDATE',
        'form': form,
    }
    return render(request, 'books_create.html', context=context)


def book_delete(request, pk):
    instance = get_object_or_404(Book, pk=pk)
    instance.delete()
    return redirect('books-list')


# def login_view(request):
#     form_data = request.POST
#     form_class = LoginForm
#
#     if request.method == 'POST':
#         form = form_class(form_data)
#         if form.is_valid():
#
#             user = authenticate(**form.cleaned_data)
#             if user:
#                 login(request, user)
#             return redirect('books-list')
#
#     elif request.method == 'GET':
#         form = form_class()
#
#     context = {
#         'form': form,
#     }
#     return render(request, 'login.html', context=context)
#
#
# def logout_view(request):
#     logout(request)
#     return redirect('login')
