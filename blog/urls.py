from django.conf.urls import url
from django.urls import path, re_path
from . import views

app_name = 'blog'

urlpatterns = [
    #post views
    re_path (r'^$', views.post_list, name='post_list'),
    re_path(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',
    views.post_detail,
    name='post_detail'),
]
