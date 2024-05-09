from databases.database import SessionLocal, engine, Base

from databases.models import Person


def main() -> None:
    Base.metadata.create_all(bind=engine)

    with SessionLocal() as db_session:
        print(f"try session active: {db_session.is_active}")

        for person in db_session.query(Person).all():
            print(person)

        natalie_fav_person = (
            db_session.query(Person).filter_by(first_name="Charlie").first()
        )

        print(natalie_fav_person)

    print(f"try session active: {db_session.is_active}")


if __name__ == "__main__":
    main()
