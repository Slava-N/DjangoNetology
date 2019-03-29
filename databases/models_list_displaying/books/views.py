from django.views import generic
from django.shortcuts import render
from books.models import Book

class BookListView(generic.ListView):
    template_name = 'book_list.html'
    context_object_name = 'books'
    paginate_by = 3
    queryset = Book.objects.all()

    def get_queryset(self):
        try:
            dataset = Book.objects.filter(pub_date__exact=self.kwargs['date_search'])
        except:
            dataset = Book.objects.all()
        return dataset

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
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # Mode
    #     context['book_list'] = Book.objects.all()
    #
    #     #
    #     # return render(
    #     #     request,
    #     #     'book_list.html',
    #     #     context
    #     # )


