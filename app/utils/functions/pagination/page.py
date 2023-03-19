from app import PER_PAGE
from flask import request


def returnPagination(model,filters=[]):

    page = request.args.get('page',1,type=int)

    rows = model.query.filter(*filters).order_by(model.id.desc()).paginate(page,PER_PAGE,error_out=False)

    return rows