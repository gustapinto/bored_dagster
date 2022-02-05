from os import getenv

from psycopg2 import connect


def db():
    return connect(host=getenv("POSTGRES_HOST"), port=getenv("POSTGRES_PORT"),
                   database=getenv("POSTGRE_DATABASE"), user=getenv("POSTGRES_USER"),
                   password=getenv("POSTGRES_PASSWORD"))

def insert(table: str, data: dict) -> None:
    columns = ','.join(data.keys())
    values = ','.join([str(d) for d in data.values()])

    conn = db()
    cursor = conn.cursor()

    cursor.execute(f'insert into {table} ({columns}) values ({values});')

    conn.commit()
    conn.close()
    cursor.close()
