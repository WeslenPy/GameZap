from app.blueprints import dash_admin
from app.utils.functions import decorators
from app.database.models import *

@dash_admin.route("/configuration",methods=["GET"])
@decorators.renderTemplate
def dash_config():

    context = dict(template_name_or_list="adm/home.html",
                )

    return context