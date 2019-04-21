import os
import csv
import pandas as pd

from django.contrib.auth.models import User, UserManager
from django.core.management.base import BaseCommand, CommandError



class Command(BaseCommand):
    # Задаём текст помощи, который будет
    # отображён при выполнении команды
    # python manage.py createtags --help
    help = 'creates superuser'


    def handle(self, *args, **options):
        try:
            User.objects.create_user('admin1', 'test@mail.ru', 'admin1', is_superuser = True, is_staff = True)
        except:
            pass

        # with open (path_to_the_file, 'r', encoding='cp1251') as csvFile:
        #     reader = csv.reader (csvFile, delimiter=';')
        #     fields_name = next(reader, None)
        #     data_stations = list()
        #     for row in reader:
        #         station = dict()
        #         station['name'] = row[1]
        #         station['latitude'] = row[3]
        #         station['longitude'] = row[2]
        #         current_station = Station.objects.create(**station)
        #         station['routes'] = [route for route in row[7].split(';')]
        #         print(station)
        #         for route in station['routes']:
        #             try:
        #                 current_route = Route.objects.get(name = route)
        #                 current_station.routes.add(current_route)
        #             except Route.DoesNotExist:
        #                 current_route = Route.objects.create(name = route)
        #                 current_station.routes.add(current_route)
        self.stdout.write('Successfully created !')

class User(UserManager):
