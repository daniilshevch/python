from django.urls import path
from .views import get_carriage_list, get_carriage, put_carriage, post_carriage, delete_carriage, get_route_list, \
    get_route, post_route, put_route, delete_route, get_squad, get_squad_list, post_squad, put_squad, delete_squad, \
    get_station_list, get_station, post_station, put_station, delete_station,  \
    get_route_with_squad, post_route_with_squad, \
    put_route_with_squad, delete_route_with_squad, get_railway_branch_list, \
    get_railway_branch, post_railway_branch, put_railway_branch, delete_railway_branch

urlpatterns = [
    path('carriages/', get_carriage_list, name='get_carriage_list'),
    path('carriages/<int:ID>/', get_carriage, name='get_carriage'),
    path('carriages/post/' , post_carriage, name='post_carriage' ),
    path('carriages/<int:ID>/put', put_carriage, name='put_carriage' ),
    path('carriages/<int:ID>/delete', delete_carriage, name='delete_carriage' ),
    path('routes/', get_route_list, name='get_route_list'),
    path('routes/<int:ID>/', get_route, name='get_route'),
    path('routes/post/', post_route, name='post_route'),
    path('routes/<int:ID>/put', put_route, name='put_route'),
    path('routes/<int:ID>/delete', delete_route, name='delete_route'),
    path('squads/', get_squad_list, name='get_squad_list'),
    path('squads/<int:ID>/', get_squad, name='get_squad'),
    path('squads/post/', post_squad, name='post_squad'),
    path('squads/<int:ID>/put', put_squad, name='put_squad'),
    path('squads/<int:ID>/delete', delete_squad, name='delete_squad'),
    path('stations/', get_station_list, name='get_station_list'),
    path('stations/<int:ID>/', get_station, name='get_station'),
    path('stations/post/', post_station, name='post_station'),
    path('stations/<int:ID>/put', put_station, name='put_station'),
    path('stations/<int:ID>/delete', delete_station, name='delete_station'),
    path('train_route_with_squad_on_date/<int:ID>/', get_route_with_squad, name='get_train_route_with_squad_on_date'),
    path('train_route_with_squad_on_date/post/', post_route_with_squad, name='post_train_route_with_squad_on_date'),
    path('train_route_with_squad_on_date/<int:ID>/put', put_route_with_squad, name='put_train_route_with_squad_on_date'),
    path('train_route_with_squad_on_date/<int:ID>/delete', delete_route_with_squad, name='delete_train_on_station_on_date'),
    path('railway_branch/', get_railway_branch_list, name='get_railway_branch_list'),
    path('railway_branch/<int:ID>/', get_railway_branch, name='get_railway_branch'),
    path('railway_branch/post/', post_railway_branch, name='post_railway_branch'),
    path('railway_branch/<int:ID>/put', put_railway_branch, name='put_railway_branch'),
    path('railway_branch/<int:ID>/delete', delete_railway_branch, name='delete_railway_branch'),
]