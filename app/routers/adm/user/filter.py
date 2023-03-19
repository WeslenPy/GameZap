from app.database.schema import UserSchema
from app import app


@app.template_filter()
def dump_user(data):
    return UserSchema().dumps(data)