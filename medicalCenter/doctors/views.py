from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


# Create your views here.


def index(request):     #HttpRequest на запрос ответ
    return HttpResponse("Страница приложения doctors")

def categories(request, catid):  # add param catid
    if(request.POST):
        print(request.POST)

    return HttpResponse(f'<h1>Статьи по категориям<h1><p>{catid}</p>') #vyvodim stran i molem perehodit


def archive(request, year):
    if int(year) > 2023:
        return redirect('/')
    return HttpResponse(f'<h1>Архив по годам></h1><p>{year}</p>'),

# СОЗДАЕМ ФУНКЦИЮ СТИРАНИЦЫ 404 'NotFound'
def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена </h1>')