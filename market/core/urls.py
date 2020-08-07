from django.urls import path
from .views import book_list, book_detail

urlpatterns = [
    path('', book_list, name='bool-list'),
    path('<slug>/', book_detail, name='book-detail'),
]
app_name='core'