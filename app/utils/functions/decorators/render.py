from flask import render_template
from functools import wraps


def renderTemplate(target):
    @wraps(target)
    def wrapper(*args, **kwargs):

        context:dict = target(*args, **kwargs)

        return render_template(**context)
    return wrapper

