import csv

from django.shortcuts import render
from django.views import View
# from app import settings
from table.models import Path_to_file, Table_setup
from django.db.models import Max


CSV_FILENAME = 'phones.csv'

Path_to_file().set_path(CSV_FILENAME)




COLUMNS = [
    {'name': 'id', 'width': 1},
    {'name': 'name', 'width': 3},
    {'name': 'price', 'width': 2},
    {'name': 'release_date', 'width': 2},
    {'name': 'lte_exists', 'width': 1},
]

# print('xxxxx')
max_ver_query = Table_setup.objects.all().aggregate(Max('version'))
# version = Table_setup.objects.all()

version = list(max_ver_query.values())[0]
# print(version)
if not (isinstance(version, int)):
    version = 1
else:
    version += 1
# print(version)


for x in range(0, len(COLUMNS)):
    # print(COLUMNS[x]['name'])
    Table_setup.objects.create(name = COLUMNS[x]['name'],
                               number = x+1,
                               width = COLUMNS[x]['width'],
                               version = version)

class TableView(View):

    def get(self, request):
        columns_query = Table_setup.objects.filter(version=version-1).defer('version')
        columns = columns_query.values()
        # print(columns_query)
        with open(CSV_FILENAME, 'rt') as csv_file:
            header = []
            table = []
            table_reader = csv.reader(csv_file, delimiter=';')
            for table_row in table_reader:
                if not header:
                    header = {idx: value for idx, value in enumerate(table_row)}
                else:
                    row = {header.get(idx) or 'col{:03d}'.format(idx): value
                           for idx, value in enumerate(table_row)}
                    table.append(row)

            result = render(request, 'table.html', {'columns': columns, 'table': table, 'csv_file': CSV_FILENAME})
        return result
