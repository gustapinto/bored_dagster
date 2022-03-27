from dagster import job

from src.tasks.boredapi.parser import parse_boredapi
from src.tasks.boredapi.extractor import extract_boredapi
from src.tasks.boredapi.loader import load_boredapi


@job
def ingest_boredapi() -> None:
    raw_data = extract_boredapi()
    parsed_data = parse_boredapi(raw_data)

    load_boredapi(parsed_data)
