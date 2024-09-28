import datetime
from peewee import *

from bot.constants import DATABASE_PATH, DATABASE_PRAGMAS, AccessLevel

dbhandle = SqliteDatabase(DATABASE_PATH, pragmas=DATABASE_PRAGMAS)


class BaseModel(Model):
    class Meta:
        database = dbhandle


class User(BaseModel):
    id = IntegerField(primary_key=True)
    username = CharField(unique=True)
    language_code = CharField(max_length=5)
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    access_level = IntegerField()
    url = CharField(max_length=255)
    created_at = DateTimeField(default=datetime.datetime.now)

    def flatten_access_level(self):
        self.access_level = min(max(self.access_level, 1), max(AccessLevel).value)
        self.save()

    def full_name(self):
        if self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.first_name


User.create_table()
