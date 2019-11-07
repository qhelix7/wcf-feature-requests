from datetime import datetime

from feature_server import db


class Client(db.Model):
    __tablename__ = "client"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)


class FeatureRequest(db.Model):
    __tablename__ = "feature_request"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    client_id = db.Column(
        db.Integer,
        db.ForeignKey("client.id"),
        nullable=False,
    )
    client = db.relationship(
        'Client',
        backref=db.backref("feature_requests"),
        lazy=True,
    )
    priority = db.Column(
        db.Enum(
            "Undetermined",
            "Critical",
            "High",
            "Medium",
            "Low",
            name="priority_enum"
        ),
        nullable=False,
    )
    target_date = db.Column(db.DateTime(timezone=True), nullable=False)
    created_at = db.Column(
        db.DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False,
    )

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "client": self.client.name,
            "priority": self.priority,
            "target_date": self.target_date.isoformat()[:10],
            "created_at": self.created_at.isoformat()[:10],
        }
