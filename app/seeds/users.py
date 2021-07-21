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


    user1 = User(
            first_name='Demo', last_name='User', username='demouser',
            email='demouser@mail.com', password='Password1!', age=20,
            location='Las Vegas, NV', gender=1, coach=False,
            discipline=0, img_url="https://i.pinimg.com/originals/b7/ab/b6/b7abb604d6b6cfa8f4b8c3699842bea7.jpg"
        )

    user2 = User(
            first_name='That Guy', last_name='Pal', username='pantmcdonalds',
            email='pgottsch@hotmail.com', password='Password1!', age=57,
            location="Phoenix, AZ", gender=1, coach=True,
            discipline=3, img_url="https://i.imgur.com/9ceiiDO.jpeg"
        )

    user3 = User(
            first_name='Tai', last_name='Tuivasa', username='shoeie',
            email='qrczak@live.com', password='Password1!', age=28,
            location="Sydney, NSW,  AU", gender=1, coach=False,
            discipline=3, img_url="https://content.api.news/v3/images/bin/49706e13a487b1307f23b62cece560da"
        )

    user4 = User(
            first_name='Ronda', last_name='Rousey', username='showtrunks',
            email='andale@me.com', password='Password1!', age=34,
            location="Riverside, CA", gender=0, coach=True,
            discipline=4, img_url="https://media.lasvegasweekly.com/img/photos/2013/07/17/1307_LasVegasWeekly_RhondaRousey_cover_068_example_effects_applied_t1000.jpg?c76bf34eada957f64a0b14990027a576ff9bf379"
        )

    user5 = User(
            first_name='Amanda', last_name='Nunes', username='skunkbarmpot',
            email='joehall@yahoo.com', password='Password1!', age=33,
            location="Pojuca, BR", gender=0, coach=False,
            discipline=3, img_url="https://pbs.twimg.com/media/E2B1AMeWUAM-2vp.jpg"
        )

    user6 = User(
            first_name='Israel', last_name='Adesanya', username='stomachvindicator',
            email='michiel@att.net', password='Password1!', age=31,
            location="Auckland, NZ", gender=1, coach=False,
            discipline=4, img_url="https://www.thesun.co.uk/wp-content/uploads/2020/12/f031d458-5ea0-49cc-8fbd-322b85428a4b.jpg"
        )

    user7 = User(
            first_name='Nate', last_name='Diaz', username='irritatingsoon',
            email='thowell@sbcglobal.net', password='Password1!', age=36,
            location="Stockton, CA", gender=1, coach=False,
            discipline=4, img_url="https://cdn.vox-cdn.com/thumbor/dJZwJD3yg5LR7SsbCSg7eOuodbE=/0x0:4220x2908/1200x800/filters:focal(2279x216:2953x890)/cdn.vox-cdn.com/uploads/chorus_image/image/69490230/1323272327.0.jpg"
        )

    user8 = User(
            first_name='Dana', last_name='White', username='skiertortilla',
            email='grossman@live.com', password='Password1!', age=51,
            location="Las Vegas, NV", gender=1, coach=True,
            discipline=2, img_url="https://cdn.vox-cdn.com/thumbor/Eju-2SC4nkDUXNNouTW09ID-hQ4=/0x0:3300x2392/1200x800/filters:focal(1684x738:2212x1266)/cdn.vox-cdn.com/uploads/chorus_image/image/69173500/1281460972.0.jpg"
        )

    user9 = User(
            first_name='Martin', last_name='Vettori', username='baleeland',
            email='moinefou@me.com', password='Password1!', age=27,
            location="Mezzocorona, Italy", gender=1, coach=False,
            discipline=2, img_url="https://i.ytimg.com/vi/EIep_cqq1D0/maxresdefault.jpg"
        )

    user10 = User(
            first_name='Mario', last_name='Nintendo', username='jordanianswimming',
            email='paley@yahoo.com', password='Password1!', age=40,
            location="Tokyo, Japan", gender=1, coach=True,
            discipline=2, img_url="https://pbs.twimg.com/media/DuNrLAqXcAERPD2.jpg"
        )

    user11 = User(
            first_name='Bowser', last_name='Nintendo', username='starbolinslatter',
            email='airship@icloud.com', password='Password1!', age=40,
            location="Tokyo, Japan", gender=2, coach=False,
            discipline=0, img_url="https://www.smashbros.com/assets_v2/img/fighter/bowser/ss_3.jpg"
        )

    user12 = User(
            first_name='Peach', last_name='Nintendo', username='rustymeddlesome',
            email='paulv@att.net', password='Password1!', age=40,
            location="Tokyo, Japan", gender=0, coach=False,
            discipline=2, img_url="https://i.ytimg.com/vi/zwZ9F0JjIho/maxresdefault.jpg"
        )

    user13 = User(
            first_name='Valentina', last_name='Shevchenko', username='loomcostly',
            email='unreal@mac.com', password='Password1!', age=33,
            location="Bishkek, Kyrgyzstan", gender=0, coach=False,
            discipline=1, img_url="https://i.ytimg.com/vi/v-J5KiWx4Hg/maxresdefault.jpg"
        )

    user14 = User(
            first_name='Rose', last_name='Namajunas', username='abcbrood',
            email='turner.joe@zulauf.com', password='Password1!', age=29,
            location="Milwaukee, WI", gender=0, coach=False,
            discipline=0, img_url="https://cdn.i-scmp.com/sites/default/files/styles/1200x800/public/d8/images/canvas/2021/04/24/e3ed2a5c-e249-41a3-97d1-210b1274673d_13764dbc.jpg?itok=c5ITmOCx&v=1619244831"
        )

    user15 = User(
            first_name='Marion', last_name='Renau', username='fennelsymptom',
            email='frank.borer@gerhold.info', password='Password1!', age=44,
            location="Tulare, CA", gender=0, coach=False,
            discipline=5, img_url="https://bucket.mn2s.com/wp-content/uploads/2021/02/12160456/Marion-Reneau.png"
        )

    user16 = User(
            first_name='Miesha', last_name='Tate', username='chilliclang',
            email='reta66@yahoo.com', password='Password1!', age=34,
            location="Tacoma, WA", gender=0, coach=False,
            discipline=0, img_url="https://www.letsengage.com/storage/talents/1547086355rs-247448-RS-Miesha-Tate-01.jpg"
        )

    user17 = User(
            first_name='Raquel', last_name='Pennington', username='onionsexpert',
            email='vreichert@howell.net', password='Password1!', age=32,
            location="Colorado Springs, CO", gender=0, coach=True,
            discipline=1, img_url="https://i.pinimg.com/originals/d9/65/e5/d965e5ef6feaf622e9ed7a3cd2976dbb.jpg"
        )

    user18 = User(
            first_name='Holly', last_name='Holm', username='chimpanzeegreens',
            email='vfeeney@oreilly.com', password='Password1!', age=39,
            location="Albuquerque, NM", gender=0, coach=False,
            discipline=4, img_url="https://static.onecms.io/wp-content/uploads/sites/20/2015/11/holly-holm-435.jpg"
        )

    user19 = User(
            first_name='Meagan', last_name='Anderson', username='nigeriansouthern',
            email='kenneth.tremblay@gislason.org', password='Password1!', age=31,
            location="Gold Coast, Australia", gender=0, coach=True,
            discipline=1, img_url="https://invictafc.com/wp-content/uploads/2014/12/Megan_Anderson_Bio.jpg"
        )

    user20 = User(
            first_name='Yoshi', last_name='Nintendo', username='plentyloutish',
            email='waelchi.lowell@lebsack.com', password='Password1!', age=50,
            location="Tokyo, Japan", gender=2, coach=True,
            discipline=9, img_url="https://www.smashbros.com/assets_v2/img/fighter/yoshi/ss_1.jpg"
        )

    user21 = User(
            first_name='Connor', last_name='McGregor', username='waship',
            email='catyunclescrooge@yahoo.com', password='Password1!', age=33,
            location="Dublin, Ireland", gender=1, coach=False,
            discipline=6, img_url="https://publish.one37pm.net/wp-content/uploads/2020/10/conor-mcgregor-mobile.jpg"
        )

    user22 = User(
            first_name='Dustin', last_name='Poirier', username='jollymagenta',
            email='robbyclever@yahoo.com', password='Password1!', age=32,
            location="Coconut Creek, FL", gender=1, coach=False,
            discipline=5, img_url="https://img.bleacherreport.net/img/images/photos/003/899/697/a4d2fc575039ce2ea97715f6706842e9_crop_north.jpg?1610647536&w=3072&h=2048"
        )

    user23 = User(
            first_name='Kevin', last_name='Holland', username='squarelutz',
            email='marcbrooding@gmail.com', password='Password1!', age=28,
            location="Riverside, CA", gender=1, coach=False,
            discipline=9, img_url="https://cdn.vox-cdn.com/thumbor/qx04Bhb3uCwwQjn2_vejJSXjZQg=/1400x1400/filters:format(jpeg)/cdn.vox-cdn.com/uploads/chorus_asset/file/22385155/1290956479.jpg"
        )

    user24 = User(
            first_name='Karl', last_name='Roberson', username='assetincomplete',
            email='zandercuddly@yahoo.com', password='Password1!', age=30,
            location="Neptune, NJ", gender=1, coach=False,
            discipline=0, img_url="https://media.elegantcms.io/a/96dc72d1-4d96-40b8-a3bd-cd44c423ca4b/87d71980-6f9a-47ab-bfcb-aea7f749bcdb/1516123543/o/karl-ranking.jpg?1516123543"
        )

    user25 = User(
            first_name='Robert', last_name='Whittaker', username='beginningscuba',
            email='confusedsu@optonline.net', password='Password1!', age=30,
            location="Auckland, NZ", gender=1, coach=True,
            discipline=9, img_url="https://images.daznservices.com/di/library/DAZN_News/62/e/robert-whittaker-7212020-getty-ftr_1rl5gancs4wze1xqu2ao5cvv1h.jpg?t=1958183011&quality=60&w=1280&h=720"
        )

    user26 = User(
            first_name='Derek', last_name='Brunson', username='purringlonghorn',
            email='wearysawney@me.com', password='Password1!', age=37,
            location="Wilmington, NC", gender=1, coach=False,
            discipline=8, img_url="https://s.yimg.com/os/creatr-uploaded-images/2020-07/f524c1e0-d351-11ea-bfb7-d00291157ffa"
        )

    user27 = User(
            first_name='Paulo', last_name='Costa', username='trebleflyingfish',
            email='jealousreggie@aol.com', password='Password1!', age=30,
            location="Belo Horizonte, Brazil", gender=1, coach=False,
            discipline=0, img_url="https://cdn.vox-cdn.com/thumbor/nYQmrm_0-Qe7qDtEvWUrlNXP7lA=/1400x1050/filters:format(jpeg)/cdn.vox-cdn.com/uploads/chorus_asset/file/19016523/131_Paulo_Costa.jpg"
        )

    user28 = User(
            first_name='Godzilla', last_name='Kaiju', username='culturaldrafter',
            email='optimisticaly@msn.com', password='Password1!', age=1000,
            location="Tokyo, Japan", gender=2, coach=True,
            discipline=6, img_url="https://static.wikia.nocookie.net/godzilla/images/3/33/Godzilla_2021.jpg/revision/latest?cb=20210314011302"
        )

    user29 = User(
            first_name='Zhang', last_name='Weili', username='easilyundies',
            email='indexwretched@yahoo.com', password='Password1!', age=31,
            location="Bejing, China", gender=0, coach=True,
            discipline=1, img_url="https://images.daznservices.com/di/library/DAZN_News/66/6c/weili-zhang-030420-getty-ftr_kw4zuvoodse01510hagpkb44w.jpg?t=-1415331856&quality=60&w=1280&h=720"
        )

    user30 = User(
            first_name='Walter', last_name='White', username='blue',
            email='wwhite@yahoo.com', password='Password1!', age=52,
            location="Albuquerque, NM", gender=1, coach=True,
            discipline=8, img_url="https://cdn.theatlantic.com/thumbor/kRAzxqy5K2BR8LVPxXv0VZvZqXk=/0x0:675x380/655x369/media/img/posts/2013/10/Walter_White/original.png"
        )

    user2.user_likes.append(user1)
    user3.user_likes.append(user22)
    user4.user_likes.append(user21)
    user5.user_likes.append(user15)
    user6.user_likes.append(user12)
    user7.user_likes.append(user1)
    user8.user_likes.append(user3)
    user9.user_likes.append(user1)
    user10.user_likes.append(user14)
    user11.user_likes.append(user1)
    user12.user_likes.append(user14)
    user13.user_likes.append(user1)
    user14.user_likes.append(user14)
    user15.user_likes.append(user1)
    user16.user_likes.append(user1)
    user17.user_likes.append(user4)
    user18.user_likes.append(user1)
    user19.user_likes.append(user11)
    user20.user_likes.append(user1)
    user21.user_likes.append(user1)
    user22.user_likes.append(user12)
    user23.user_likes.append(user1)
    user24.user_likes.append(user19)
    user25.user_likes.append(user13)
    user26.user_likes.append(user1)
    user27.user_likes.append(user1)
    user28.user_likes.append(user18)
    user29.user_likes.append(user1)
    user30.user_likes.append(user11)

    db.session.add_all([
            user1,
            user2,
            user3,
            user4,
            user5,
            user6,
            user7,
            user8,
            user9,
            user10,
            user11,
            user12,
            user13,
            user14,
            user15,
            user17,
            user18,
            user19,
            user20,
            user21,
            user22,
            user23,
            user24,
            user25,
            user26,
            user27,
            user28,
            user29,
            user30
            ])

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_users():
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
    db.session.commit()
