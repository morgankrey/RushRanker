from django.conf.urls import patterns,url
from django.conf import settings
from rushranking import views

urlpatterns = patterns('',
   url(r'^$', views.index),
   url(r'^about/$',views.about),
   url(r'^add_rushee/$',views.add_rushee),
   url(r'^edit_rushee/(?P<rushee_id>\w+)$',views.edit_rushee),
   url(r'^add_comment/(?P<rushee_id>\w+)$',views.add_comment),
   url(r'^rushee/(?P<rushee_id>\w+)/$',views.rushee),
   url(r'^rushees/$',views.rushees),
   url(r'^vote/(?P<rushee_id>\w+)/$',views.vote),
   url(r'^horse/(?P<rushee_id>\w+)/$',views.horse),
   url(r'^met/(?P<rushee_id>\w+)/$',views.brotherMet),
   url(r'^game/$',views.game),
   url(r'^register/$',views.register),
   url(r'^login/$',views.user_login),
   url(r'^logout/$',views.user_logout),)