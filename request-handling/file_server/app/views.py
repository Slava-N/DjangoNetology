import datetime
from django.http import Http404


from datetime import datetime as dt
import os
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings

class FileList(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, date=None):
        files_names = os.listdir(settings.FILES_PATH)
        print(date)
        files = []

        for file in files_names:
            file_desc = (os.stat(os.path.join(settings.FILES_PATH, file)))
            file_data = {}
            file_data['name'] = file
            file_data['ctime'] = dt.fromtimestamp(file_desc.st_ctime)
            file_data['mtime'] = dt.fromtimestamp(file_desc.st_mtime)

            if date is not None:
                try:
                    date_formatted = dt.strptime(date, "%Y-%m-%d")
                    if file_data['mtime'].date() == date_formatted.date():
                        files.append(file_data)

                except:
                    pass

        return {
            'files': files
        }

def file_content(request, name='none'):
    try:
        with open(os.path.join(settings.FILES_PATH, name), encoding='utf8') as file:
            file_data = file.read()
    except FileNotFoundError:
        raise Http404('Файл не ннайден')
    

    return render(
        request,
        'file_content.html',
        context={'file_name': name, 'file_content': file_data}
    )

