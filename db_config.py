import datetime
import os
from dotenv import load_dotenv
from peewee import Model, IntegerField, CharField, TimestampField
from playhouse.db_url import connect

load_dotenv(override=True)


db = connect(os.environ.get("DATABASE"))


# メッセージのモデル
class Message(Model):
    id = IntegerField(primary_key=True)
    name = CharField()
    age = IntegerField()
    pub_date = TimestampField(default=datetime.datetime.now())

    class Meta:
        database = db
        table_name = "messages"


db.create_tables([Message])
