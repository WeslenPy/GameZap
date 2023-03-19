

from app.database.models import User
from app import ma

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:

        unknown = "exclude"
        model = User
        
        load_instance = True
        include_fk=True
        ordered = True

        dump_only = ("id","balance")