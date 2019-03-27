from django.shortcuts import render
from django.views.generic import TemplateView
import os
from .settings import INFLATION_DATA
import csv
import pandas as pd

class InflationView(TemplateView):
    template_name = 'inflation.html'

    def get(self, request, *args, **kwargs):
        # чтение csv-файла и заполнение контекста
        print(INFLATION_DATA)


        with open('inflation_russia.csv') as file:
            # inflation_rader = pd
            inflation_reader = csv.reader(file, delimiter = ';')
            # inflation_header =
            inflation_data = [row for row in inflation_reader]
            # inflation_data = pd.read_csv(file)
            # inflation_data = csv.DictReader(file)
            print(inflation_data[1:])


        # print()


            # for row in inflation_reader:
            #     print(row)

        # print(inflation_reader)

        context = {'inflation': inflation_data, "x_variable": "test_data"}
        return render(request, self.template_name,
                      context)