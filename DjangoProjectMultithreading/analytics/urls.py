from django.urls import path

from .queries import railway_branches_grouped_by_stations
from .views import carriages_by_year, carriages_by_manufacturer_and_type, railway_branches_by_stations, \
    train_on_station, stations_of_train, stations_by_time, plotly_carriage_by_year_view, plotly_carriage_by_year_view, \
    plotly_carriages_by_manufacturer_and_type_view, plotly_railway_branches_by_stations, \
    plotly_railway_branches_by_stations_view, plotly_trains_on_station_view, plotly_stations_of_train_view, \
    plotly_station_by_time_view, carriages_by_manufacturer_and_type_view_interactive, all_graphs_view_linear, \
    all_bokeh_graphs_view_linear
from analytics.views import (
    bokeh_carriage_by_year_view,
bokeh_carriages_by_manufacturer_and_type_view,
bokeh_trains_on_station_view,
bokeh_stations_of_train_view,
bokeh_station_by_time_view,
bokeh_railway_branches_by_stations_view,
carriages_by_year,
plotly_carriage_by_year_interactive_view,
carriage_statistics_view, all_graphs_view, all_bokeh_graphs_view, dashboard_view, refresh_dashboard_data)


urlpatterns = [
    path('carriages_by_year/', carriages_by_year, name='carriages_by_year'),
    path('carriages_by_manufacturer_and_type/', carriages_by_manufacturer_and_type, name='carriages_by_manufacturer_and_type'),
    path('railway_branches_by_stations/', railway_branches_by_stations, name='railway_branches_by_stations'),
    path('trains_on_station/', train_on_station, name='train_on_station'),
    path('stations_of_train/', stations_of_train, name='stations_of_train'),
    path('stations_by_time/', stations_by_time, name='station_by_time'),
    path('plotly_carriage_by_year/', plotly_carriage_by_year_view, name='plotly_carriage_by_year'),
    path('plotly_carriage_by_year_interactive/', plotly_carriage_by_year_interactive_view, name='plotly_carriage_by_year_interactive'),
    path('plotly_carriage_by_manufacturer_and_type', plotly_carriages_by_manufacturer_and_type_view, name = 'plotly_carriage_by_manufacturer_and_type'),
    path('plotly_railway_branches_by_stations', plotly_railway_branches_by_stations_view, name = 'plotly_railway_branches_by_stations'),
    path('plotly_trains_on_station', plotly_trains_on_station_view, name = 'plotly_trains_on_station'),
    path('plotly_stations_of_train', plotly_stations_of_train_view, name = 'plotly_stations_of_train'),
    path('plotly_station_by_time', plotly_station_by_time_view, name = 'plotly_station_by_time'),
    path('bokeh_carriage_by_year/', bokeh_carriage_by_year_view, name='bokeh_carriage_by_year'),
    path('bokeh_carriages_by_manufacturer_and_type/', bokeh_carriages_by_manufacturer_and_type_view, name='bokeh_carriages_by_manufacturer_and_type'),
    path('bokeh_railway_branches_by_stations/', bokeh_railway_branches_by_stations_view, name='bokeh_railway_branches_by_stations'),
    path('bokeh_trains_on_station/', bokeh_trains_on_station_view, name='bokeh_trains_on_station'),
    path('bokeh_stations_of_train/', bokeh_stations_of_train_view, name='bokeh_stations_of_train'),
    path('bokeh_station_by_time/', bokeh_station_by_time_view, name='bokeh_station_by_time'),
    path('carriages_by_manufacturer_and_type_interactive', carriages_by_manufacturer_and_type_view_interactive, name = 'carriages_by_manufacturer_and_type_interactive'),
    path('carriage_statistics/', carriage_statistics_view, name='carriage_statistics'),
    path('all_graphs/', all_graphs_view, name='all_graphs'),
    path('all_bokeh_graphs/', all_bokeh_graphs_view, name='all_bokeh_graphs'),
    path('all_graphs_linear/', all_graphs_view_linear, name='all_graphs_linear'),
    path('all_bokeh_graphs_linear/', all_bokeh_graphs_view_linear, name='all_bokeh_graphs_linear'),
    path('multithreading_dashboard/', dashboard_view, name='multithreading_dashboard'),
    path('refresh_dashboard_data/', refresh_dashboard_data, name='refresh_dashboard_data'),


]


