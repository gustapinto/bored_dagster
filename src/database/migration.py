from model import db


def main() -> None:
    conn = db()
    cursor = conn.cursor()

    cursor.execute('''
    create table activities (
        id serial primary key,
        activity varchar(100) not null,
        kind varchar(60) not null,
        participants smallint not null,
        price real not null
    );
    ''')

    conn.commit()
    conn.close()
    cursor.close()

if __name__ == "__main__":
    main()
