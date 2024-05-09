from sqlalchemy import Column, Integer, String

from databases.database import Base


class Person(Base):
    __tablename__ = "people"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    age = Column(Integer)
