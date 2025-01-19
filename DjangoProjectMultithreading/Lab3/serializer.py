from rest_framework import serializers
from .models import TrainRoute, TrainSquad, TrainRouteWithSquadOnDate, TrainOnStationOnDate, Station, RailwayBranch, PassengerCarriage
class PassengerCarriageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PassengerCarriage
        fields = [
            'CarriageID',
            'TypeOf',
            'Capacity',
            'Manufacturer',
            'ProductionYear',
            'RenewalInfo',
            'IsInclusive',
            'TrainSquadID',
            'AirConditioning',
            'DepotStationID'
        ]
class TrainRouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainRoute
        fields = [
            'TrainRouteID',
            'NumberCode',
            'FullConnectionName',
            'FormingRailwayBranchID',
            'StartingStationID',
            'DepartureTime',
            'EndingStationID',
            'ArrivalTime',
            'TripFrequency',
            'IsBranded',
            'BrandedName',
            'TripType',
            'SpeedType',
            'FormingType',
            'FrequencyType'
        ]
class TrainSquadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainSquad
        fields = [
            'TrainSquadID',
            'FormingDepotStationID'
        ]
class TrainOnStationOnDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainOnStationOnDate
        fields = [
            'StationID',
            'TrainRouteWithSquadFullIdentificator',
            'ArrivalTime',
            'DepartureTime',
            'TypeOf'
        ]
class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = [
            'StationID',
            'Title',
            'TypeOf',
            'RailwayBranchID',
            'CarriageDepaut',
            'LocomotiveDepaut'
        ]
class RailwayBranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = RailwayBranch
        fields = [
            'RailwayBranchID',
            'Title',
            'OfficeLocation'
        ]
class TrainRouteWithSquadOnDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainRouteWithSquadOnDate
        fields = [
            'FullTrainIdentificator',
            'TrainRouteID',
            'TrainSquadID',
            'DepartureDate',
            'ArrivalDate'
        ]