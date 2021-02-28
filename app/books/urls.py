from django.urls import path
from books import views

app_name = 'books'

urlpatterns = [
    path('list/', views.BookList.as_view(), name='list'),
    path('list/my-books/', views.MyBooksList.as_view(), name='my-books'),
    path('list/my-requested-books/', views.MyRequestedBooks.as_view(), name='my-requested-books'),
    path('list/requested-books/', views.RequestedBooks.as_view(), name='requested-books'),
    path('requested-books/confirm/<int:request_id>/', views.RequestBookConfirm.as_view(), name='requested-books-confirm'),
    path('create/', views.BookCreate.as_view(), name='create'),
    path('update/<int:pk>/', views.BookUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', views.BookDelete.as_view(), name='delete'),
    path('download/csv/', views.DownloadCSVBookView.as_view(), name='download-csv'),
    path('create/book/request/<int:book_id>/', views.RequestBookCreate.as_view(), name='create-book-request'),
]
