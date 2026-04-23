from app import app
from extensions import db
from models import User, Note
from faker import Faker

fake = Faker()

with app.app_context():
    db.drop_all()
    db.create_all()

    for _ in range(5):
        user = User(username=fake.user_name())
        user.set_password("password")

        db.session.add(user)
        db.session.commit()

        for _ in range(3):
            note = Note(
                title=fake.sentence(),
                content=fake.text(),
                user_id=user.id
            )
            db.session.add(note)

    db.session.commit()
    print("Database seeded!")