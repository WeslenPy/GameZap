from flask import Blueprint

dash_admin = Blueprint('dashboard', __name__, url_prefix='/admin/dashboard'
                                    ,template_folder="templates/adm")


api_admin_v1 = Blueprint('admin_api_v1', __name__, url_prefix='/api/v1/admin'
                                    ,template_folder="templates/adm")