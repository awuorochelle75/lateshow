from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()

class Guest(db.Model):
    __tablename__ = 'guests'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    occupation = db.Column(db.String, nullable=False)

    appearances = db.relationship('Appearance', backref='guest', cascade='all, delete-orphan')

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "occupation": self.occupation
        }

class Episode(db.Model):
    __tablename__ = 'episodes'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String, nullable=False)
    number = db.Column(db.Integer, nullable=False)

    appearances = db.relationship('Appearance', backref='episode', cascade='all, delete-orphan')

    def to_dict(self):
        return {
            "id": self.id,
            "date": self.date,
            "number": self.number
        }

    def to_dict_with_appearances(self):
        return {
            "id": self.id,
            "date": self.date,
            "number": self.number,
            "appearances": [
                appearance.to_dict(include_episode=False)
                for appearance in self.appearances
            ]
        }

class Appearance(db.Model):
    __tablename__ = 'appearances'

    id = db.Column(db.Integer, primary_key=True)
    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id'), nullable=False)
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    @validates('rating')
    def validate_rating(self, key, value):
        if not (1 <= value <= 5):
            raise ValueError('Rating must be between 1 and 5')
        return value

    def to_dict(self, include_guest=True, include_episode=True):
        data = {
            "id": self.id,
            "rating": self.rating,
            "guest_id": self.guest_id,
            "episode_id": self.episode_id,
        }

        if include_guest:
            data["guest"] = self.guest.to_dict()
        if include_episode:
            data["episode"] = self.episode.to_dict()

        return data
