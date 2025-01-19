from django.db.models import Count
from Lab3.models import PassengerCarriage
from Lab3.models import Station
from Lab3.models import TrainOnStationOnDate
from Lab3.models import TrainRoute
import pandas as pd
from django.db.models import Count, F, ExpressionWrapper, fields, Q

def carriages_grouped_by_year_to_dataframe():
    data = PassengerCarriage.objects.values('ProductionYear').annotate(
        count=Count('CarriageID')
    ).order_by('ProductionYear')
    df = pd.DataFrame(list(data))
    df['ProductionYear'] = pd.to_numeric(df['ProductionYear'], errors='coerce')
    df = df.dropna(subset=['ProductionYear'])
    return df
def carriages_grouped_by_manufacturer_and_type_to_dataframe():
    data = PassengerCarriage.objects.values('TypeOf', 'Manufacturer').annotate(
        count=Count('CarriageID')
    ).order_by('TypeOf', 'Manufacturer')
    df = pd.DataFrame(list(data))
    df['TypeOf'] = df['TypeOf'].fillna('Невідомо')
    df['Manufacturer'] = df['Manufacturer'].fillna('Невідомо')
    return df
def railway_branches_grouped_by_stations():
    data =  Station.objects.values('RailwayBranchID__Title').annotate(
    station_count=Count('StationID')
).filter(
    station_count__gt=1
).order_by('-station_count')
    df = pd.DataFrame(list(data))
    return df
def train_on_station_count():
    data = TrainOnStationOnDate.objects.values('StationID__Title').annotate(
    unique_trains=Count('TrainRouteWithSquadFullIdentificator__TrainRouteID', distinct=True)
).order_by('-unique_trains')
    df = pd.DataFrame(list(data))
    return df
def stations_of_train_count():
    data =  TrainRoute.objects.values('NumberCode', 'FullConnectionName').annotate(
        station_count=Count('trainroutewithsquadondate__trainonstationondate__StationID', distinct=True)
    ).filter(station_count__gt=1).order_by('-station_count')
    df = pd.DataFrame(list(data))
    return df
def station_by_time_count():
    data = TrainOnStationOnDate.objects.annotate(
    stop_duration=ExpressionWrapper(
        F('DepartureTime') - F('ArrivalTime'),
        output_field=fields.DurationField()
    )
).filter(
    ~Q(TypeOf='start') & ~Q(TypeOf='end')
).values(
    'stop_duration'
).annotate(
    stop_count=Count('StationID')
).order_by('stop_duration')
    df = pd.DataFrame(list(data))
    df['stop_duration'] = df['stop_duration'] / 60000000000
    return df


def calculate_statistics(df, column_name):
    if column_name not in df:
        return None

    stats = {
        'mean': df[column_name].mean(),
        'median': df[column_name].median(),
        'min': df[column_name].min(),
        'max': df[column_name].max(),
    }
    return stats



