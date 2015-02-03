from mapfeed.models import MapPath, MapCity, MapLine, MapStation, Incident
from django.contrib import admin

class MapCityAdmin(admin.ModelAdmin):
    list_display = ('city_name', 'rail_name')

class MapLineAdmin(admin.ModelAdmin):
    list_display = ('line_name', 'line_code')

class MapPathAdmin(admin.ModelAdmin):
    pass

class MapStationAdmin(admin.ModelAdmin):
    list_display = ('station_name', 'station_code')

class IncidentAdmin(admin.ModelAdmin):
    pass

admin.site.register(MapCity, MapCityAdmin)
admin.site.register(MapLine, MapLineAdmin)
admin.site.register(MapPath, MapPathAdmin)
admin.site.register(MapStation, MapStationAdmin)
admin.site.register(Incident, IncidentAdmin)
