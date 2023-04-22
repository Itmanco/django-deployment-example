from django.urls import path
from . import views

app_name = 'basic_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('registration/', views.registration, name='registration'),
    path('special/', views.special, name='special'),

]

