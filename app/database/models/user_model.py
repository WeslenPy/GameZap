from datetime import datetime
from app import db
class User(db.Model):
    __tablename__ = 'user'

    id  = db.Column(db.Integer, primary_key=True,autoincrement=True)

    chat_id = db.Column(db.String(200),unique=True,nullable=False)
    device = db.Column(db.String(200),nullable=False)

    username = db.Column(db.String(256))

    full_name =  db.Column(db.String(256))
    
    balance = db.Column(db.Float(precision=2),nullable=False,default=0)

    cpf = db.Column(db.String(12),unique=True,default=None,nullable=True)

    active = db.Column(db.Boolean,default=True,nullable=False)
    full_profile = db.Column(db.Boolean,default=False,nullable=False)
    banned = db.Column(db.Boolean,default=False,nullable=False)

    created_at = db.Column(db.DateTime,default=datetime.now,nullable=False)

    recharge_children = db.relationship(
        "Recharge", back_populates="user_ship",
        cascade="all, delete",passive_deletes=True)
    
    def __init__(self,chat_id,device,username,full_name,active=True,full_profile=False,
                            banned=False,balance=0,cpf=None,created_at=datetime.now):
        
        self.chat_id = chat_id
        self.device = device
        self.username = username
        self.full_name = full_name
        self.balance = balance
        self.banned = banned
        self.full_profile = full_profile
        self.full_profile = full_profile
        self.active = active
        self.cpf = cpf
        self.created_at = created_at()

        
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