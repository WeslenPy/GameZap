from app.utils.functions import decorators
from app.blueprints.adm import dash_admin
from app.database.models import *

@dash_admin.route("/login",methods=["GET"])
@decorators.renderTemplate
def dash_login():

    context = dict(template_name_or_list="index/login.html",
                )

    return context