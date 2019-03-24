from django.shortcuts import render_to_response, redirect
from django.urls import reverse
from .settings import BUS_STATION_CSV
import csv
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import os


def index(request):




    return redirect(reverse(bus_stations))



def bus_stations(request):

    stations = []
    current_page_number = request.GET.get('page', 1)

    with open(BUS_STATION_CSV, encoding='cp1251') as data_file:
        reader = csv.DictReader(data_file)
        for station in reader:
            current_station = {'Name':station['Name'],
                               'Street': station['Street'],
                               'District': station['District']}
            stations.append(current_station)


    p = Paginator(stations, 5)
    page = p.get_page(current_page_number)





    try:
        previous_page = '?page={}'.format(page.previous_page_number())
        # x=1
    except EmptyPage:
        previous_page = ''

    try:
        next_page = '?page={}'.format(page.next_page_number())
    except PageNotAnInteger:
        next_page = ''

    # print(page.previous_page_number())


    return render_to_response('index.html', {'bus_stations': p.page(current_page_number),
                                             'current_page': page,
                                             'next_page_url': next_page,
                                             'prev_page_url': previous_page
                                             }
    #                           context={
    #     'bus_stations': stations,
    #     'current_page': 1,
    #     'prev_page_url': None,
    #     'next_page_url': 'bus_stations/?page=2',
    # }
    )

