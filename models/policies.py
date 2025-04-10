import uuid
from datetime import datetime

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
    start_date = db.Column(db.Date, default=datetime.now())
    premium = db.Column(db.Numeric(10, 2), nullable=False)

    coverage_type = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            "policy_id": self.policy_id,
            "user_id": self.user_id,
            "vehicle_id": self.vehicle_id,
            "start_date": self.start_date.strftime("%Y-%m-%d"),
            "premium": float(self.premium),
            "coverage_type": self.coverage_type,
        }
