from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article, Profile, User


# def show_articles(request):
#     return render(
#         request,
#         'articles.html'
#     )

def show_article(request, pk):
    # article_id = request.GET.get('pk')
    # print('article ID:', article_id)
    # print(pk)
    article = Article.objects.get(pk=pk)
    # print(.)
    # # if
    # print(User.objects.filter(Profile=request.user))
    user_id = User.objects.filter(username = request.user)
    # print(user_id.pk)
    # print(user_id[0].pk)
    profile_subscription=False
    try:
        profile_subscription = Profile.objects.get(user=user_id[0].pk).has_subscription
    except:
        pass


    # current_client = Profile.objects.get(pk = User.pk)
    # print(current_client.has_subscription)

    # has_rights = Profile.objects.get(user=request.user)



    if article.commercial_article:
        if not(profile_subscription):
            template_name = 'blocked_content.html'
        else:
            template_name = 'article.html'

    else:
        template_name = 'article.html'

    context = {
        'article_title' : article.title,
        'article_text' : article.text
    }

    return render(
        request,
        template_name,
        context=context
    )


class ArticleView(ListView):
    model = Article
    template_name = 'articles.html'
    context_object_name = 'articles'

# class ArticleDetails(DetailView):
#     model = Article
#     context_object_name = 'article'
#     template_name = 'blocked_content.html'
#
#     # print(self.get_object())
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         current_article = self.get_object()
#         print(current_article.commercial_article)
#         print(context)
#         template_name = 'blocked_content.html'
#
#         return context
#
#     # print()
#     # if
#
#
