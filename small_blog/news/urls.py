from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home, name="news_home"),  # ничего не пишу в кавычках, т. к. главная страница без "добавок",  а кавычки после названия метода не надо (), т. к. мы не хотим сейчас его выполнить, а просто отправляем название
    path('create', views.create, name='create'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='news_detail'),  # pk = primary key, динамический параметр типа целое
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name='news_update'),
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name='news_delete')
]
