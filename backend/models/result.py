from peewee import IntegerField, DoubleField, TextField
from models.model import BaseModel


class Result(BaseModel):
    name = TextField()
    km = DoubleField()
    distance = DoubleField()
    highway = IntegerField()
    item = TextField()

    class Meta:
        db_table = 'results'
