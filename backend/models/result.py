from peewee import IntegerField, DoubleField
from models.model import BaseModel


class Result(BaseModel):
    highway = IntegerField()
    km = DoubleField()
    buraco = IntegerField()
    remendo = IntegerField()
    trinca = IntegerField()
    placa = IntegerField()
    drenagem = IntegerField()
