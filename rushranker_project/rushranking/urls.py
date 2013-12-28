from django.conf.urls import patterns,url
from rushranking import views

urlpatterns = patterns('',
   url(r'^$', views.index),
   url(r'^about/$',views.about),
   url(r'^add_rushee/$',views.add_rushee),
   url(r'^add_comment/(?P<rushee_id>\w+)$',views.add_comment),
   url(r'^rushee/(?P<rushee_id>\w+)/$',views.rushee),)