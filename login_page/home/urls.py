from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.login_page, name='login_page'),
    path('signup_page/', views.signup_page, name='signup_page'),
    path('home_page/', views.home_page, name='home_page'),
    path('logout_page/', views.logout_page, name='logout_page'),
]
