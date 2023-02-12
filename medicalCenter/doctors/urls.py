from django.urls import path, re_path

from .views import *
"""
Создавая urls файл в проекте мы организовали абсолютную независимость
"""

urlpatterns = [
    path('', index, name='home'),  #http://127.0.0.1:8000/ginecologist/
    #1 path('cats/', categories),  # http://127.0.0.1:8000/ginecologist/cats/
    path('cats/<int:catid>/', categories),  # 2 добавили <int:catid> для того чтоб можно было перейти на след страницу
    # re_path(r'^archive/(?P<year>[0-9]{4})/', archive),  #3 на случай если в браузере запросить числа
                                                        #add at views
]
