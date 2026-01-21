from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# For development, we use SQLite (a file named 'mamacare.db').
# For production, we would swap this URL with PostgreSQL.
SQLALCHEMY_DATABASE_URL = "sqlite:///./mamacare.db"

# create_engine: Establishes the connection
# connect_args={"check_same_thread": False} is needed ONLY for SQLite
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# SessionLocal: The "factory" that creates database sessions for each request
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base: The class that all our Database Models will inherit from
Base = declarative_base()

# Dependency to get the DB session in endpoints
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()