from dagster import job

from src.extractors.boredapi import extract_boredapi

@job
def ingest_boredapi() -> None:
    extract_boredapi()
