# concert/urls.py

from django.contrib import admin
from django.urls import path
from app1 import views
from concert.views import home
from app1.views import concert_detail
from app1.views import book_now

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.Signuppage, name='signup'),
    path('', home, name='home'),
    path('login/', views.LoginPage, name='login'),
    path('home/', views.Homepage, name='home'),
    path('logout/', views.LogoutPage, name='logout'),
    path('about/', views.about, name='about'),
    path('upcoming/', views.upcoming, name='upcoming'),
    path('contact/', views.contact, name='contact'),
    path('concert/<int:concert_id>/', concert_detail, name='concert_detail'),
    path('book_now/<int:concert_id>/', book_now, name='book_now'),
   
]
