import os
import csv
import pandas as pd

# from routing.models import Station, Route
from django.core.management.base import BaseCommand, CommandError

path_to_the_file = '/Users/Slava/developer/django/creating-project/projectnew/moscow_bus_stations.csv'
# >>> apps.get_model('shop', 'Product')
#

class Command(BaseCommand):
    # Задаём текст помощи, который будет
    # отображён при выполнении команды
    # python manage.py createtags --help
    help = 'loads bus-station to the model'


    def handle(self, *args, **options):
        # Получаем аргумент, создаём необходимое количество тегов
        # и выводим сообщение об успешном завершении генерирования
        # self.path_to_file

        # print('xXJJJJJJJJJJJ')
        with open (path_to_the_file, 'r', encoding='cp1251') as csvFile:
            # print('xXJJJJJJJJJJJ')

            # reader = csv.reader(csvFile, delimiter=';', quotechar="\"")
            reader = csv.reader (csvFile, delimiter=';')
            # print(reader)
            fields_name = next(reader, None)
            data_stations = list()
            for row in reader:
                station = dict()
                station['name'] = row[1]
                station['latitude'] = row[3]
                station['longitude'] = row[2]
                # station_data''
                # print(station)
                #
                current_station = Station.objects.create(**station)
                station['routes'] = [route for route in row[7].split(';')]
                print(station)
                for route in station['routes']:
                    try:
                        current_route = Route.objects.get(name = route)
                        current_station.routes.add(current_route)
                    except Route.DoesNotExist:
                        current_route = Route.objects.create(name = route)
                        current_station.routes.add(current_route)
                # data_stations.append(station)
            # fields_name = reader.next ()
            # print(reader)





        self.stdout.write('Successfully created !')