from peewee import CharField, DoubleField
from models.model import BaseModel


class Rodovia(BaseModel):
    highway = CharField()
    km_inicial = DoubleField()
    km_final = DoubleField()
