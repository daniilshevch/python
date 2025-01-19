import os
import pandas as pd
import plotly.express as px
from django.shortcuts import render
from django.http import JsonResponse
import analytics.multithreading_section
from analytics.multithreading_section import experiment_parallel_execution


def generate_dashboard_graph(refresh=False):
    file_path = "analytics/experiment_results.csv"

    if not refresh and os.path.exists(file_path):
        df = pd.read_csv(file_path)
    else:
        df = experiment_parallel_execution()
        df.to_csv(file_path, index=False)

    fig = px.line(df, x='Threads', y='Time', title='Час виконання залежно від кількості потоків')

    table_html = df.to_html(index=False, classes="table table-striped", border=0)

    return fig.to_html(), table_html


