from django import template
from mapfeed.models import MapPath, MapStation

register = template.Library()

#provide sequenced order of stations
def draw_line(line):
    seq_sta = []
    paths = MapPath.objects.filter(line__id=line.id).order_by('seq_num')
    for p in paths:
        station = MapStation.objects.get(id=p.station.id)
        seq_sta.append(station)
    return {
        'seq_sta' : seq_sta,
        'line' : line,
    }
register.inclusion_tag('mapfeed/path_draw.html')(draw_line)

#returns the next station given a specific key
@register.filter
def next_station_x(list, key):
    try:
        station = list[key+1]
    except Exception as e:
        station = list[key]
    return station.x_coord

@register.filter
def next_station_y(list, key):
    try:
        station = list[key+1]
    except Exception as e:
        station = list[key]
    return station.y_coord
