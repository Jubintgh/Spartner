from app.models import db, Discipline

def seed_disciplines():

    disciplines = [
        Discipline(discipline_name='Southpaw'),
        Discipline(discipline_name='Kickboxing'),
        Discipline(discipline_name='Orthodox'),
        Discipline(discipline_name='Judo'),
        Discipline(discipline_name='Muay Thai'),
        Discipline(discipline_name='Grappling'),
        Discipline(discipline_name='Counter Striker'),
        Discipline(discipline_name='Karate'),
        Discipline(discipline_name='Switch'),
        Discipline(discipline_name='Brazilian Jiu-Jitsu')
        ]
        
    db.bulk_save_objects(disciplines)
    db.session.commit()

def undo_disciplines():
    db.session.execute('TRUNCATE disciplines RESTART IDENTITY CASCADE;')
    db.session.commit()
