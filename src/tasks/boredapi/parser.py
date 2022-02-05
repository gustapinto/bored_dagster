from dagster import op

from src.database.models.activity import Activity


@op
def parse_boredapi(raw_data: list) -> list:
    activities = []

    unique_activities = [i for n, i in enumerate(raw_data) if i not in raw_data[n + 1:]]

    for a in unique_activities:
        name = a['activity'].replace("'", "") or ''
        kind = a['type'] or ''
        participants = a['participants']
        price = round(a['price'], 2)

        activity = Activity(name=name, kind=kind, participants=participants,
                            price=price)

        activities.append(activity)

    return activities
