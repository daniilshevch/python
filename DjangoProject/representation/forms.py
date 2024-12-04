from django import forms
from Lab3.models import PassengerCarriage

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