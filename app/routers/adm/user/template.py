from app.utils.functions.pagination import page
from app.blueprints import dash_admin
from app.utils.functions import decorators
from app.database.models import *

@dash_admin.route("/user",methods=["GET"])
@decorators.renderTemplate
def dash_user():
    rows = page.returnPagination(User)
    context = dict(template_name_or_list="adm/user.html",
                   rows=rows,
                )

    return context