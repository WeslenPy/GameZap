from .menu import menu

def load_menu(name:str)->dict:

    new:dict = menu.copy()

    title:str= new['title'].format(name=name)
    new['title'] = title

    return new  


def load_button(key:str,button:dict,**kwargs)->dict:

    new:dict = button.copy()

    mod:str= new[key].format(**kwargs)
    new[key] = mod

    return new  

