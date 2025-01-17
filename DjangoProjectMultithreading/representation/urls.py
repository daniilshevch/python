from . import views
from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='index'),
    path('menu/', views.menu_view, name='menu'),
    path('graph_menu/', views.graph_menu_view, name='graph_menu'),
    ##PassengerCarriage
    path('carriages/', views.carriages_operations, name='carriages'),
    path('passenger_carriages/<int:pk>/', views.passenger_carriage_detail, name='passenger_carriage_detail'),
    path('passenger_carriages/add/', views.passenger_carriage_add, name='passenger_carriage_add'),
    path('passenger_carriages/<int:pk>/edit/', views.passenger_carriage_edit, name='passenger_carriage_edit'),
    path('carriages/get/', views.carriages_get, name='carriages_get'),
    path('carriages/get-id/', views.carriages_get_by_id, name='carriages_get_by_id'),
    path('carriages/post/', views.carriages_post, name='carriages_post'),
    path('carriages/put/', views.carriages_put, name='carriages_put'),
    path('carriages/delete/', views.carriages_delete, name='carriages_delete'),
    ##RailwayBranch
    path('railway_branches/', views.railway_branches_operations, name='railway_branches'),
    path('railway_branches/<int:pk>/', views.railway_branch_detail, name='railway_branch_detail'),
    path('railway_branches/add/', views.railway_branch_add, name='railway_branch_add'),
    path('railway_branches/<int:pk>/edit/', views.railway_branch_edit, name='railway_branch_edit'),
    path('railway_branches/get/', views.railway_branches_get, name='railway_branches_get'),
    path('railway_branches/get-id/', views.railway_branches_get_by_id, name='railway_branches_get_by_id'),
    path('railway_branches/post/', views.railway_branches_post, name='railway_branches_post'),
    path('railway_branches/put/', views.railway_branches_put, name='railway_branches_put'),
    path('railway_branches/delete/', views.railway_branches_delete, name='railway_branches_delete'),

    ##Station
    path('stations/', views.stations_operations, name='stations'),
    path('stations/get/', views.stations_get, name='stations_get'),
    path('stations/get-id/', views.stations_get_by_id, name='stations_get_by_id'),
    path('stations/post/', views.stations_post, name='stations_post'),
    path('stations/put/', views.stations_put, name='stations_put'),
    path('stations/delete/', views.stations_delete, name='stations_delete'),
    path('stations/<int:pk>/', views.station_detail, name='station_detail'),
    path('stations/add/', views.station_add, name='station_add'),
    path('stations/<int:pk>/edit/', views.station_edit, name='station_edit'),
    ##TrainRoute

    path('train_routes/', views.train_routes_operations, name='train_routes'),
    path('train_routes/get/', views.train_routes_get, name='train_routes_get'),
    path('train_routes/get-id/', views.train_routes_get_by_id, name='train_routes_get_by_id'),
    path('train_routes/post/', views.train_routes_post, name='train_routes_post'),
    path('train_routes/put/', views.train_routes_put, name='train_routes_put'),
    path('train_routes/delete/', views.train_routes_delete, name='train_routes_delete'),
    path('train_routes/<int:pk>/', views.train_route_detail, name='train_route_detail'),
    path('train_routes/add/', views.train_route_add, name='train_route_add'),
    path('train_routes/<int:pk>/edit/', views.train_route_edit, name='train_route_edit'),
    path('train_squads/', views.train_squads_operations, name='train_squads'),
    path('train_squads/get/', views.train_squads_get, name='train_squads_get'),
    path('train_squads/get-id/', views.train_squads_get_by_id, name='train_squads_get_by_id'),
    path('train_squads/post/', views.train_squads_post, name='train_squads_post'),
    path('train_squads/put/', views.train_squads_put, name='train_squads_put'),
    path('train_squads/delete/', views.train_squads_delete, name='train_squads_delete'),
    path('train_squads/<int:pk>/', views.train_squad_detail, name='train_squad_detail'),
    path('train_squads/add/', views.train_squad_add, name='train_squad_add'),
    path('train_squads/<int:pk>/edit/', views.train_squad_edit, name='train_squad_edit'),
    path('train_routes_with_squads/', views.train_route_with_squads_operations, name='train_routes_with_squads'),
    path('train_routes_with_squads/get/', views.train_routes_with_squads_get, name='train_routes_with_squads_get'),
    path('train_routes_with_squads/get-id/', views.train_routes_with_squads_get_by_id, name='train_routes_with_squads_get_by_id'),
    path('train_routes_with_squads/post/', views.train_routes_with_squads_post, name='train_routes_with_squads_post'),
    path('train_routes_with_squads/put/', views.train_routes_with_squads_put, name='train_routes_with_squads_put'),
    path('train_routes_with_squads/delete/', views.train_routes_with_squads_delete, name='train_routes_with_squads_delete'),
    path('train_routes_with_squads/<int:pk>/', views.train_route_with_squad_detail, name='train_route_with_squad_detail'),
    path('train_routes_with_squads/add/', views.train_route_with_squad_add, name='train_route_with_squad_add'),
    path('train_routes_with_squads/<int:pk>/edit/', views.train_route_with_squad_edit, name='train_route_with_squad_edit'),

]
