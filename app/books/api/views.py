from rest_framework import generics, viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from django.core.cache import cache

from books.api.filters import BookFilter
from books.api.serializers import BookSerializer, CategorySerializer
from books.models import Book, Category, RequestBook
from books import model_choices as mch


# class BookList(generics.ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#
# class BookInstanceView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookModelViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['condition', 'title']
    filterset_class = BookFilter
    # filterset_fields = ['condition']
    # filterset_fields = {
    #     'title': ['icontains', 'exact'], # filter(title='awda'), filter(title__exact='awda')
    #     'condition': ['gt', 'gte', 'lt', 'lte'],
    # }
    # def list(self, request, *args, **kwargs):
    #     breakpoint()
    #     super().list(request, *args, **kwargs)


class CategoryModelViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = ()
    pagination_class = None

    def list(self, request, *args, **kwargs):

        response_data = cache.get(Category.CACHE_OBJECTS_LIST)
        if response_data is not None:
            return Response(response_data)

        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        response_data = serializer.data
        cache.set(Category.CACHE_OBJECTS_LIST, response_data, 60 * 60 * 24 * 7)  # move to consts

        return Response(response_data)


class CreateRequestView(generics.GenericAPIView):
    authentication_classes = (SessionAuthentication, )
    permission_classes = ()

    def get(self, request, book_id):
        book = get_object_or_404(Book, pk=book_id)
        if not RequestBook.objects.filter(book=book, recipient=request.user, status=mch.STATUS_IN_PROGRESS).exists():
            RequestBook.objects.create(book=book, recipient=request.user, status=mch.STATUS_IN_PROGRESS)
        return Response({'message':'ok'})

# from django.utils.decorators import method_decorator
# from django.views.decorators.cache import cache_page
#
#
# class CategoryModelViewSet(viewsets.ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     permission_classes = ()
#     pagination_class = None
#
#     @method_decorator(cache_page(60 * 60 * 2))
#     def list(self, request, *args, **kwargs):
#         return super().list(request, *args, **kwargs)
