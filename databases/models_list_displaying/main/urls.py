"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url
# from django.urls import
from django.contrib import admin
from django.urls import path, re_path
# from books.views import BookListView
# from django import views
# from .. import books
# from books import
# from django.urls import
from books import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.BookListView.as_view()),
    path('books/', views.BookListView.as_view(), name="books_list_view"),
    re_path(r'^books/(?P<date_search>[0-9]{4}-[0-9]{1,2}-[0-9]{1,2})/$', views.BookListView.as_view(), name="books_list_view_2"),
    # url(r'^/([0-9]{4})/([0-9]{2})/([0-9]+)/$', views.BookListView, name="books_list_view")
    # url(r'^/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$', views.BookListView)
]
