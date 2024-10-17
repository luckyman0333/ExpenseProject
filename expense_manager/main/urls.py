from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('cards/', views.card_list_json, name='card_list_json'),
    path('worker/', views.worker_list_json, name='worker_list_json'),
    path('registration/', views.registration_list_json, name='registration_list_json'),
]
