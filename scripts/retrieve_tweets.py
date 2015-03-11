from django.conf import settings
from railtracker.mapfeed.models import Incident
from pprint import pprint
import twitter, httplib, urllib, base64, json

#Functions
def loadIncidents():
    try:
        conn.request("GET", "/Incidents.svc/json/Incidents?%s" % params, "", headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
    except Exception as e:
        pprint("[Errno {0}] {1}".format(e.errno, e.strerror))
    decoded_inc = json.loads(data)
    #Go through incident list and load into database
    for incident in decoded_inc['Incidents']:
        inc_model = Incident(
                description=incident['Description'],
                incident_date=incident['DateUpdated'].replace('T', ' '),
                warning=incident['IncidentType'][:3]
        )
        pprint(inc_model)

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
loadTweets()
