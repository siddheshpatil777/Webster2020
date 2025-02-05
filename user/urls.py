from django.urls import path
from . import views

urlpatterns=[
 path('<slug:slug>/profile/',views.profile,name='profile'),
 path('notifications/',views.notification,name='notifications'),
 path('<user>/following',views.following,name='following'),
 path('<user>/followers',views.followers,name='followers'),
 path('<user>/follow',views.follow,name='follow'),
 path('<user>/unfollow',views.unfollow,name='unfollow'),
 path('test/',views.test,name='test')
]
