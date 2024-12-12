from ..database import db


class Creditors(db.Model):
    __tablename__ = 'creditors'
    cnpj = db.Column(db.String(14), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(20))
    email = db.Column(db.String(100))
