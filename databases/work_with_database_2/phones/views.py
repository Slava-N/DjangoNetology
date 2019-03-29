from django.shortcuts import render
from .models import Phone
import operator

def show_catalog(request):
    # print()
    sort = request.GET.get('sort')
    # phones = Phone.objects.all()



    try:
        phones = Phone.objects.order_by(sort)
    except:
        phones = Phone.objects.all()
    #
    # print(phones)
    # print(auths)

    context = {
        'phones': phones
    }

    return render(
        request,
        'catalog.html',
        context
    )


def show_product(request, slug):
    return render(
        request,
        'product.html',
    )
