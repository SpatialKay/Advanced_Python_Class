from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(
    "sqlite:///./demo.sqlite3",
    connect_args={"check_same_thread": False},
    echo=True,
)

SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
