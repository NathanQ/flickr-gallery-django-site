from django.conf.urls import url

from pictures import views

urlpatterns = [
  url(r'^$', views.IndexView.as_view()),
  url(r'^(?P<photoset_slug>\S+)/$', views.getPhotoSet, name='getPhotoSet',),
]
