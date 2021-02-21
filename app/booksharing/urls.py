from django.contrib import admin

import debug_toolbar
from django.urls import include, path
# from django.views.generic import TemplateView
from accounts.views import MyProfileView, ContactUsView
from books import views

# from books.models import Book  WRONG


urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/', include('django.contrib.auth.urls')),
    path('books/', include('books.urls')),

    path('', views.Index.as_view(), name='index'),

    # accounts
    path('accounts/my-profile/', MyProfileView.as_view(), name='my-profile'),
    path('accounts/contact-us/', ContactUsView.as_view(), name='contact-us'),

    path('__debug__/', include(debug_toolbar.urls)),
]
