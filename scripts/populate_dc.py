from django.conf import settings
from pprint import pprint
from railtracker.mapfeed.models import MapStation, MapLine, MapCity
import httplib, urllib, base64
import json

def loadCity():
    c_model = MapCity(
            city_name="Washington D.C.",
            rail_name="Metro",
            twitter_id="MetroRailInfo"
    )
    c_model.save()

def loadLines ():
    try:
        conn.request("GET", "/Rail.svc/json/jLines?%s" % params, "", headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
    except Exception as e:
        pprint("[Errno {0}] {1}".format(e.errno, e.strerror))
    decoded_lines = json.loads(data)
    #Go through line list and load into database
    for line in decoded_lines['Lines']:
        print line['DisplayName']
        city = MapCity.objects.get(city_name="Washington D.C.").id
        l_model = MapLine(
                map_id=city,
                line_name=line['DisplayName'],
                line_code=line['LineCode']
        )
        l_model.save()

def loadStations ():
    city = MapCity.objects.get(city_name="Washington D.C.").id
    try:
        conn.request("GET", "/Rail.svc/json/jStations?%s" % params, "", headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
    except Exception as e:
        pprint("[Errno {0}] {1}".format(e.errno, e.strerror))
    decoded_stations = json.loads(data)
    #Go through station list and load into database
    for station in decoded_stations['Stations']:
        print station['Name']
        try:
            s_model = MapStation.objects.get(station_name=station['Name'])
        except Exception:
            s_model = MapStation(
                    station_name=station['Name'],
                    lat=station['Lat'],
                    lon=station['Lon'],
                    station_code=station['Code']
            )
            s_model.save()
        for x in range(1, 5):
            try:
                line = MapLine.objects.get(line_code=station['LineCode' + str(x)], map=city)
                s_model.lines.add(line)
            except Exception:
                print "Line " + str(x) + " is invalid!"

headers = {
}

params = urllib.urlencode({
    'api_key': settings.DC_PRIMARY_KEY
})

conn = httplib.HTTPSConnection('api.wmata.com')
loadCity()
loadLines()
loadStations()
