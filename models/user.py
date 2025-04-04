import uuid

from flask_login import UserMixin

from extensions import db


class User(UserMixin, db.Model):
    __tablename__ = "users"
    user_id = db.Column(
        db.String(255), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    user_name = db.Column(db.String(100))
    title = db.Column(db.String(10))
    password_hash = db.Column(db.String(400))
    surname = db.Column(db.String(100))
    id_number = db.Column(db.String(100))
    dob = db.Column(db.Date)
    gender = db.Column(db.String(10))
    phone_no = db.Column(db.String(30))
    email = db.Column(db.String(100))
    address = db.Column(db.String(255))

    def get_id(self):
        return str(self.user_id)

    # Object -> Dict
    def to_dict(self):
        return {
            "user_id": self.user_id,
            "title": self.title,
            "user_name": self.user_name,
            "password_hash": self.password_hash,
            "surname": self.surname,
            "id_number": self.id_number,
            "dob": self.dob,
            "gender": self.gender,
            "phone_no": self.phone_no,
            "email": self.email,
            "address": self.address,
        }
