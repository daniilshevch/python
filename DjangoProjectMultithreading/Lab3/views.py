from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .repositories import (
    PassengerCarriageRepository,
    TrainRouteRepository,
    TrainSquadRepository,
    StationRepository,
    TrainOnStationRepository,
    TrainRouteWithSquadOnDateRepository,
    RailwayBranchRepository,
)
from .serializer import (
    PassengerCarriageSerializer,
    TrainRouteSerializer,
    TrainSquadSerializer,
    StationSerializer,
    TrainOnStationOnDateSerializer,
    TrainRouteWithSquadOnDateSerializer,
    RailwayBranchSerializer,
)

# PassengerCarriage
@api_view(['GET'])
def get_carriage_list(request):
    carriages = PassengerCarriageRepository.get_all()
    serializer = PassengerCarriageSerializer(carriages, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_carriage(request, ID):
    carriage = PassengerCarriageRepository.get(ID)
    if carriage is None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = PassengerCarriageSerializer(carriage)
    return Response(serializer.data)

@api_view(['POST'])
def post_carriage(request):
    serializer = PassengerCarriageSerializer(data=request.data)
    if serializer.is_valid():
        PassengerCarriageRepository.add(**serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def put_carriage(request, ID):
    carriage = PassengerCarriageRepository.get(ID)
    if carriage is None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = PassengerCarriageSerializer(carriage, data=request.data)
    if serializer.is_valid():
        PassengerCarriageRepository.update(ID, **serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_carriage(request, ID):
    carriage = PassengerCarriageRepository.get(ID)
    if carriage is None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    PassengerCarriageRepository.delete(ID)
    return Response(status=status.HTTP_204_NO_CONTENT)

# TrainRoute
@api_view(['GET'])
def get_route_list(request):
    routes = TrainRouteRepository.get_all()
    serializer = TrainRouteSerializer(routes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_route(request, ID):
    route = TrainRouteRepository.get(ID)
    if route is None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = TrainRouteSerializer(route)
    return Response(serializer.data)

@api_view(['POST'])
def post_route(request):
    serializer = TrainRouteSerializer(data=request.data)
    if serializer.is_valid():
        TrainRouteRepository.add(**serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def put_route(request, ID):
    route = TrainRouteRepository.get(ID)
    if route is None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = TrainRouteSerializer(route, data=request.data)
    if serializer.is_valid():
        TrainRouteRepository.update(ID, **serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_route(request, ID):
    route = TrainRouteRepository.get(ID)
    if route is None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    TrainRouteRepository.delete(ID)
    return Response(status=status.HTTP_204_NO_CONTENT)

# TrainSquad
@api_view(['GET'])
def get_squad_list(request):
    squads = TrainSquadRepository.get_all()
    serializer = TrainSquadSerializer(squads, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_squad(request, ID):
    squad = TrainSquadRepository.get(ID)
    if squad is None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = TrainSquadSerializer(squad)
    return Response(serializer.data)

@api_view(['POST'])
def post_squad(request):
    serializer = TrainSquadSerializer(data=request.data)
    if serializer.is_valid():
        TrainSquadRepository.add(**serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def put_squad(request, ID):
    squad = TrainSquadRepository.get(ID)
    if squad is None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = TrainSquadSerializer(squad, data=request.data)
    if serializer.is_valid():
        TrainSquadRepository.update(ID, **serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_squad(request, ID):
    squad = TrainSquadRepository.get(ID)
    if squad is None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    TrainSquadRepository.delete(ID)
    return Response(status=status.HTTP_204_NO_CONTENT)

# Station
@api_view(['GET'])
def get_station_list(request):
    stations = StationRepository.get_all()
    serializer = StationSerializer(stations, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_station(request, ID):
    station = StationRepository.get(ID)
    if station is None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = StationSerializer(station)
    return Response(serializer.data)

@api_view(['POST'])
def post_station(request):
    serializer = StationSerializer(data=request.data)
    if serializer.is_valid():
        StationRepository.add(**serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def put_station(request, ID):
    station = StationRepository.get(ID)
    if station is None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = StationSerializer(station, data=request.data)
    if serializer.is_valid():
        StationRepository.update(ID, **serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_station(request, ID):
    station = StationRepository.get(ID)
    if station is None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    StationRepository.delete(ID)
    return Response(status=status.HTTP_204_NO_CONTENT)

# TrainOnStation
@api_view(['GET'])
def get_train_on_station_list(request):
    trains = TrainOnStationRepository.get_all()
    serializer = TrainOnStationOnDateSerializer(trains, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_train_on_station(request, ID):
    train = TrainOnStationRepository.get(ID)
    if train is None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = TrainOnStationOnDateSerializer(train)
    return Response(serializer.data)

@api_view(['POST'])
def post_train_on_station(request):
    serializer = TrainOnStationOnDateSerializer(data=request.data)
    if serializer.is_valid():
        TrainOnStationRepository.add(**serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def put_train_on_station(request, ID):
    train = TrainOnStationRepository.get(ID)
    if train is None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = TrainOnStationOnDateSerializer(train, data=request.data)
    if serializer.is_valid():
        TrainOnStationRepository.update(ID, **serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_train_on_station(request, ID):
    train = TrainOnStationRepository.get(ID)
    if train is None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    TrainOnStationRepository.delete(ID)
    return Response(status=status.HTTP_204_NO_CONTENT)

# TrainRouteWithSquadOnDate
@api_view(['GET'])
def get_route_with_squad_list(request):
    routes = TrainRouteWithSquadOnDateRepository.get_all()
    serializer = TrainRouteWithSquadOnDateSerializer(routes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_route_with_squad(request, ID):
    route = TrainRouteWithSquadOnDateRepository.get(ID)
    if route is None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = TrainRouteWithSquadOnDateSerializer(route)
    return Response(serializer.data)

@api_view(['POST'])
def post_route_with_squad(request):
    serializer = TrainRouteWithSquadOnDateSerializer(data=request.data)
    if serializer.is_valid():
        TrainRouteWithSquadOnDateRepository.add(**serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def put_route_with_squad(request, ID):
    route = TrainRouteWithSquadOnDateRepository.get(ID)
    if route is None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = TrainRouteWithSquadOnDateSerializer(route, data=request.data)
    if serializer.is_valid():
        TrainRouteWithSquadOnDateRepository.update(ID, **serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_route_with_squad(request, ID):
    route = TrainRouteWithSquadOnDateRepository.get(ID)
    if route is None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    TrainRouteWithSquadOnDateRepository.delete(ID)
    return Response(status=status.HTTP_204_NO_CONTENT)

# RailwayBranch
@api_view(['GET'])
def get_railway_branch_list(request):
    branches = RailwayBranchRepository.get_all()
    serializer = RailwayBranchSerializer(branches, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_railway_branch(request, ID):
    branch = RailwayBranchRepository.get(ID)
    if branch is None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = RailwayBranchSerializer(branch)
    return Response(serializer.data)

@api_view(['POST'])
def post_railway_branch(request):
    serializer = RailwayBranchSerializer(data=request.data)
    if serializer.is_valid():
        RailwayBranchRepository.add(**serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def put_railway_branch(request, ID):
    branch = RailwayBranchRepository.get(ID)
    if branch is None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = RailwayBranchSerializer(branch, data=request.data)
    if serializer.is_valid():
        RailwayBranchRepository.update(ID, **serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_railway_branch(request, ID):
    branch = RailwayBranchRepository.get(ID)
    if branch is None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    RailwayBranchRepository.delete(ID)
    return Response(status=status.HTTP_204_NO_CONTENT)
