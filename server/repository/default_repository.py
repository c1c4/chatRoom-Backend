from sqlalchemy.exc import IntegrityError

from server import db
from server.configuration.exceptions import DataFail


def save(model: db.Model, is_insert=False):
    try:
        if is_insert:
            db.session.add(model)

        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        raise DataFail(f"{model.__class__.__name__} already in our base with this identify")
