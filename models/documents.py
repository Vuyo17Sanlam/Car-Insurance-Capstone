import uuid

from extensions import db


class Document(db.Model):
    __tablename__ = "documents"

    document_id = db.Column(
        db.String(255), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    claim_id = db.Column(
        db.String(255), db.ForeignKey("claims.claim_id"), nullable=False
    )
    images = db.Column(db.Text, nullable=False)
    affidavit = db.Column(db.String(255), nullable=False)
    police_report = db.Column(db.String(255), nullable=False)

    def to_dict(self):
        return {
            "document_id": self.document_id,
            "claim_id": self.claim_id,
            "images": self.images,
            "affidavit": self.affidavit,
            "police_report": self.police_report,
        }
