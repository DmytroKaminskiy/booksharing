from django.urls import path
from books.api import views
from rest_framework.routers import DefaultRouter

# from books.api.views import BookList, BookInstanceView

app_name = 'books-api'

# urlpatterns = [
    # path('api/v1/books/', BookList.as_view()),
    # path('api/v1/books/<int:pk>/', BookInstanceView.as_view()),
# ]

router = DefaultRouter()

router.register('books', views.BookModelViewSet, basename='book')

urlpatterns = router.urls
