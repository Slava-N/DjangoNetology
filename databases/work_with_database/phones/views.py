from django.shortcuts import render
from .models import Phone

def show_catalog(request):

    # phones = Phone.object.all()

    context = {
        'phones': phones
    }
    return render(
        request,
        'catalog.html',
        context
    )


def show_product(request, slug):
    # slug = request.GET.get('slug')



    return render(
        request,
        'product.html',
    )
