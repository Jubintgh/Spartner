from app.models import db, Like

def seed_likes():
    like1 = Like(praiser_id=2,praised_id=1)
    like2 = Like(praiser_id=3,praised_id=1)
    like3 = Like(praiser_id=5,praised_id=1)
    like4 = Like(praiser_id=7,praised_id=1)
    like5 = Like(praiser_id=8,praised_id=1)
    like6 = Like(praiser_id=10,praised_id=1)
    like7 = Like(praiser_id=11,praised_id=1)
    like8 = Like(praiser_id=13,praised_id=1)
    like9 = Like(praiser_id=14,praised_id=1)
    like10 = Like(praiser_id=16,praised_id=1)
    like11 = Like(praiser_id=17,praised_id=1)
    like12 = Like(praiser_id=18,praised_id=1)
    like13 = Like(praiser_id=20,praised_id=1)
    like14 = Like(praiser_id=22,praised_id=1)
    like15 = Like(praiser_id=23,praised_id=1)
    like16 = Like(praiser_id=24,praised_id=1)
    like17 = Like(praiser_id=25,praised_id=1)
    like18 = Like(praiser_id=26,praised_id=1)
    like19 = Like(praiser_id=29,praised_id=1)
    like20 = Like(praiser_id=30,praised_id=1)

    db.session.add(like1)
    db.session.add(like2)
    db.session.add(like3)
    db.session.add(like4)
    db.session.add(like5)
    db.session.add(like6)
    db.session.add(like7)
    db.session.add(like8)
    db.session.add(like9)
    db.session.add(like10)
    db.session.add(like11)
    db.session.add(like12)
    db.session.add(like13)
    db.session.add(like14)
    db.session.add(like15)
    db.session.add(like16)
    db.session.add(like17)
    db.session.add(like18)
    db.session.add(like19)
    db.session.add(like20)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_likes():
    db.session.execute('TRUNCATE likes RESTART IDENTITY CASCADE;')
    db.session.commit()
