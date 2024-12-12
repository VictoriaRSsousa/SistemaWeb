from ..database import db

class Accounts(db.Model):
    __tablename__ = 'accounts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cnpj = db.Column(db.String(14), db.ForeignKey('creditors.cnpj'), nullable=False)
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    penalty = db.Column(db.Numeric(10, 2), nullable=False)
    payment_date = db.Column(db.Date)
    interest = db.Column(db.Numeric(10, 2), nullable=False)
    status = db.Column(db.String(20), nullable=False)

    creditor = db.relationship('Creditors', backref='accounts')
