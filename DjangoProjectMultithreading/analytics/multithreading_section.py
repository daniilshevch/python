import time
from concurrent.futures import ThreadPoolExecutor
from django.db import connection
import pandas as pd
def fetch_data(pk):
    time.sleep(0.1)
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM TrainRouteWithSquadOnDate WHERE FullTrainIdentificator = %s", [pk])
        result = cursor.fetchone()
    return result

def parallel_execution(thread_count=5, ids=[]):
    start_time = time.time()
    results = []
    with ThreadPoolExecutor(max_workers=thread_count) as executor:
        results = list(executor.map(fetch_data, ids))
    end_time = time.time()
    return results, end_time - start_time

def execute_parallel_test():
    ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for thread_count in [2, 4, 8, 16]:
        results, duration = parallel_execution(thread_count, ids)
        print(f"Threads: {thread_count}, Time: {duration:.2f}s")

def experiment_parallel_execution():

    ids = list(range(1, 201))
    results = []

    for thread_count in [1, 2, 4, 8, 16]:
        execution_results, duration = parallel_execution(thread_count, ids)
        results.append({'Threads': thread_count, 'Time': duration})


    df = pd.DataFrame(results)
    df.to_csv("experiment_results.csv", index=False)
    return df
