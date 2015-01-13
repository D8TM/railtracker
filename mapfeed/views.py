from django.shortcuts import render_to_response, get_object_or_404
from django.conf import settings
from mapfeed.models import MapCity
import twitter

def index(request):
    city_list = MapCity.objects.all()
    return render_to_response('mapfeed/index.html', {'city_list': city_list})

def details(request, city_id):
    city = get_object_or_404(MapCity, pk=city_id)
    
    api = twitter.Api(consumer_key=settings.TWITTER_CONSUMER_KEY, consumer_secret=settings.TWITTER_CONSUMER_SECRET, access_token_key=settings.TWITTER_TOKEN, access_token_secret=settings.TWITTER_TOKEN_SECRET)
    statuses = api.GetUserTimeline(screen_name='MetroRailInfo')

    return render_to_response('mapfeed/details.html', {'city': city, 'statuses': statuses})
