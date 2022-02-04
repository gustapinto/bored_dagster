from dagster import op

from src.database.model import insert

@op
def load_boredapi(activities: list) -> None:
    for activity in activities:
        insert('activities', activity)
