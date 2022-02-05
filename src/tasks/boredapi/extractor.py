from concurrent.futures import as_completed

from dagster import op, repository
from requests_futures.sessions import FuturesSession


@op
def extract_boredapi() -> list:
    ENDPOINT = 'https://www.boredapi.com/api/activity'
    TOTAL = 1000

    data = []
    futures = []

    session = FuturesSession()

    for i in range(0, TOTAL):
        future = session.get(ENDPOINT)
        future.i = i

        futures.append(future)

    for future in as_completed(futures):
        response = future.result()

        data.append(response.json())

    return data
