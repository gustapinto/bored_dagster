from dagster import repository

from src.tasks.boredapi.job import ingest_boredapi


@repository
def boredapi_repository():
    return [ingest_boredapi]
