from django.shortcuts import render
from news import views


def index(request):
    return render(request, 'main/index.html')  # представляю, что я УЖЕ нахожусь в папке templates


def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    return render(request, 'main/contacts.html')
