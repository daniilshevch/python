from django.contrib import admin

from Lab3.models import PassengerCarriage, TrainSquad, TrainRouteWithSquadOnDate, TrainRoute, Station, \
    TrainOnStationOnDate, RailwayBranch

class PassengerCarriageAdmin(admin.ModelAdmin):
    list_display = ("CarriageID", "TypeOf", "Manufacturer", "Capacity", "ProductionYear")
    search_fields = ("CarriageID", "TypeOf", "Manufacturer", "Capacity", "ProductionYear")
    list_filter = ("CarriageID", "TypeOf", "Manufacturer", "Capacity", "ProductionYear")
class RailwayBranchAdmin(admin.ModelAdmin):
    list_display = ("Title", "OfficeLocation")
    search_fields = ("Title", "OfficeLocation")
    list_filter = ("Title", "OfficeLocation")
class StationAdmin(admin.ModelAdmin):
    list_display = ("Title", "RailwayBranchID__Title")
    search_fields = ("Title", "RailwayBranchID__Title")
    list_filter = ("Title", "RailwayBranchID__Title")
class TrainRouteAdmin(admin.ModelAdmin):
    list_display = ("NumberCode", "StartingStationID__Title", "DepartureTime",
    "EndingStationID__Title","ArrivalTime")

    def get_railway_branch_title(self, obj):
        return obj.RailwayBranchID.Title
    get_railway_branch_title.short_description = "Railway Branch"
admin.site.register(PassengerCarriage, PassengerCarriageAdmin)
admin.site.register(TrainSquad)
admin.site.register(TrainRoute, TrainRouteAdmin)
admin.site.register(TrainRouteWithSquadOnDate)
admin.site.register(Station, StationAdmin)
admin.site.register(TrainOnStationOnDate)
admin.site.register(RailwayBranch, RailwayBranchAdmin)
