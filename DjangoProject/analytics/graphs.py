import plotly.express as px
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import ColumnDataSource
def plotly_carriage_by_year(df):
    fig = px.bar(
        df,
        x='ProductionYear',
        y='count',
        title='Вагони за роками виробництва (Plotly)',
        labels={'ProductionYear': 'Рік виробництва', 'count': 'Кількість вагонів'}
    )
    fig.update_layout(
        xaxis=dict(title='Рік виробництва'),
        yaxis=dict(title='Кількість вагонів'),
        template='plotly_white'
    )
    return fig


def plotly_carriage_by_manufacturer_and_type(df):
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
    return fig

def plotly_railway_branches_by_stations(df):
    fig = px.pie(
        df,
        values='station_count',
        names='RailwayBranchID__Title',
        title='Кількість станцій у залізничних гілках',
        labels={'station_count': 'Кількість станцій', 'RailwayBranchID__Title': 'Залізнична гілка'}
    )
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(template='plotly_white')
    return fig

def plotly_trains_on_station(df):
    fig = px.line(
        df,
        x='StationID__Title',
        y='unique_trains',
        title='Лінійна діаграма: Кількість унікальних потягів на кожній станції',
        labels={'StationID__Title': 'Станція', 'unique_trains': 'Кількість потягів'}
    )
    fig.update_layout(
        xaxis=dict(title='Станція', tickangle=45),
        yaxis=dict(title='Кількість потягів'),
        template='plotly_white'
    )
    return fig

def plotly_stations_of_train(df):

    fig = px.bar(
        df,
        x='NumberCode',
        y='station_count',
        title='Стовпчикова діаграма: Кількість станцій у маршрутах',
        labels={'NumberCode': 'Номер маршруту', 'station_count': 'Кількість станцій'}
    )
    fig.update_layout(
        xaxis=dict(title='Маршрут', tickangle=45),
        yaxis=dict(title='Кількість станцій'),
        template='plotly_white'
    )
    return fig

def plotly_station_by_time(df):
    fig = px.line(
        df,
        x='stop_duration',
        y='stop_count',
        title='Лінійна діаграма: Кількість зупинок залежно від тривалості стоянки',
        labels={'stop_duration': 'Тривалість зупинки (хвилини)', 'stop_count': 'Кількість зупинок'}
    )
    fig.update_layout(
        xaxis=dict(title='Тривалість зупинки (хвилини)'),
        yaxis=dict(title='Кількість зупинок'),
        template='plotly_white'
    )
    return fig



