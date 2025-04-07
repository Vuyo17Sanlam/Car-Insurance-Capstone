import uuid

from extensions import db
from flask_login import UserMixin
from sqlalchemy import ForeignKey


class Vehicles(db.Model):
    __tablename__ = "vehicles"
    vehicle_id = db.Column(
        db.String(255), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    user_id = db.Column(db.String(255), db.ForeignKey("users.user_id"))
    make = db.Column(db.String(100))
    model = db.Column(db.String(100))
    year = db.Column(db.Integer)
    license_plate = db.Column(db.String(20))
    vin = db.Column(db.String(17))
    current_mileage = db.Column(db.Integer)
    estimated_current_value = db.Column(db.Numeric(10, 2))
    purchase_date = db.Column(db.Date)

    def get_id(self):
        return str(self.user_id)

    # Object -> Dict
    def to_dict(self):
        return {
            "vehicle_id": self.vehicle_id,
            "user_id": self.user_id,
            "make": self.make,
            "model": self.model,
            "year": self.year,
            "license_plate": self.license_plate,
            "vin": self.vin,
            "current_mileage": self.current_mileage,
            "estimated_current_value": self.estimated_current_value,
            "purchase_date": self.purchase_date,
        }
