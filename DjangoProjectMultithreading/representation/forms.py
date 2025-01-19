from django import forms
from Lab3.models import PassengerCarriage, RailwayBranch, Station, TrainRoute, TrainSquad, TrainRouteWithSquadOnDate

class PassengerCarriageForm(forms.ModelForm):
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
            'DepotStationID',
        ]

class RailwayBranchForm(forms.ModelForm):
    class Meta:
        model = RailwayBranch
        fields = [
            'RailwayBranchID',
            'Title',
            'OfficeLocation',
        ]
class StationForm(forms.ModelForm):
    class Meta:
        model = Station
        fields = [
            'StationID',
            'Title',
            'TypeOf',
            'RailwayBranchID',
            'CarriageDepaut',
            'LocomotiveDepaut',
        ]

class TrainRouteForm(forms.ModelForm):
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
            'FrequencyType',
        ]
class TrainSquadForm(forms.ModelForm):
    class Meta:
        model = TrainSquad
        fields = [
            'TrainSquadID',
            'FormingDepotStationID',
        ]
class TrainRouteWithSquadOnDateForm(forms.ModelForm):
    class Meta:
        model = TrainRouteWithSquadOnDate
        fields = [
            'FullTrainIdentificator',
            'TrainRouteID',
            'TrainSquadID',
            'DepartureDate',
            'ArrivalDate',
        ]