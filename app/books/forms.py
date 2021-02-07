from django import forms

from books.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = (
            'author',
            'title',
            'publish_year',
            'review',
            'condition',
        )


# class LoginForm(forms.Form):
#     username = forms.CharField()
#     password = forms.CharField()
