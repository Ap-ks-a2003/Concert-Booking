
# urls.py
from django.urls import path
from .views import concert_detail
from .views import book_now
urlpatterns = [
    # Other URL patterns...
    path('concert/<int:concert_id>/', concert_detail, name='concert_detail'),
    path('book_now/<int:concert_id>/', book_now, name='book_now')
]
