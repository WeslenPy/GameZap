# def typeUser(user:UserMixin=current_user, default=None):
#     if default != None: default=default
#     else: default =  ["administrador", "suporte", "programador"]
#     def decoratorType(func):

#         @wraps(func)
#         def wrapper(*args,**kwargs):
#             if not validar_tipo(user, default):
#                 return redirect('/')
                
#             return func(*args,**kwargs)
#         return wrapper
        
#     return decoratorType
