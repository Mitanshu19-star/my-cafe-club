from django.urls import path
from . import views
urlpatterns =[
    path('', views.members, name ='members'),
    path('order', views.order, name ='order'),
    path('menu', views.menu, name ='menu'),
    path('about/',views.about ,name = 'about'),
    path('profile/', views.profile, name = 'profile'),
    path('login/', views.login , name = 'login'),
    path('index/', views.index , name = 'index'),
    path('navbar/', views.navbar , name = 'navbar'),
    path('contact/', views.contact , name = 'contact'),
    path('home/', views.home , name = 'home'),
    path('register/', views.register , name = 'register'),
]