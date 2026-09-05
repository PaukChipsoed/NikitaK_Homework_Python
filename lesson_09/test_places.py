from datetime import datetime
from decimal import Decimal

from sqlalchemy import Column, DateTime, Integer, Numeric, String
from sqlalchemy import func, select
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Place(Base):
    __tablename__ = "places"

    place_id = Column(Integer, primary_key=True)
    place_name = Column(String)
    place_size = Column(Numeric)
    place_date_start = Column(DateTime)


def get_new_place_id(session):
    max_id = session.execute(
        select(func.max(Place.place_id))
    ).scalar()

    return (max_id or 0) + 1


def test_create_place(db_session):
    place_id = get_new_place_id(db_session)

    place = Place(
        place_id=place_id,
        place_name="Test Place",
        place_size=Decimal("100.50"),
        place_date_start=datetime(2026, 9, 5, 12, 0, 0),
    )

    try:
        db_session.add(place)
        db_session.commit()

        created_place = db_session.execute(
            select(Place).where(Place.place_id == place_id)
        ).scalar_one_or_none()

        assert created_place is not None
        assert created_place.place_name == "Test Place"
        assert created_place.place_size == Decimal("100.50")
    finally:
        created_place = db_session.execute(
            select(Place).where(Place.place_id == place_id)
        ).scalar_one_or_none()

        if created_place is not None:
            db_session.delete(created_place)
            db_session.commit()


def test_update_place(db_session):
    place_id = get_new_place_id(db_session)

    place = Place(
        place_id=place_id,
        place_name="Test Place",
        place_size=Decimal("100.50"),
        place_date_start=datetime(2026, 9, 5, 12, 0, 0),
    )

    try:
        db_session.add(place)
        db_session.commit()

        place.place_name = "Updated Place"
        place.place_size = Decimal("200.75")
        db_session.commit()

        updated_place = db_session.execute(
            select(Place).where(Place.place_id == place_id)
        ).scalar_one_or_none()

        assert updated_place is not None
        assert updated_place.place_name == "Updated Place"
        assert updated_place.place_size == Decimal("200.75")
    finally:
        created_place = db_session.execute(
            select(Place).where(Place.place_id == place_id)
        ).scalar_one_or_none()

        if created_place is not None:
            db_session.delete(created_place)
            db_session.commit()


def test_delete_place(db_session):
    place_id = get_new_place_id(db_session)

    place = Place(
        place_id=place_id,
        place_name="Test Place",
        place_size=Decimal("100.50"),
        place_date_start=datetime(2026, 9, 5, 12, 0, 0),
    )

    db_session.add(place)
    db_session.commit()

    try:
        db_session.delete(place)
        db_session.commit()

        deleted_place = db_session.execute(
            select(Place).where(Place.place_id == place_id)
        ).scalar_one_or_none()

        assert deleted_place is None
    finally:
        created_place = db_session.execute(
            select(Place).where(Place.place_id == place_id)
        ).scalar_one_or_none()

        if created_place is not None:
            db_session.delete(created_place)
            db_session.commit()
