from django.shortcuts import render

from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers
# Create your views here.

def show_mywatchlist(request):
    data_film_mywatchlist = MyWatchList.objects.all()
    context = {
    'list_film': data_film_mywatchlist,
    'nama': 'Eldira Lahanny P S'
    }
    return render(request, "mywatchlist.html", context)

def show_mywatchlist_in_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_mywatchlist_in_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_film_json(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_film_xml(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

