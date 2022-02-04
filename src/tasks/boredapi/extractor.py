from time import sleep

from dagster import op
from requests import get


@op
def extract_boredapi() -> list:
    ENDPOINT = 'https://www.boredapi.com/api/activity'
    TOTAL = 100
    LIMIT = 10

    data = []

    for _ in range(0, TOTAL, LIMIT):
        data.extend([get(ENDPOINT).json() for _ in range(LIMIT)])

    return data
