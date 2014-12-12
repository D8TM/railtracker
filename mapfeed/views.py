from django.shortcuts import render_to_response, get_object_or_404
from mapfeed.models import MapCity

def index(request):
    city_list = MapCity.objects.all()
    return render_to_response('mapfeed/index.html', {'city_list': city_list})

def details(request, city_id):
    c = get_object_or_404(MapCity, pk=city_id)
    return render_to_response('mapfeed/details.html', {'city': c})
