from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('book-list/', views.book_list, name='book-list')
]
