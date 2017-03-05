from django.conf.urls import include, url
from django.contrib import admin
import views
import feeds

urlpatterns = [
    url(r'^books/', 'main.views.books'),
    url(r'^articles/', 'main.views.articles'),
    url(r'^blog/(?P<slug>[-\w\d]+),(?P<id>\d+)/$', 'main.views.blog'),
    url(r'^blog/rss/', feeds.RSSFeed()),
    url(r'^interviews/', 'main.views.interviews'),
    url(r'^projects/', 'main.views.projects'),
    url(r'^', 'main.views.home'),
]