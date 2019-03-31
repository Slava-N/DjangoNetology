from django.views import generic
from django.shortcuts import render
from books.models import Book
import datetime


class BookListView(generic.ListView):
    template_name = 'book_list.html'
    context_object_name = 'books'
    paginate_by = 3
    queryset = Book.objects.all()

    def get_queryset(self):
        # print(paginator)
        # print(data)
        try:
            dataset = Book.objects.filter(pub_date__exact=self.kwargs['date_search'])
        except:
            dataset = Book.objects.all()

        return dataset



    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        try:
            data['previous_date'] = Book.objects.filter(pub_date__lt=self.kwargs['date_search']).last().pub_date
        except:
            None

        try:
            data['next_date'] = Book.objects.filter(pub_date__gt=self.kwargs['date_search']).first().pub_date
            # data['next_date'] = next_d.date()

            # print(data['next_date'])
        except:
            None

        print(data)
        return data

        # pass
    #     # filter_val = self.request.GET.get('filter', 'give-default-value')
    #     # queryset = queryset.filter(is_staff=False)
    #     # queryset = Book.objects.filter(date)
    #     pass

    #
    # def get_queryset(self):
    #     """Return the last five published questions."""
    #     return Book.objects.all()
    #     #
    #     # return render(
    #     #     request,
    #     #     'book_list.html',
    #     #     context
    #     # )
    #
    #



