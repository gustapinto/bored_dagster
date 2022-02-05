from dagster import op


@op
def parse_boredapi(raw_data: list) -> list:
    data = []

    for d in raw_data:
        activity = d['activity'].replace("'", "") or ''
        kind = d['type'] or ''
        participants = d['participants']
        price = round(d['price'], 2)

        data.append({
            'activity': f"'{activity}'",
            'kind': f"'{kind}'",
            'participants': participants,
            'price': price,
        })

    return data
