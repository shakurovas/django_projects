from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),  # ничего не пишу в кавычках, т. к. главная страница без "добавок",  а кавычки после названия метода не надо (), т. к. мы не хотим сейчас его выполнить, а просто отправляем название
    path('about/', views.about, name="about"),
    path('contacts/', views.contacts, name="contacts")
]
