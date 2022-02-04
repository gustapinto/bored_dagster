from dagster import job
from humanfriendly import parse_date

from .parser import parse_boredapi
from .extractor import extract_boredapi
from .loader import load_boredapi


@job
def ingest_boredapi() -> None:
    raw_data = extract_boredapi()
    parsed_data = parse_boredapi(raw_data)

    load_boredapi(parsed_data)
