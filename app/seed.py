from app import create_app
from app.models import db, Guest, Episode, Appearance

app = create_app()

with app.app_context():
    # Drop all tables first (optional, good for dev)
    db.drop_all()
    db.create_all()

    # Create Guests
    guest1 = Guest(name="Trevor Noah", occupation="Comedian")
    guest2 = Guest(name="Lupita Nyong'o", occupation="Actress")
    guest3 = Guest(name="Ali Kiba", occupation="Musician")

    # Create Episodes (using date and number, not title!)
    episode1 = Episode(date="1/11/99", number=1)
    episode2 = Episode(date="1/12/99", number=2)
    episode3 = Episode(date="1/13/99", number=3)

    # Add to session so we can access their IDs
    db.session.add_all([guest1, guest2, guest3, episode1, episode2, episode3])
    db.session.flush()

    # Create Appearances
    appearance1 = Appearance(guest_id=guest1.id, episode_id=episode1.id, rating=4)
    appearance2 = Appearance(guest_id=guest2.id, episode_id=episode3.id, rating=5)
    appearance3 = Appearance(guest_id=guest3.id, episode_id=episode2.id, rating=3)
    appearance4 = Appearance(guest_id=guest1.id, episode_id=episode3.id, rating=4)

    db.session.add_all([appearance1, appearance2, appearance3, appearance4])
    db.session.commit()

    print("✅ Database seeded successfully!")
