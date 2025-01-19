from .models import PassengerCarriage, TrainRoute, TrainSquad, TrainRouteWithSquadOnDate, TrainOnStationOnDate, RailwayBranch, Station
class BaseRepository:
    model = None

    @classmethod
    def get_all(cls):
        return cls.model.objects.all()

    @classmethod
    def get(cls, id):
        try:
            return cls.model.objects.get(pk=id)
        except cls.model.DoesNotExist:
            print("Object not found")
            return None

    @classmethod
    def add(cls, **kwargs):
        return cls.model.objects.create(**kwargs)

    @classmethod
    def update(cls, id, **kwargs):
        obj = cls.get(id)
        if obj:
            for attr, value in kwargs.items():
                setattr(obj, attr, value)
            obj.save()
            return obj
        return None

    @classmethod
    def delete(cls, id):
        obj = cls.get(id)
        if obj:
            obj.delete()



class PassengerCarriageRepository(BaseRepository):
    model = PassengerCarriage

class StationRepository(BaseRepository):
    model = Station

class TrainRouteRepository(BaseRepository):
    model = TrainRoute

class TrainSquadRepository(BaseRepository):
    model = TrainSquad

class TrainRouteWithSquadOnDateRepository(BaseRepository):
    model = TrainRouteWithSquadOnDate

class TrainOnStationRepository(BaseRepository):
    model = TrainOnStationOnDate

class RailwayBranchRepository(BaseRepository):
    model = RailwayBranch

