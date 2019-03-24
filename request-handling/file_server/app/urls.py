from django.urls import path
import re



# Определите и зарегистрируйте конвертер для определения даты в урлах и наоборот урла по датам

from .views import file_content, FileList

urlpatterns = [
    # path('', test_function, name='test name 1')
    # Определите схему урлов с привязкой к отображениям .views.FileList и .views.file_content
    path('', FileList.as_view(), name='file_list'),
    path('<str:date>/', FileList.as_view(), name='file_list'),
    path(r'files/<str:name>', file_content, name='file_content'),
]
