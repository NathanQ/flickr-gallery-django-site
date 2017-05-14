from django.conf import settings
from django.shortcuts import render_to_response, redirect, render, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse
from django.views.decorators.cache import cache_page
from django.core.cache import cache

from django.views.generic import View, ListView, DetailView

from . models import Flickr_Account, Set



class IndexView(ListView):
	template_name = 'index.html'
	model = Set

	def get_queryset(self):
		return Set.objects.order_by('name')


# @cache_page(60 * 15)
def getPhotoSet(request, photoset_slug):
	photoset = Set.objects.get(slug=photoset_slug)

	return render(request, 'set.html', {'photoset': photoset} )
