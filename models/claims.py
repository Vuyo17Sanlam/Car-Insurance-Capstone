import uuid

from extensions import db


class Claim(db.Model):
    __tablename__ = "claims"
    id = db.Column(
        db.String(50), primary_key=True, default=lambda: str(uuid.uuid4())
    )  # uuid will generate random id for us | random ids to protect people from attacking our data
    # safeguards data and migration is easier
    name = db.Column(db.String(100))
    dte = db.Column(db.Date)
    cause = db.Column(db.String(100))
    amount = db.Column(db.Float)
    status = db.Column(db.String(100))

    # Object -> Dict
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "dte": self.dte,
            "cause": self.cause,
            "amount": self.amount,
            "status": self.status,
        }
