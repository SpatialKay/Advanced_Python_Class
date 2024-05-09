from databases.database import SessionLocal, engine, Base

from databases.models import Person


def main() -> None:
    try:
        Base.metadata.create_all(bind=engine)

        db_session = SessionLocal()
        print(f"try session active: {db_session.is_active}")

        # delete all of the records in people
        db_session.query(Person).delete()

        # insert many new people
        people = [
            Person(first_name="Alice", last_name="Wonderland", age=25),
            Person(first_name="Bob", last_name="Smith", age=42),
            Person(first_name="Charlie", last_name="Brown", age=32),
            Person(first_name="David", last_name="Miller", age=55),
            Person(first_name="Eve", last_name="Jackson", age=28),
            Person(first_name="Frank", last_name="Ocean", age=19),
            Person(first_name="Grace", last_name="Hopper", age=35),
            Person(first_name="Heidi", last_name="Klum", age=46),
            Person(first_name="Isaac", last_name="Newton", age=41),
            Person(first_name="Jack", last_name="Johnson", age=33),
        ]

        db_session.add_all(people)
        db_session.commit()

    finally:
        db_session.close()
        print(f"finally session active: {db_session.is_active}")


if __name__ == "__main__":
    main()
