from app import db
from flask import jsonify

def deleteRow(model,_id):
    
    if _id:
        method = model.query.get(_id)
        if method:
            db.session.delete(method)
            db.session.commit()

            return jsonify({"title":'Deletado com sucesso!', "icon":'success',"timer":2500})
        
        return jsonify({"title":'Não encontrado!', "icon":'error',"timer":2500})

    return jsonify({"title":'Dados inválidos!', "icon":'info',"timer":2500})