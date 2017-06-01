from django.shortcuts import render
from django.views.decorators.cache import cache_page

from django.views.generic import ListView

from . models import Set


class IndexView(ListView):
    template_name = 'index.html'
    model = Set

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context


@cache_page(60 * 15)
def getPhotoSet(request, photoset_slug):
    photoset = Set.objects.get(slug=photoset_slug)

    return render(request, 'set.html', {'photoset': photoset})
