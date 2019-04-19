from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings

import csv

class InflationView(TemplateView):
    template_name = 'inflation.html'

    def get(self, request, *args, **kwargs):
        with open(settings.INFLATION_DATA) as file:
            inflation_reader = csv.reader(file, delimiter = ';')
            inflation_data = [row for row in inflation_reader]
        context = {'inflation': inflation_data}
        return render(request, self.template_name,
                      context)