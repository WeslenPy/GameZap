from datetime import datetime
from app import db

class Recharge(db.Model):
    __tablename__ = 'recharge'

    id  = db.Column(db.Integer, primary_key=True,autoincrement=True)

    txid = db.Column(db.String(256),unique=True,nullable=False)
    value= db.Column(db.Float(precision=2),nullable=False)

    status = db.Column(db.String(10),default="ACTIVE")

    expiration = db.Column(db.DateTime,default=datetime.now,nullable=False)
    created_at = db.Column(db.DateTime,default=datetime.now,nullable=False)
    
    user_id = db.Column(db.ForeignKey("user.id",ondelete='cascade'),nullable=False)
    user_ship= db.relationship('User',back_populates='recharge_children')

    def __init__(self,txid,value,expiration,user_id,status="ACTIVE",created_at=datetime.now):

        self.txid =txid
        self.value =value
        self.status =status
        self.user_id =user_id
        self.expiration =expiration
        self.created_at =created_at()
        
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