import datetime

from datetime import datetime as dt
import os
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from .settings import FILES_PATH



# def test_function(request):
#     # x_var = request.GET.get('s')
#     # print(request.GET)
#
#     return HttpResponse(x_var)


class FileList(TemplateView):
    template_name = 'index.html'
    # template_name = 'file_content.html'
    
    def get_context_data(self, date=None):
        # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
        files_names = os.listdir(FILES_PATH)



        files = []

        for file in files_names:
            file_desc = (os.stat(os.path.join(FILES_PATH, file)))
            file_data = {}
            file_data['name'] = file
            file_data['ctime'] = dt.fromtimestamp(file_desc.st_ctime)
            file_data['mtime'] = dt.fromtimestamp(file_desc.st_mtime)

            if date is not None:
                # print(dt.fromtimestamp(file_desc.st_mtime).strftime("%Y-%m-%d"))

                if dt.fromtimestamp(file_desc.st_mtime).strftime("%Y-%m-%d") == date:
                    files.append(file_data)
                # print('sdf')
            else:
                files.append(file_data)

        return {
            'files': files,
            #     [
            #     {'name': 'file_name_1.txt',
            #      'ctime': datetime.datetime(2018, 1, 1),
            #      'mtime': datetime.datetime(2018, 1, 2)}
            # ],
            'date': datetime.date(2018, 1, 1)  # Этот параметр необязательный
        }

def file_content(request, name='none'):
    files = os.listdir(FILES_PATH)
    # print(files)
    with open(os.path.join(FILES_PATH, name), encoding='utf8') as file:
        file_data = file.read()
    # file = os.read(os.path.join(FILES_PATH, name), encoding='utf8')
    # print()
    # print(file_data)
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    return render(
        request,
        'file_content.html',
        context={'file_name': name, 'file_content': file_data}
    )

