from django.conf.urls import url

from pictures import views

urlpatterns = [
 # url(r'^$', views.index, name='index'),
  # url(r'^(?P<user>[^/]+)/$', views.profile),
  url(r'^$', views.IndexView.as_view()),
  # url(r'^(?P<slug>[-\w]+)/$', SetDetailView.as_view(), name='set-detail'),
  # url(r'^([\w-]+)/$', views.PhotoSet.as_view()),
  # url(r'^(?P<photoset_title>[^/W]+)/$', views.photoset, name='photoset',),
  url(r'^(?P<photoset_slug>\S+)/$', views.getPhotoSet, name='getPhotoSet',),
]
