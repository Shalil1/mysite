from django.conf.urls import url
from . import views
from django.urls import path,re_path

app_name = 'blog'
urlpatterns = [
        #path('', views.post_list, name='post_list'),
        #path('<int:year>/<int:month>/<int:day>/<int:post>', views.post_detail, name='post_detail'),

        re_path(r'^$', views.post_list, name='post_list'),
        re_path(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$', views.post_detail, name='post_detail'),

]