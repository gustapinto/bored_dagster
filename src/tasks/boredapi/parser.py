from dagster import op


@op
def parse_boredapi(raw_data: list) -> list:
    data = []

    for d in raw_data:
        activity = d['activity'] or ''
        kind = d['type'] or ''
        participants = d['participants'] or 0
        price = d['price'] or 0.0

        data.append({
            'activity': f"'{activity}'",
            'kind': f"'{kind}'",
            'participants': participants,
            'price': price,
        })

    return data
