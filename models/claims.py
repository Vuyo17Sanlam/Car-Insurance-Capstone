import uuid

from extensions import db


class Claim(db.Model):
    __tablename__ = "claims"

    claim_id = db.Column(
        db.String(255), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    policy_id = db.Column(
        db.String(255), db.ForeignKey("policies.policy_id"), nullable=False
    )
    user_id = db.Column(db.String(255), db.ForeignKey("users.user_id"), nullable=False)
    incident = db.Column(db.String(50), nullable=False)
    incident_date = db.Column(db.Date, nullable=False)
    claim_amount = db.Column(db.Numeric(10, 2), default=1000)
    claim_status = db.Column(db.String(40), default="Pending")
    description = db.Column(db.Text)
    claim_duration = db.Column(
        db.String(255), default="Not Available"
    )  # Default value for claim_duration

    def to_dict(self):
        return {
            "claim_id": self.claim_id,
            "policy_id": self.policy_id,
            "user_id": self.user_id,
            "incident": self.incident,
            "incident_date": self.incident_date.strftime("%Y-%m-%d")
            if self.incident_date
            else None,
            "claim_amount": float(self.claim_amount) if self.claim_amount else None,
            "claim_status": self.claim_status,
            "description": self.description,
            "claim_duration": self.claim_duration,
        }
