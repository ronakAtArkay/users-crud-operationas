from uuid import uuid4
import datetime

def generate_id():
    id = str(uuid4())
    return id


def date():
    dt = datetime.datetime.now()
    return dt