from dagster import op
from sqlalchemy.orm import Session

from src.database.database import engine


@op
def load_boredapi(activities: list) -> None:
    with Session(engine) as session, session.begin():
        session.add_all(activities)
        session.commit()
