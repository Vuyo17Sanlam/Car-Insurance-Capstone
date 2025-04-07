import uuid

from extensions import db


class Policy(db.Model):
    __tablename__ = "policies"

    policy_id = db.Column(
        db.String(255), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    user_id = db.Column(db.String(255), db.ForeignKey("users.user_id"), nullable=False)
    vehicle_id = db.Column(
        db.String(255), db.ForeignKey("vehicles.vehicle_id"), nullable=False
    )
    policy_number = db.Column(db.String(50), unique=True, nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    premium = db.Column(db.Numeric(10, 2), nullable=False)
    monthly_payment_day = db.Column(db.Integer, nullable=False)
    coverage_type = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            "policy_id": self.policy_id,
            "user_id": self.user_id,
            "vehicle_id": self.vehicle_id,
            "policy_number": self.policy_number,
            "start_date": self.start_date.strftime("%Y-%m-%d")
            if self.start_date
            else None,
            "premium": float(self.premium),
            "monthly_payment_day": self.monthly_payment_day,
            "coverage_type": self.coverage_type,
        }
