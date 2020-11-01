from django.urls import path
from . import views

urlpatterns=[
 path('<slug:slug>/profile/',views.profile,name='profile'),
 path('notifications/',views.notification,name='notifications'),
 path('<user>/following',views.following,name='following'),
 path('<user>/followers',views.followers,name='followers'),
 path('test/',views.test,name='test')
]
