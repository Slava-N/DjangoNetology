from django.shortcuts import render
from .models import Phone


def show_catalog(request):

    context = {
        'phones_data': Phone.objects.all()
    }

    return render(
        request,
        'catalog.html',
        context
    )
