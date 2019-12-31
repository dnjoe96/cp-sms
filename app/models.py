from app import db
from datetime import datetime


class Outgoing(db.Model):
    __tablename__ = 'outgoing_messages'

    id = db.Column(db.Integer, primary_key=True)
    receiver = db.Column(db.String(140))
    body = db.Column(db.Text)
    time_sent = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __init__(self, receiver, body):
        self.receiver = receiver
        self.body = body

    def __repr__(self):
        return '<post {}>'.format(self.body)
