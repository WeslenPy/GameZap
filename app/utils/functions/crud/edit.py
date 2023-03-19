from flask import jsonify,request

def editRow(model,schema,data:dict=False):
    if data==False:data = request.get_json(force=True,silent=True)
    
    if data is None:return jsonify({"title":'Dados inválidos!', "icon":'info',"timer":2500})

    find = model.query.get(data.get('id',''))
    if find:
        _schema = schema()
        erros = _schema.validate(data)
        if erros: return jsonify({"title":'Oops, algo deu errado!', "icon":'error',"timer":2500})

        _result = _schema.dump(data)
        find.update(_result)

        return jsonify({"title":'Dados atualizados com sucesso!', "icon":'success',"timer":2500})
    
    return jsonify({"title":'Não encontrado(a)!', "icon":'error',"timer":2500})