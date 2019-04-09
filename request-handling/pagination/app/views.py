from django.shortcuts import render_to_response, redirect
from django.urls import reverse
from django.conf import settings
import csv
from django.core.paginator import Paginator

def index(request):
    return redirect(reverse(bus_stations))



def bus_stations(request):

    stations = []
    current_page_number = request.GET.get('page', 1)

    with open(settings.BUS_STATION_CSV, encoding='cp1251') as data_file:
        reader = csv.DictReader(data_file)
        for station in reader:
            stations.append(station)

    p = Paginator(stations, 10)

    page = p.get_page(current_page_number)

    if page.has_previous():
        previous_page = '?page={}'.format(page.previous_page_number())
    else:
        previous_page = ''

    if page.has_next():
        next_page = '?page={}'.format(page.next_page_number())
    else:
        next_page = ''

    return render_to_response('index.html', {'bus_stations': p.page(current_page_number),
                                             'current_page': page,
                                             'next_page_url': next_page,
                                             'prev_page_url': previous_page
                                             })