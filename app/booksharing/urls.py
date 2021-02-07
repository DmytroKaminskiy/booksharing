from django.contrib import admin

import debug_toolbar
from django.urls import include, path

from books import views

# from books.models import Book  WRONG


urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/', include('django.contrib.auth.urls')),

    path('', views.index, name='index'),

    path('books/list/', views.book_list, name='books-list'),

    # path('books/create/', views.book_create, name='books-create'),
    path('books/create/', views.BookCreate.as_view(), name='books-create'),
    path('books/update/<int:pk>/', views.book_update, name='books-update'),
    path('books/delete/<int:pk>/', views.book_delete, name='books-delete'),

    # path('books/login/', views.login_view, name='login'),
    # path('books/logout/', views.logout_view, name='logout'),

    path('__debug__/', include(debug_toolbar.urls)),
]
