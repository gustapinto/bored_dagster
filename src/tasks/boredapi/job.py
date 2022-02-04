from dagster import job

from tasks.extractor import extract_boredapi

@job
def ingest_boredapi() -> None:
    extract_boredapi()
