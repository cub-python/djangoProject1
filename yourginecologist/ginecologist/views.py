from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):     #HttpRequest на запрос ответ
    return HttpResponse("Страница приложения ginecologist")

def categories(request, catid):  # add param catid
    return HttpResponse(f'<h1>Статьи по категориям<h1><p>{catid}</p>') #vyvodim stran i molem perehodit