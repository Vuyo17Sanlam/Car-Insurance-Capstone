import uuid

from extensions import db


class User(db.Model):
    __tablename__ = "clients"
    id = db.Column(db.String(255), primary_key=True, default=lambda: str(uuid.uuid4()))
    username = db.Column(db.String(100))
    password = db.Column(db.String(255))

    # Object -> Dict
    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password,
        }
