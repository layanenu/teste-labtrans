from peewee import CharField, DoubleField
from models.model import BaseModel


class Video(BaseModel):
    name = CharField()
    km_inicial = DoubleField()
    km_final = DoubleField()
