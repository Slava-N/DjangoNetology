from django.shortcuts import render

from .models import Route, Station

# Create your views here.


def show_stations(request):
    routes = Route.objects.values_list('name', flat = True)
    route = request.GET.get('route')
    # print(route)
    if route:
        current_route = Route.objects.filter(name = route)[0]
        # print(current_route)
        stations = current_route.stations.all()
        context['stations'] = stations
        stations_ordered_lat = stations.order_by('latitude')
        stations_oredered_long = stations.order_by('longitude')
        x = str(stations_ordered_lat.first().longitude + (stations_ordered_lat.last().longitude - stations_ordered_lat.first().longitude) / 2)
        y = str(stations_oredered_long.first().latitude + (stations_oredered_long.last().latitude - stations_oredered_long.first().latitude) / 2)
        context['center'] = {'y': y, 'x': x}
    return render(request, 'stations.html', context)