from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import PassengerCarriage, TrainRoute, TrainSquad, Station, TrainOnStationOnDate, TrainRouteWithSquadOnDate, \
    RailwayBranch
from .repositories import StationRepository, PassengerCarriageRepository
from .serializer import PassengerCarriageSerializer
from .serializer import TrainRouteSerializer
from .serializer import TrainSquadSerializer
from .serializer import StationSerializer
from .serializer import TrainOnStationOnDateSerializer
from .serializer import TrainRouteWithSquadOnDateSerializer
from .serializer import RailwayBranchSerializer
import logging
#PassengerCarriage
'''
@api_view(['GET'])
def get_carriage_list(request):
    carriages = PassengerCarriage.objects.all()
    serializer = PassengerCarriageSerializer(carriages, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def get_carriage(request, ID):
    try:
        carriage = PassengerCarriage.objects.get(CarriageID=ID)
    except PassengerCarriage.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = PassengerCarriageSerializer(carriage)
    return Response(serializer.data)
@api_view(['POST'])
def post_carriage(request):
    serializer = PassengerCarriageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['PUT'])
def put_carriage(request, ID):
    try:
        carriage = PassengerCarriage.objects.get(CarriageID=ID)
    except PassengerCarriage.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = PassengerCarriageSerializer(carriage, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['DELETE'])
def delete_carriage(request, ID):
    try:
        carriage = PassengerCarriage.objects.get(CarriageID=ID)
    except PassengerCarriage.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    carriage.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
'''
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
    else:
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
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['DELETE'])
def delete_carriage(request, ID):
    carriage = PassengerCarriageRepository.get(ID)
    if carriage is None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    PassengerCarriageRepository.delete(ID)
    return Response(status=status.HTTP_204_NO_CONTENT)
#TrainRoute
@api_view(['GET'])
def get_route_list(request):
    routes = TrainRoute.objects.all()
    serializer = TrainRouteSerializer(routes, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def get_route(request, ID):
    try:
        route = TrainRoute.objects.get(TrainRouteID=ID)
    except TrainRoute.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = TrainRouteSerializer(route)
    return Response(serializer.data)
@api_view(['POST'])
def post_route(request):
    serializer = TrainRouteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['PUT'])
def put_route(request, ID):
    try:
        route = TrainRoute.objects.get(TrainRouteID=ID)
    except TrainRoute.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = TrainRouteSerializer(route, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['DELETE'])
def delete_route(request, ID):
    try:
        route = TrainRoute.objects.get(TrainRouteID=ID)
    except TrainRoute.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    route.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

#TrainSquad
@api_view(['GET'])
def get_squad_list(request):
    squades = TrainSquad.objects.all()
    serializer = TrainSquadSerializer(squades, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def get_squad(request, ID):
    try:
        squad = TrainSquad.objects.get(TrainSquadID=ID)
    except TrainSquad.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = TrainSquadSerializer(squad)
    return Response(serializer.data)
@api_view(['POST'])
def post_squad(request):
    serializer = TrainSquadSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['PUT'])
def put_squad(request, ID):
    try:
        squad = TrainSquad.objects.get(TrainSquadID=ID)
    except TrainSquad.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = TrainSquadSerializer(squad, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['DELETE'])
def delete_squad(request, ID):
    try:
        squad = TrainSquad.objects.get(TrainSquadID=ID)
    except TrainSquad.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    squad.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

#Station
@api_view(['GET'])
def get_station_list(request):
    stations = Station.objects.all()
    serializer = StationSerializer(stations, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def get_station(request, ID):
    try:
        station = Station.objects.get(StationID=ID)
    except Station.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = StationSerializer(station)
    return Response(serializer.data)
@api_view(['POST'])
def post_station(request):
    serializer = StationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['PUT'])
def put_station(request, ID):
    try:
        station = Station.objects.get(StationID = ID)
    except Station.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = StationSerializer(station, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['DELETE'])
def delete_station(request, ID):
    try:
        station = Station.objects.get(StationID=ID)
    except Station.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    station.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

'''
#TrainOnStationOnDate
@api_view(['GET'])
def get_train_on_station_on_date_list(request):
    res = TrainOnStationOnDate.objects.all()
    serializer = TrainOnStationOnDateSerializer(res, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def get_train_on_station_on_date(request, ID):
    try:
        res = TrainOnStationOnDate.objects.get(CarriageID=ID)
    except TrainOnStationOnDate.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = TrainOnStationOnDateSerializer(res)
    return Response(serializer.data)
@api_view(['POST'])
def post_train_on_station_on_date(request):
    serializer = TrainOnStationOnDateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['PUT'])
def put_train_on_station_on_date(request, ID):
    try:
        res = TrainOnStationOnDate.objects.get(CarriageID=ID)
    except TrainOnStationOnDate.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = StationSerializer(res, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['DELETE'])
def delete_train_on_station_on_date(request, ID):
    try:
        res = TrainOnStationOnDate.objects.get(CarriageID=ID)
    except TrainOnStationOnDate.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    res.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
'''
#TrainRouteWithSquadOnDate
@api_view(['GET'])
def get_route_with_squad_on_date_list(request):
    res = TrainRouteWithSquadOnDate.objects.all()
    serializer = TrainRouteWithSquadOnDateSerializer(res, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def get_train_route_with_squad_on_date(request, ID):
    try:
        res = TrainRouteWithSquadOnDate.objects.get(FullTrainIdentificator=ID)
    except TrainRouteWithSquadOnDate.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = TrainRouteWithSquadOnDateSerializer(res)
    return Response(serializer.data)
@api_view(['POST'])
def post_train_route_with_squad_on_date(request):
    serializer = TrainRouteWithSquadOnDateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['PUT'])
def put_train_route_with_squad_on_date(request, ID):
    try:
        res = TrainRouteWithSquadOnDate.objects.get(FullTrainIdentificator=ID)
    except TrainRouteWithSquadOnDate.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = TrainRouteWithSquadOnDateSerializer(res, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['DELETE'])
def delete_train_route_with_squad_on_date(request, ID):
    try:
        res = TrainRouteWithSquadOnDate.objects.get(FullTrainIdentificator=ID)
    except TrainRouteWithSquadOnDate.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    res.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

#RailwayBranch
@api_view(['GET'])
def get_railway_branch_list(request):
    branch = RailwayBranch.objects.all()
    serializer = RailwayBranchSerializer(branch, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def get_railway_branch(request, ID):
    try:
        res = RailwayBranch.objects.get(RailwayBranchID=ID)
    except RailwayBranch.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = RailwayBranchSerializer(res)
    return Response(serializer.data)
@api_view(['POST'])
def post_railway_branch(request):
    serializer = RailwayBranchSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['PUT'])
def put_railway_branch(request, ID):
    try:
        branch = RailwayBranch.objects.get(RailwayBranchID=ID)
    except RailwayBranch.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = RailwayBranchSerializer(branch, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['DELETE'])
def delete_railway_branch(request, ID):
    try:
        branch = RailwayBranch.objects.get(RailwayBranchID=ID)
    except RailwayBranch.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    branch.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)