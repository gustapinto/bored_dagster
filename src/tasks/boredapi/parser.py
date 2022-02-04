from dagster import op


@op
def parse_boredapi(raw_data: list) -> list:
    data = []

    for activity in raw_data:
        data.append({
            'activity': activity['activity'],
            'kind': activity['type'],
            'participants': activity['participants'],
            'price': float(activity['price']),
        })

    return data
