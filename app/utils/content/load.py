from .menu import menu

def load_menu(name:str)->dict:

    new:dict = menu.copy()

    title:str= new['title'].format(name=name)
    new['title'] = title

    return new  
