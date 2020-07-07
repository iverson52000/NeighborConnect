from django.urls import path
from . import views

app_name = 'first_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('signin', views.signin, name='signin'),
    path('profile', views.profile, name='profile'),
]
