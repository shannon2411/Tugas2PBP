from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_watchlist_main(request):
    context = {
        'nama' : 'Monica Shannon Clio Aurelie',
        'npm' : '2106751732'
    }
    return render(request, "mywatchlist_main.html", context)

def show_watchlist(request):
    data_movie_mywatchlist = MyWatchList.objects.all()
    context = {
        'list_movie' : data_movie_mywatchlist,
        'nama' : 'Monica Shannon Clio Aurelie',
        'npm' : '2106751732'
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
