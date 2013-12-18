from django.conf.urls import patterns, url

from blog import views

urlpatterns = patterns('',

    # home page
    # ex: /
    url(r'^$', views.index, name='index'),

    # index page
    # ex: /123/
    url(r'^(?P<selected_page>[\d]+)/$', views.index, name='index'),

    # post detail
    # ex: /p/5/
    url(r'^p/(?P<slug>[\w-]+)/$', views.post_detail, name='post_detail'),

    # category page
    # ex: /c/
    url(r'^c/(?P<category_slug>[\w-]+)$', views.category, name='category'),

    # category page
    # ex: /c/5/
    url(r'^c/(?P<category_slug>[\w-]+)/(?P<selected_page>[\d]+)/$', views.category, name='category'),

    # rss feed
    #ex: /rss/
    url(r'^rss/$', views.Rss(), name='rss'),
)