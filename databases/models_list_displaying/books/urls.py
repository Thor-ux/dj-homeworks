from django.urls import path
from . import views

urlpatterns = [
    path("", views.all_books, name="all_books"),
    path("<str:pub_date>/", views.books_by_date, name="books_by_date"),
]
