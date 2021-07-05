from django.urls import path
from app01 import views

urlpatterns = [
    path("add_publisher/", views.add_publisher),
    path("publisher_list/", views.publisher_list),
    path("edit_publisher/", views.edit_publisher),
    path("delete_publisher/", views.delete_publisher),
    path("book_list/", views.book_list),
]
