# contains the rest endpoints

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('outmessages/', views.outMessageDetails, name='outmessages'),

    path('mail/new', views.mail_new, name='mail_new'),

]