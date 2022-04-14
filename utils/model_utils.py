import uuid


def generate_id():
    return uuid.uuid4().hex[:10]


def generate_short_id():
    return uuid.uuid4().hex[:3]
