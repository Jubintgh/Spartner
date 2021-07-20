from app.models import User, db


# Adds a demo user, you can add other users here if you want
def seed_users():
    # demo = User(
    #     username='Demo', email='demo@aa.io', password='password')
    # marnie = User(
    #     username='marnie', email='marnie@aa.io', password='password')
    # bobbie = User(
    #     username='bobbie', email='bobbie@aa.io', password='password')

    # db.session.add(demo)
    # db.session.add(marnie)
    # db.session.add(bobbie)

    users = [
        User(
            first_name='Demo', last_name='User', username='demouser',
            email='demouser@mail.com', password='Password1!', age=20,
            location='Las Vegas, NV', gender=1, coach=False,
            discipline='Southpaw'
        ),
        User(
            first_name='That Guy', last_name='Pal', username='pantmcdonalds',
            email='pgottsch@hotmail.com', password='Password1!', age=57,
            location="Phoenix, AZ", gender=1, coach=True,
            discipline='Judo'
        ),
        User(
            first_name='Tai', last_name='Tuivasa', username='shoeie',
            email='qrczak@live.com', password='Password1!', age=28,
            location="Sydney, NSW,  AU", gender=1, coach=False
        ),
        User(
            first_name='Ronda', last_name='Rousey', username='showtrunks',
            email='andale@me.com', password='Password1!', age=34,
            location="Riverside, CA", gender=0, coach=True,
            discipline='Muay Thai'
        ),
        User(
            first_name='Amanda', last_name='Nunes', username='skunkbarmpot',
            email='joehall@yahoo.com', password='Password1!', age=33,
            location="Pojuca, BR", gender=0, coach=False,
            discipline='Judo'
        ),
        User(
            first_name='Israel', last_name='Adesanya', username='stomachvindicator',
            email='michiel@att.net', password='Password1!', age=31,
            location="Auckland, NZ", gender=1, coach=False,
            discipline='Muay Thai'
        ),
        User(
            first_name='Nate', last_name='Diaz', username='irritatingsoon',
            email='thowell@sbcglobal.net', password='Password1!', age=36,
            location="Stockton, CA", gender=1, coach=False,
            discipline='Muay Thai'
        ),
        User(
            first_name='Dana', last_name='White', username='skiertortilla',
            email='grossman@live.com', password='Password1!', age=51,
            location="Las Vegas, NV", gender=1, coach=True,
            discipline='Orthodox'
        ),
        User(
            first_name='Martin', last_name='Vettori', username='baleeland',
            email='moinefou@me.com', password='Password1!', age=27,
            location="Mezzocorona, Italy", gender=1, coach=False,
            discipline='Orthodox'
        ),
        User(
            first_name='Mario', last_name='Nintendo', username='jordanianswimming',
            email='paley@yahoo.com', password='Password1!', age=40,
            location="Tokyo, Japan", gender=1, coach=True,
            discipline='Orthodox'
        ),
        User(
            first_name='Bowser', last_name='Nintendo', username='starbolinslatter',
            email='airship@icloud.com', password='Password1!', age=40,
            location="Tokyo, Japan", gender=2, coach=False,
            discipline='Southpaw'
        ),
        User(
            first_name='Peach', last_name='Nintendo', username='rustymeddlesome',
            email='paulv@att.net', password='Password1!', age=40,
            location="Tokyo, Japan", gender=0, coach=False,
            discipline='Orthodox'
        ),
        User(
            first_name='Valentina', last_name='Shevchenko', username='loomcostly',
            email='unreal@mac.com', password='Password1!', age=33,
            location="Bishkek, Kyrgyzstan", gender=0, coach=False,
            discipline='Kickboxing'
        ),
        User(
            first_name='Rose', last_name='Namajunas', username='abcbrood',
            email='turner.joe@zulauf.com', password='Password1!', age=29,
            location="Milwaukee, WI", gender=0, coach=False,
            discipline='Southpaw'
        ),
        User(
            first_name='Marion', last_name='Renau', username='fennelsymptom',
            email='frank.borer@gerhold.info', password='Password1!', age=44,
            location="Tulare, CA", gender=0, coach=False,
            discipline='Grappling'
        ),
        User(
            first_name='Miesha', last_name='Tate', username='chilliclang',
            email='reta66@yahoo.com', password='Password1!', age=34,
            location="Tacoma, WA", gender=0, coach=False,
            discipline='Southpaw'
        ),
        User(
            first_name='Raquel', last_name='Pennington', username='onionsexpert',
            email='vreichert@howell.net', password='Password1!', age=32,
            location="Colorado Springs, CO", gender=0, coach=True,
            discipline='Kickboxing'
        ),
        User(
            first_name='Holly', last_name='Holm', username='chimpanzeegreens',
            email='vfeeney@oreilly.com', password='Password1!', age=39,
            location="Albuquerque, NM", gender=0, coach=False,
            discipline='Muay Thai'
        ),
        User(
            first_name='Meagan', last_name='Anderson', username='nigeriansouthern',
            email='kenneth.tremblay@gislason.org', password='Password1!', age=31,
            location="Gold Coast, Australia", gender=0, coach=True,
            discipline='Kickboxing'
        ),
        User(
            first_name='Yoshi', last_name='Nintendo', username='plentyloutish',
            email='waelchi.lowell@lebsack.com', password='Password1!', age=50,
            location="Tokyo, Japan", gender=2, coach=True,
            discipline='Brazilian Jiu-Jitsu'
        ),
        User(
            first_name='Connor', last_name='McGregor', username='waship',
            email='catyunclescrooge@yahoo.com', password='Password1!', age=33,
            location="Dublin, Ireland", gender=1, coach=False,
            discipline='Counter Striker'
        ),
        User(
            first_name='Dustin', last_name='Poirier', username='jollymagenta',
            email='robbyclever@yahoo.com', password='Password1!', age=32,
            location="Coconut Creek, FL", gender=1, coach=False,
            discipline='Grappling'
        ),
        User(
            first_name='Kevin', last_name='Holland', username='squarelutz',
            email='marcbrooding@gmail.com', password='Password1!', age=28,
            location="Riverside, CA", gender=1, coach=False,
            discipline='Brazilian Jiu-Jitsu'
        ),
        User(
            first_name='Karl', last_name='Roberson', username='assetincomplete',
            email='zandercuddly@yahoo.com', password='Password1!', age=30,
            location="Neptune, NJ", gender=1, coach=False,
            discipline='Southpaw'
        ),
        User(
            first_name='Robert', last_name='Whittaker', username='beginningscuba',
            email='confusedsu@optonline.net', password='Password1!', age=30,
            location="Auckland, NZ", gender=1, coach=True,
            discipline='Brazilian Jiu-Jitsu'
        ),
        User(
            first_name='Derek', last_name='Brunson', username='purringlonghorn',
            email='wearysawney@me.com', password='Password1!', age=37,
            location="Wilmington, NC", gender=1, coach=False,
            discipline='Switch'
        ),
        User(
            first_name='Paulo', last_name='Costa', username='trebleflyingfish',
            email='jealousreggie@aol.com', password='Password1!', age=30,
            location="Belo Horizonte, Brazil", gender=1, coach=False,
            discipline='Southpaw'
        ),
        User(
            first_name='Godzilla', last_name='Kaiju', username='culturaldrafter',
            email='optimisticaly@msn.com', password='Password1!', age=1000,
            location="Tokyo, Japan", gender=2, coach=True,
            discipline='Counter Striker'
        ),
        User(
            first_name='Zhang', last_name='Weili', username='easilyundies',
            email='indexwretched@yahoo.com', password='Password1!', age=31,
            location="Bejing, China", gender=0, coach=True,
            discipline='Kickboxing'
        ),
        User(
            first_name='Walter', last_name='White', username='blue',
            email='wwhite@yahoo.com', password='Password1!', age=52,
            location="Albuquerque, NM", gender=1, coach=True,
            discipline='Switch'
        ),
    ]
    db.bulk_save_objects(users)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_users():
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
    db.session.commit()
