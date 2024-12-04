from django.db import models

class PassengerCarriage(models.Model):
    CarriageID = models.IntegerField(db_column='CarriageID', primary_key=True)
    TypeOf = models.CharField(db_column='TypeOf', max_length=8)
    Capacity = models.IntegerField(db_column='Capacity')
    Manufacturer = models.CharField(db_column='Manufacturer', max_length=45)
    ProductionYear = models.TextField(db_column='ProductionYear', blank=True, null=True)
    RenewalInfo = models.CharField(db_column='RenewalInfo', max_length=100, blank=True, null=True)
    IsInclusive = models.IntegerField(db_column='IsInclusive', blank=True, null=True)
    TrainSquadID = models.ForeignKey('TrainSquad', models.DO_NOTHING, db_column='TrainSquadID', blank=True, null=True)
    AirConditioning = models.IntegerField(db_column='AirConditioning', blank=True, null=True)
    DepotStationID = models.ForeignKey('Station', models.DO_NOTHING, db_column='DepotStationID', blank=True, null=True)
    class Meta:
        db_table = 'PassengerCarriage'
    def __str__(self):
        return str(self.CarriageID) + "-" + self.TypeOf + "-" + self.Manufacturer

class RailwayBranch(models.Model):
    RailwayBranchID = models.AutoField(db_column='RailwayBranchID', primary_key=True)
    Title = models.CharField(db_column='Title', max_length=35)
    OfficeLocation = models.CharField(db_column='OfficeLocation', max_length=30)
    class Meta:
        db_table = 'RailwayBranch'
    def __str(self):
        return self.Title

class Station(models.Model):
    StationID = models.IntegerField(db_column='StationID', primary_key=True)
    Title = models.CharField(db_column='Title', max_length=30)
    TypeOf = models.CharField(db_column='TypeOf', max_length=11)
    RailwayBranchID = models.ForeignKey('RailwayBranch', models.DO_NOTHING, db_column='RailwayBranchID', blank=True, null=True)
    CarriageDepaut = models.CharField(db_column='CarriageDepaut', unique=True, max_length=20, blank=True, null=True)
    LocomotiveDepaut = models.CharField(db_column='LocomotiveDepaut', unique=True, max_length=20, blank=True, null=True)
    class Meta:
        db_table = 'Station'
    def __str__(self):
        return self.Title

class TrainOnStationOnDate(models.Model):
    StationID = models.OneToOneField(Station, models.DO_NOTHING, db_column='StationID', primary_key=True)
    TrainRouteWithSquadFullIdentificator = models.ForeignKey('TrainRouteWithSquadOnDate', models.DO_NOTHING, db_column='TrainRouteWithSquadFullIdentificator')
    ArrivalTime = models.DateTimeField(db_column='ArrivalTime', blank=True, null=True)
    DepartureTime = models.DateTimeField(db_column='DepartureTime', blank=True, null=True)
    TypeOf = models.CharField(db_column='TypeOf', max_length=15, blank=True, null=True)
    class Meta:
        db_table = 'TrainOnStationOnDate'
        unique_together = (('StationID', 'TrainRouteWithSquadFullIdentificator'),)

class TrainRoute(models.Model):
    TrainRouteID = models.IntegerField(db_column='TrainRouteID', primary_key=True)
    NumberCode = models.CharField(db_column='NumberCode', unique=True, max_length=7)
    FullConnectionName = models.CharField(db_column='FullConnectionName', unique=True, max_length=50, blank=True, null=True)
    FormingRailwayBranchID = models.ForeignKey('RailwayBranch', models.DO_NOTHING, db_column='FormingRailwayBranchID')
    StartingStationID = models.ForeignKey('Station', models.DO_NOTHING, db_column='StartingStationID')
    DepartureTime = models.TimeField(db_column='DepartureTime')
    EndingStationID = models.ForeignKey('Station', models.DO_NOTHING, db_column='EndingStationID', related_name='trainroute_endingstationid_set')
    ArrivalTime = models.TimeField(db_column='ArrivalTime')
    TripFrequency = models.CharField(db_column='TripFrequency', max_length=30, blank=True, null=True)
    IsBranded = models.IntegerField(db_column='IsBranded')
    BrandedName = models.CharField(db_column='BrandedName', max_length=45, blank=True, null=True)
    TripType = models.CharField(db_column='TripType', max_length=19, blank=True, null=True)
    SpeedType = models.CharField(db_column='SpeedType', max_length=9, blank=True, null=True)
    FormingType = models.CharField(db_column='FormingType', max_length=16, blank=True, null=True)
    FrequencyType = models.CharField(db_column='FrequencyType', max_length=10, blank=True, null=True)
    class Meta:
        db_table = 'TrainRoute'
    def __str__(self):
        return self.NumberCode

class TrainRouteWithSquadOnDate(models.Model):
    FullTrainIdentificator = models.IntegerField(db_column='FullTrainIdentificator', primary_key=True)
    TrainRouteID = models.ForeignKey('TrainRoute', models.DO_NOTHING, db_column='TrainRouteID')
    TrainSquadID = models.ForeignKey('TrainSquad', models.DO_NOTHING, db_column='TrainSquadID')
    DepartureDate = models.DateField(db_column='DepartureDate')
    ArrivalDate = models.DateField(db_column='ArrivalDate')
    class Meta:
        db_table = 'TrainRouteWithSquadOnDate'

class TrainSquad(models.Model):
    TrainSquadID = models.IntegerField(db_column='TrainSquadID', primary_key=True)
    FormingDepotStationID = models.IntegerField(db_column='FormingDepotStationID', blank=True, null=True)
    class Meta:
        db_table = 'TrainSquad'
