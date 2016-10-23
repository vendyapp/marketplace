from django.conf.urls import patterns, url

from vendy import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^bids/$', views.bids, name='bids'),
    url(r'^manage/$', views.manage, name='manage'),
    url(r'^manage/breezer_f400/$', views.breezer_f400, name='breezer_f400'),
)
