from flask import render_template
from app import app

@app.errorhandler(404) 
@app.errorhandler(500) 
def error_page(error):
    return render_template('erros/abort404.html'),404
