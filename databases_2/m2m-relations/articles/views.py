from django.views.generic import ListView

from articles.models import Article


class ArticleListView(ListView):
    template_name = 'articles/news.html'
    model = Article
    ordering = '-published_at'
    # art_list = Article.objects.get(pk=2).topics.all()
    #
    # print(art_list[0].primary_topic)
