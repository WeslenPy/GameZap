
import bcrypt

def encryptPassword(password:str)->str:
    return bcrypt.hashpw(str.encode(password.strip()),
                            bcrypt.gensalt())


def decryptPassword(password:str,hashed_password:str)->bool:
    return bcrypt.checkpw(str.encode(password),str.encode(hashed_password))