from django.views.generic import TemplateView

from .forms import CalcForm
from django.shortcuts import render


class CalcView(TemplateView):
    template_name = "app/calc.html"
    # print('ok')

    def get(self, request):
        # if this is a POST request we need to process the form data

        # print('ok1')
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            # print('ok2')
            # initial_fee=form.cleaned_data['initial_fee']
            # check whether it's valid:
            if form.is_valid():
                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
                return HttpResponseRedirect('/thanks/')

        # if a GET (or any other method) we'll create a blank form
        else:
            form = CalcForm(self.request.GET)
            if form.is_valid():
                print('ss')
                price = float(request.GET['initial_fee'])
                interest_rate = float(request.GET['rate'])/100
                tenor = float(request.GET['months_count'])
                print(price, interest_rate, tenor)
                context = {
                    'form': form,
                    'total_payment': round(price * (1 + interest_rate * tenor / 12), 1),
                    'monthly_payment': round(price * (1 + interest_rate * tenor / 12) / tenor, 2)
                }

                return render(request, self.template_name, context=context)


        return render(request, self.template_name, {'form': form})