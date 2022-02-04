from model import db

def main() -> None:
    cursor = db().cursor()

    cursor.execute('''
        create table if not exists activities (
            id serial primary key,
            activity varchar(100) not null,
            kind varchar(60) not null,
            participants smallint not null ,
            price real not null
        )
    ''')

    cursor.close()

if __name__ == "__main__":
    main()
