from peewee import IntegerField, DoubleField
from models.model import BaseModel


class VwResult(BaseModel):
    highway = IntegerField()
    km = DoubleField()
    buraco = IntegerField()
    remendo = IntegerField()
    trinca = IntegerField()
    placa = IntegerField()
    drenagem = IntegerField()

    class Meta:
        db_table = 'vw_results'
