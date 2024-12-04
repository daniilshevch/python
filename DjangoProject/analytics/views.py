from rest_framework.decorators import api_view
from rest_framework.response import Response
import pandas as pd
from django.db.models import Count
from Lab3.models import PassengerCarriage
from analytics.queries import carriages_grouped_by_year_to_dataframe, \
    carriages_grouped_by_manufacturer_and_type_to_dataframe, railway_branches_grouped_by_stations, \
    train_on_station_count, stations_of_train_count, station_by_time_count
from django.http import JsonResponse
import plotly.io as pio
from .graphs import plotly_carriage_by_year, plotly_carriage_by_year, plotly_carriage_by_manufacturer_and_type, \
    plotly_railway_branches_by_stations, plotly_trains_on_station, plotly_stations_of_train, plotly_station_by_time
from django.shortcuts import render
import plotly.express as px
from .queries import carriages_grouped_by_year_to_dataframe, calculate_statistics
from bokeh.resources import INLINE
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
from bokeh.embed import components
from bokeh.resources import INLINE
from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import ColumnDataSource
import logging
from bokeh.transform import cumsum
from bokeh.palettes import Category20c
import pandas as pd
from math import pi
@api_view(['GET'])
def carriages_by_year(request):
    df = carriages_grouped_by_year_to_dataframe()
    df = df.fillna('Unknown')
    response_data = df.to_dict(orient='records')
    return Response(response_data)
@api_view(['GET'])
def carriages_by_manufacturer_and_type(request):
    df = carriages_grouped_by_manufacturer_and_type_to_dataframe()
    df = df.fillna('Unknown')
    response_data = df.to_dict(orient='records')
    return Response(response_data)
@api_view(['GET'])
def railway_branches_by_stations(request):
    df = railway_branches_grouped_by_stations()
    df = df.fillna('Unknown')
    response_data = df.to_dict(orient='records')
    return Response(response_data)
@api_view(['GET'])
def train_on_station(request):
    df = train_on_station_count()
    df = df.fillna('Unknown')
    response_data = df.to_dict(orient='records')
    return Response(response_data)
@api_view(['GET'])
def stations_of_train(request):
    df = stations_of_train_count()
    df = df.fillna('Unknown')
    response_data = df.to_dict(orient='records')
    return Response(response_data)
@api_view(['GET'])
def stations_by_time(request):
    df = station_by_time_count()
    df = df.fillna('Unknown')
    response_data = df.to_dict(orient='records')
    return Response(response_data)

def plotly_carriage_by_year_view(request):
    df = carriages_grouped_by_year_to_dataframe()
    fig = plotly_carriage_by_year(df)
    graph_json = fig.to_json()
    graph_json = fig.to_json()
    return render(request, 'analytics/carriage_by_year.html', {'graph_json': graph_json})
def plotly_carriage_by_year_interactive_view(request):
    df = carriages_grouped_by_year_to_dataframe()
    fig = plotly_carriage_by_year(df)
    graph_json = fig.to_json()
    return render(request, 'analytics/carriage_by_year_interactive.html', {'graph_json': graph_json})

def plotly_carriages_by_manufacturer_and_type_view(request):
    df = carriages_grouped_by_manufacturer_and_type_to_dataframe()
    fig = plotly_carriage_by_manufacturer_and_type(df)
    graph_json = fig.to_json()
    return render(request, 'analytics/carriage_by_manufacturer_and_type.html', {'graph_json': graph_json})


def plotly_railway_branches_by_stations_view(request):
    df = railway_branches_grouped_by_stations()
    fig = plotly_railway_branches_by_stations(df)
    graph_json = fig.to_json()
    return render(request, 'analytics/railway_branches_by_stations.html', {'graph_json': graph_json})


def plotly_trains_on_station_view(request):
    df = train_on_station_count()
    fig = plotly_trains_on_station(df)
    graph_json = fig.to_json()
    return render(request, 'analytics/trains_on_station.html', {'graph_json': graph_json})


def plotly_stations_of_train_view(request):
    df = stations_of_train_count()
    fig = plotly_stations_of_train(df)
    graph_json = fig.to_json()
    return render(request, 'analytics/stations_of_train.html', {'graph_json': graph_json})


def plotly_station_by_time_view(request):
    df = station_by_time_count()
    fig = plotly_station_by_time(df)
    graph_json = fig.to_json()
    return render(request, 'analytics/station_by_time.html', {'graph_json': graph_json})


def bokeh_carriage_by_year_view(request):
    try:
        df = carriages_grouped_by_year_to_dataframe()
        if df.empty:
            return render(request, 'analytics/error.html', {'message': 'Дані для графіка відсутні.'})
        df['ProductionYear'] = pd.to_numeric(df['ProductionYear'], errors='coerce')
        df = df.dropna(subset=['ProductionYear'])
        df['ProductionYear'] = df['ProductionYear'].astype(int).astype(str)
        source = ColumnDataSource(df)
        p = figure(
            title="Вагони за роками виробництва",
            x_axis_label='Рік виробництва',
            y_axis_label='Кількість вагонів',
            x_range=df['ProductionYear'],
            sizing_mode='stretch_width',
            height=500
        )
        p.vbar(x='ProductionYear', top='count', width=0.8, source=source)
        script, div = components(p, INLINE)
        resources = INLINE.render()
        return render(request, 'analytics/bokeh_carriage_by_year.html', {
            'script': script,
            'div': div,
            'resources': resources,
        })
    except Exception as e:
        return render(request, 'analytics/error.html', {'message': 'Сталася помилка під час побудови графіка.'})
from bokeh.models import ColumnDataSource



def bokeh_carriages_by_manufacturer_and_type_view(request):
    try:
        df = carriages_grouped_by_manufacturer_and_type_to_dataframe()
        if df.empty:
            return render(request, 'analytics/error.html', {'message': 'Дані для графіка відсутні.'})
        df['label'] = df['TypeOf'] + " (" + df['Manufacturer'] + ")"
        df = df.dropna(subset=['count', 'label'])
        df['angle'] = df['count'] / df['count'].sum() * 2 * pi
        df['color'] = Category20c[len(df)] if len(df) <= 20 else Category20c[20]
        source = ColumnDataSource(df)
        p = figure(
            height=500,
            title="Кругова діаграма вагонів за типом і виробником",
            toolbar_location=None,
            tools="hover",
            tooltips="@label: @count",
            x_range=(-0.5, 1)
        )
        p.wedge(
            x=0,
            y=0,
            radius=0.4,
            start_angle=cumsum('angle', include_zero=True),
            end_angle=cumsum('angle'),
            line_color="white",
            fill_color='color',
            legend_field='label',
            source=source
        )
        p.axis.axis_label = None
        p.axis.visible = False
        p.grid.grid_line_color = None
        script, div = components(p, INLINE)
        resources = INLINE.render()
        return render(request, 'analytics/bokeh_carriage_by_manufacturer_and_type.html', {
            'script': script,
            'div': div,
            'resources': resources,
        })

    except Exception as e:
        return render(request, 'analytics/error.html', {'message': f'Сталася помилка під час побудови графіка: {str(e)}'})

def bokeh_railway_branches_by_stations_view(request):
    try:
        df = railway_branches_grouped_by_stations()

        if df.empty:
            return render(request, 'analytics/error.html', {'message': 'Дані для графіка відсутні.'})
        df = df.dropna(subset=['station_count', 'RailwayBranchID__Title'])

        df['angle'] = df['station_count'] / df['station_count'].sum() * 2 * pi
        df['color'] = Category20c[len(df)] if len(df) <= 20 else Category20c[20]  # Палітра

        source = ColumnDataSource(df)

        p = figure(
            height=500,
            title="Кількість станцій у залізничних гілках",
            toolbar_location=None,
            tools="hover",
            tooltips="@RailwayBranchID__Title: @station_count",
            x_range=(-0.5, 1)
        )

        p.wedge(
            x=0,
            y=0,
            radius=0.4,
            start_angle=cumsum('angle', include_zero=True),
            end_angle=cumsum('angle'),
            line_color="white",
            fill_color='color',
            legend_field='RailwayBranchID__Title',
            source=source
        )

        p.axis.axis_label = None
        p.axis.visible = False
        p.grid.grid_line_color = None

        script, div = components(p, INLINE)
        resources = INLINE.render()

        return render(request, 'analytics/bokeh_branches_by_stations.html', {
            'script': script,
            'div': div,
            'resources': resources,
        })

    except Exception as e:
        return render(request, 'analytics/error.html', {'message': f'Сталася помилка під час побудови графіка: {str(e)}'})


def bokeh_trains_on_station_view(request):
    try:
        df = train_on_station_count()
        if df.empty:
            return render(request, 'analytics/error.html', {'message': 'Дані для графіка відсутні.'})
        source = ColumnDataSource(df)
        p = figure(
            title="Лінійна діаграма: Кількість унікальних потягів на кожній станції",
            x_axis_label='Станція',
            y_axis_label='Кількість потягів',
            x_range=df['StationID__Title'],
            sizing_mode='stretch_width',
            height=500
        )
        p.line(x='StationID__Title', y='unique_trains', source=source, line_width=2)
        p.circle(x='StationID__Title', y='unique_trains', source=source, size=8)
        script, div = components(p, INLINE)
        resources = INLINE.render()
        return render(request, 'analytics/bokeh_trains_on_station.html', {
            'script': script,
            'div': div,
            'resources': resources,
        })
    except Exception as e:
        return render(request, 'analytics/error.html', {'message': 'Сталася помилка під час побудови графіка.'})

def bokeh_stations_of_train_view(request):
    try:
        df = stations_of_train_count()
        if df.empty:
            return render(request, 'analytics/error.html', {'message': 'Дані для графіка відсутні.'})
        source = ColumnDataSource(df)
        p = figure(
            title="Стовпчикова діаграма: Кількість станцій у маршрутах",
            x_axis_label='Маршрут',
            y_axis_label='Кількість станцій',
            x_range=df['NumberCode'],
            sizing_mode='stretch_width',
            height=500
        )
        p.vbar(x='NumberCode', top='station_count', width=0.8, source=source)
        script, div = components(p, INLINE)
        resources = INLINE.render()
        return render(request, 'analytics/bokeh_stations_of_train.html', {
            'script': script,
            'div': div,
            'resources': resources,
        })
    except Exception as e:
        return render(request, 'analytics/error.html', {'message': 'Сталася помилка під час побудови графіка.'})


def bokeh_station_by_time_view(request):
    try:
        df = station_by_time_count()
        if df.empty:
            return render(request, 'analytics/error.html', {'message': 'Дані для графіка відсутні.'})
        df['stop_duration'] = df['stop_duration'] / 1000
        source = ColumnDataSource(df)
        p = figure(
            title="Лінійна діаграма: Кількість зупинок залежно від тривалості стоянки",
            x_axis_label='Тривалість зупинки (хвилини)',
            y_axis_label='Кількість зупинок',
            sizing_mode='stretch_width',
            height=500
        )
        p.line(x='stop_duration', y='stop_count', source=source, line_width=2)
        p.circle(x='stop_duration', y='stop_count', source=source, size=8)
        script, div = components(p, INLINE)
        resources = INLINE.render()
        return render(request, 'analytics/bokeh_station_by_time.html', {
            'script': script,
            'div': div,
            'resources': resources,
        })
    except Exception as e:
        return render(request, 'analytics/error.html', {'message': 'Сталася помилка під час побудови графіка.'})

def carriages_by_manufacturer_and_type_view_interactive(request):
    df = carriages_grouped_by_manufacturer_and_type_to_dataframe()

    graph_json = generate_interactive_pie_chart(df)
    return render(request, 'analytics/carriages_by_manufacturer_and_type_interactive.html', {'graph_json': graph_json})

def generate_interactive_pie_chart(df):
    df['label'] = df['TypeOf'] + " (" + df['Manufacturer'] + ")"

    fig = px.pie(
        df,
        values='count',
        names='label',
        title='Кругова діаграма вагонів за типом і виробником',
        labels={'count': 'Кількість вагонів', 'label': 'Тип і виробник'}
    )
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(template='plotly_white')

    return fig.to_json()


def carriage_statistics_view(request):
    df = carriages_grouped_by_year_to_dataframe()

    statistics = calculate_statistics(df, 'ProductionYear')

    return render(request, 'analytics/carriage_statistics.html', {'statistics': statistics})