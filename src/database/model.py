from os import getenv

from psycopg2 import connect


def db():
    return connect(host=getenv("POSTGRES_HOST"), port=getenv("POSTGRES_PORT"),
                   database=getenv("POSTGRES_HOST"), user=getenv("POSTGRES_USER"),
                   password=getenv("POSTGRES_PASSWORD"))

def insert(table: str, data: dict) -> None:
    columns = ','.join(data.keys())
    values = ','.join([str(d) for d in data.values()])

    cursor = db().cursor()

    cursor.execute(f'insert into {table} ({columns}) values ({values});')

    cursor.close()
