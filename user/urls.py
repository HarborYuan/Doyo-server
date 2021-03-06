from django.urls import path

from user import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('emailverify', views.email_verify, name='emailverify'),
    path('logout', views.logout, name='logout'),
]
