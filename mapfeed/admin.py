from mapfeed.models import MapPath, MapCity, MapLine, MapStation, Incident, Dict_Entry
from django.contrib import admin
from django import forms

class MapCityAdmin(admin.ModelAdmin):
    list_display = ('city_name', 'rail_name')

class MapLineAdmin(admin.ModelAdmin):
    list_display = ('line_name', 'line_code')

class MapStationAdmin(admin.ModelAdmin):
    list_display = ('station_name', 'station_code')

class IncidentAdmin(admin.ModelAdmin):
    pass

class Dict_EntryAdmin(admin.ModelAdmin):
    list_display = ('lookup', 'translation', 'translation_cat')

class MapPathForm(forms.ModelForm):
    line = forms.ModelChoiceField(queryset=MapLine.objects.order_by('line_name'))

    class Meta:
        model = MapStation

class MapPathAdmin(admin.ModelAdmin):
    form = MapPathForm
    list_display = ('get_line', 'get_station', 'seq_num')

    def get_station(self, obj):
        return obj.station.station_name

    def get_line(self, obj):
        return obj.line.line_name

    get_station.short_description = 'Station'
    get_station.admin_order_field = 'station__station_name'
    get_line.short_description = 'Line'
    get_line.admin_order_field = 'line__line_name'

admin.site.register(MapCity, MapCityAdmin)
admin.site.register(MapLine, MapLineAdmin)
admin.site.register(MapPath, MapPathAdmin)
admin.site.register(MapStation, MapStationAdmin)
admin.site.register(Incident, IncidentAdmin)
admin.site.register(Dict_Entry, Dict_EntryAdmin)
