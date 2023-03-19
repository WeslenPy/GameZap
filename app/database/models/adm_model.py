from datetime import datetime
from app import db
from app.utils.functions.crypt import encryptPassword


class AdminPainel(db.Model):
    __tablename__ = 'admin'
    id  = db.Column(db.Integer, primary_key=True,autoincrement=True)
    email= db.Column(db.String(100),unique=True)
    password = db.Column(db.String(255),nullable=False)
    
    def __init__(self,email:str,password:str,created_at=datetime.now):

        self.email = email.strip().lower()
        self.created_at = created_at()
        self.password = encryptPassword(password.strip())
        
    def save(self):
        db.session.add(self)
        db.session.commit()
 
    def update(self,data:dict):
        for key, value in data.items():
            if key == 'id':continue
            if getattr(self,key,'not_found') != 'not_found':
                setattr(self, key, value)

        db.session.commit()
        return self