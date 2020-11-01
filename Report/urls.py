from django.urls import path
from . import views

urlpatterns=[
     path('report_post/<id>/',views.create_report,name='report-create'),
     path('repost_list/',views.report_list,name='report-list'),
]