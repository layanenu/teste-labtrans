import peewee

db = peewee.SqliteDatabase('base.db')


class BaseModel(peewee.Model):
    class Meta:
        database = db
