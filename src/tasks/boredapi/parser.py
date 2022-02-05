from dagster import op

from src.database.models.activity import Activity


@op
def parse_boredapi(raw_data: list) -> list:
    data = []

    for d in raw_data:
        name = d['activity'].replace("'", "") or ''
        kind = d['type'] or ''
        participants = d['participants']
        price = round(d['price'], 2)

        activity = Activity(name=name, kind=kind, participants=participants,
                            price=price)

        data.append(activity)

    return data
