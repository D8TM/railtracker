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

#determine line order for drawing
@register.filter
def determine_line_order(line, station):
    order = 1
    paths = MapPath.objects.filter(station__id=station.id).order_by('line')
    #iterates through each path segment, compares to line given
    for p in paths:
        if line.id == p.line.id:
            return order
        order = order + 1
    return 0

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

@register.filter
def next_station_num_lines(list, key):
    try:
        station = list[key+1]
    except Exception as e:
        station = list[key]
    return station.lines.count

@register.filter
def next_station_name(list, key):
    try:
        station = list[key+1]
    except Exception as e:
        station = list[key]
    return station.station_name
