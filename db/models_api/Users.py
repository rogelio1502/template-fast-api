from datetime import datetime
import enum
import pytz
from sqlalchemy import Column, Enum, Integer, String, DATETIME
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import Session

from utils.Exceptions import NotFound

from ..database import Base, engine
from .ORM import ORM


class RolesEnum(enum.Enum):

    father = "father"
    admin = "admin"


class Users(Base, ORM, SerializerMixin):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(220), nullable=False)
    role = Column(Enum(RolesEnum), nullable=False)
    created = Column(
        DATETIME, default=datetime.now(tz=pytz.timezone("America/Monterrey"))
    )
    updated = Column(
        DATETIME, default=datetime.now(tz=pytz.timezone("America/Monterrey"))
    )

    @staticmethod
    def update(id: int, data: dict) -> dict:

        pass

    @staticmethod
    def get_user_by_email(email: str) -> dict:
        db_session = Session(engine)
        row = db_session.query(Users).filter(Users.email == email).first()
        db_session.close()

        if row:
            return row.to_dict()
        raise NotFound("User not found")

    def get_role(email: str) -> str:
        user = Users.get_user_by_email(email)
        return user.get("role")
