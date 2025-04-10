import uuid

from extensions import db
from sqlalchemy import Column


class Payment(db.Model):
    __tablename__ = "payment_details"
    payment_details_id = db.Column(
        db.String(255), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    user_id = db.Column(db.String(255), db.ForeignKey("users.user_id"), nullable=False)
    monthly_payment_day = db.Column(db.Integer, nullable=False)

    card_number = db.Column(db.String(4), nullable=False)

    def to_dict(self):
        return {
            "payment_details_id": self.payment_details_id,
            "user_id": self.user_id,
            "monthly_payment_day": self.monthly_payment_day,
            "card_number": self.card_number,
        }
