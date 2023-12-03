import databases
import ormar
import sqlalchemy
import datetime

from .config import settings

database = databases.Database(settings.db_url)
metadata = sqlalchemy.MetaData()


class BaseMeta(ormar.ModelMeta):
    metadata = metadata
    database = database


class Operation(ormar.Model):
    class Meta(BaseMeta):
        tablename = "operation"

    id: int = ormar.Integer(primary_key=True)
    expression: str = ormar.String(max_length=128, nullable=False)
    result: float = ormar.Float()
    timestamp: datetime.datetime = ormar.DateTime(
        pydantic_only=True, default=datetime.datetime.now
    )


engine = sqlalchemy.create_engine(settings.db_url)
metadata.create_all(engine)