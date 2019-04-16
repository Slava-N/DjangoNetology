from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.shortcuts import HttpResponseRedirect
from .models import Product, Review
from .forms import ReviewForm


class ProductsList(ListView):
    model = Product
    context_object_name = 'product_list'


class ProductView(DetailView):
    model = Product
    template_name = 'app/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # print('1')
        context['reviews'] = Review.objects.filter(product=self.get_object())
        context['form'] = ReviewForm
        if self.request.session.get('is_review_exist', False):
            # print(self.request.session,'commented')
            context['is_review_exist'] = True
        return context


    def post(self, request, **kwargs):
        is_review_exist = self.request.session.get('is_review_exist', '')
        # if not is_review_exist:
        form = ReviewForm(self.request.POST)
            # print(self.request.POST)
        # print(self.kwargs.get('pk'))
        item_key = self.kwargs.get('pk')
        current_product = Product.objects.get(id=item_key)

        if not is_review_exist:
            Review.objects.create(text=request.POST['text'], product=current_product)
            self.request.session['is_review_exist'] = is_review_exist

        return HttpResponseRedirect(reverse('product_detail', kwargs={'pk': item_key}))
