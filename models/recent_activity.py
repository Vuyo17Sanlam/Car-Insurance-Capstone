import uuid
from datetime import datetime

from extensions import db


class RecentActivity(db.Model):
    __tablename__ = "recent_activity"

    id = db.Column(db.String(255), primary_key=True, default=lambda: str(uuid.uuid4()))
    activity = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "activity": self.activity,
            "created_at": self.created_at,
        }
