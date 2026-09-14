import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URL = (
    "postgresql://postgres:12345678@localhost:5432/QA"
)

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)


@pytest.fixture
def db_session():
    session = Session()
    yield session
    session.close()
