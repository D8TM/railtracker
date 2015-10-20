from django.conf import settings
from railtracker.mapfeed.models import Incident, MapCity, MapLine
from pprint import pprint
import twitter, httplib, urllib, base64, json

#Functions
def loadIncidents():
    city = MapCity.objects.get(city_name="Washington D.C.").id
    lines = MapLine.objects.filter(map=city)
    try:
        conn.request("GET", "/Incidents.svc/json/Incidents?%s" % params, "", headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
    except Exception as e:
        pprint("[Errno {0}] {1}".format(e.errno, e.strerror))
    decoded_inc = json.loads(data)
    pprint(decoded_inc)
    #Go through incident list and load into database
    for incident in decoded_inc['Incidents']:
        obj_date = incident['DateUpdated'].replace('T', ' ')
        obj_desc = incident['Description']
        num_results = Incident.objects.filter(incident_date=obj_date).filter(description=obj_desc).count()
        if num_results < 1:
            inc_model = Incident(
                    description=obj_desc,
                    incident_date=obj_date,
                    warning=incident['IncidentType'][:3]
            )
            pprint(inc_model)
            inc_model.save()
            pprint(inc_model)
            for line in lines:
                if line.line_code in incident['LinesAffected']:
                    inc_model.lines.add(line)

def loadTweets():
    api = twitter.Api(
            consumer_key=settings.TWITTER_CONSUMER_KEY,
            consumer_secret=settings.TWITTER_CONSUMER_SECRET,
            access_token_key=settings.TWITTER_TOKEN,
            access_token_secret=settings.TWITTER_TOKEN_SECRET
    )
    statuses = api.GetUserTimeline(screen_name='MetroRailInfo')
    for s in statuses:
        if '@' not in s.text:
            pprint(s.text)

#Vars
headers = {
}

params = urllib.urlencode({
    'api_key': settings.DC_PRIMARY_KEY
})

conn = httplib.HTTPSConnection('api.wmata.com')

test_inc = {'Incidents': [{
    'Description': 'This is a test incident.',
    'DateUpdated': '2015-02-04 12:59:59',
}]}

#Calls
loadIncidents()
#loadTweets()
