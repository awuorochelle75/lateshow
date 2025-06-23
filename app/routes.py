from flask import Blueprint, request, jsonify
from .models import db, Guest, Episode, Appearance

routes = Blueprint("routes", __name__)

@routes.route("/episodes", methods=["GET"])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([{
        "id": ep.id,
        "date": ep.date,
        "number": ep.number
    } for ep in episodes]), 200

@routes.route("/episodes/<int:id>", methods=["GET"])
def get_episode_by_id(id):
    ep = Episode.query.get(id)
    if not ep:
        return jsonify({"error": "Episode not found"}), 404

    return jsonify({
        "id": ep.id,
        "date": ep.date,
        "number": ep.number,
        "appearances": [{
            "id": ap.id,
            "rating": ap.rating,
            "guest_id": ap.guest_id,
            "episode_id": ap.episode_id,
            "guest": {
                "id": ap.guest.id,
                "name": ap.guest.name,
                "occupation": ap.guest.occupation
            }
        } for ap in ep.appearances]
    }), 200

@routes.route("/guests", methods=["GET"])
def get_guests():
    guests = Guest.query.all()
    return jsonify([{
        "id": g.id,
        "name": g.name,
        "occupation": g.occupation
    } for g in guests]), 200

@routes.route("/appearances", methods=["POST"])
def create_appearance():
    data = request.get_json()
    try:
        appearance = Appearance(
            rating=data["rating"],
            guest_id=data["guest_id"],
            episode_id=data["episode_id"]
        )
        db.session.add(appearance)
        db.session.commit()

        return jsonify({
            "id": appearance.id,
            "rating": appearance.rating,
            "guest_id": appearance.guest_id,
            "episode_id": appearance.episode_id,
            "episode": {
                "id": appearance.episode.id,
                "date": appearance.episode.date,
                "number": appearance.episode.number
            },
            "guest": {
                "id": appearance.guest.id,
                "name": appearance.guest.name,
                "occupation": appearance.guest.occupation
            }
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"errors": [str(e)]}), 400

@routes.route("/guests/<int:id>", methods=["DELETE"])
def delete_guest(id):
    guest = Guest.query.get(id)
    if not guest:
        return jsonify({"error": "Guest not found"}), 404

    db.session.delete(guest)
    db.session.commit()
    return jsonify({"message": "Guest deleted successfully"}), 200
