from sqlalchemy.orm import Session

from utils.Exceptions import BadRequest, NotFound
from ..database import engine


class ORM:
    @classmethod
    def list(_class) -> list:
        db_session = Session(engine)
        rows = db_session.query(_class).filter().all()
        rows_json = [row.to_dict() for row in rows]
        db_session.close()
        return rows_json

    @classmethod
    def insert(_class, data: dict) -> dict:
        db_session = Session(engine)
        obj = _class(**data)
        db_session.add(obj)
        try:
            db_session.commit()
            object_return = obj.to_dict()
            db_session.close()
            return object_return

        except Exception as e:
            db_session.rollback()
            db_session.close()
            if "Duplicate" in str(e):
                raise BadRequest("Duplicate Entry")
            if "a foreign key constraint fails" in str(e):
                raise NotFound("Foreign Key Row does not exist.")
            raise e

    @classmethod
    def delete(_class, id: int) -> bool:
        db_session = Session(engine)
        obj = db_session.query(_class).filter(_class.id == id)
        if obj.first() == None:
            raise NotFound("Row Not found")

        db_session.delete(obj.first())
        try:
            db_session.commit()
            db_session.close()
        except Exception as e:
            db_session.rollback()
            db_session.close()
            raise e

    @classmethod
    def get(_class, id: int) -> dict:
        db_session = Session(engine)
        row = db_session.query(_class).filter(_class.id == id).first()

        if row:
            db_session.close()
            return row.to_dict()
        else:
            db_session.close()
            raise NotFound("Row Not Found")
