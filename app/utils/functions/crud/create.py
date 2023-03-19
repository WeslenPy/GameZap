from flask import jsonify,request

def createRow(model,schema,data:dict=False):
    if data==False:data = request.get_json(force=True,silent=True)

    if data is None:return jsonify({"title":'Dados inválidos!', "icon":'error',"timer":2500})

    erros = schema().validate(data)
    if erros:return jsonify({"title":'Dados inválidos!', "icon":'error',"timer":2500})
    
    find = model.query.filter_by(**data).first()
    if not find:
        new = schema().load(data)
        new.save()
        
        return jsonify({"title":'Cadastro efetuado com sucesso!', "icon":'success',"timer":2500})

    return jsonify({"title":'Dados duplicados!',"text":"Já existe um item com esses mesmos dados.", 
                            "icon":'info',"timer":2500})