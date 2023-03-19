

from app.database.models import Recharge
from app import ma

class RechargeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:

        unknown = "exclude"
        model = Recharge
        
        load_instance = True
        include_fk=True
        ordered = True

        dump_only = ("id",)