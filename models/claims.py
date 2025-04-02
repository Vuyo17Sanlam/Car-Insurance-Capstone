import uuid

from extensions import db


class Claim(db.Model):
    __tablename__ = "car_claims"
    id = db.Column(db.String(100), primary_key=True)
    name = db.Column(db.String(100))
    incident = db.Column(db.String(100))
    date = db.Column(db.String(100))
    amount = db.Column(db.String(100))
    status = db.Column(db.String(100))

    # Object -> Dict
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "incident": self.incident,
            "date": self.date,
            "amount": self.amount,
            "status": self.status,
        }
