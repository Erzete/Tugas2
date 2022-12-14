from django.shortcuts import render
from mywatchlist.models import MyWatchlist
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_mywatchlist(request):
	data_watchlist = MyWatchlist.objects.all()
	context = {'list_watchlist': data_watchlist}
	return render(request, "mywatchlist.html", context)

def show_xml(request):
	data = MyWatchlist.objects.all()
	return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
	data = MyWatchlist.objects.all()
	return HttpResponse(serializers.serialize("json", data), content_type="application/json")

