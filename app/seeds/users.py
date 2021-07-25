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


    user31 = User(first_name='Trinity', last_name='Betts', email='donato.smith@gmail.com', username='pampersgymnasium', password='Password1!', gender=1, coach=True, discipline=6, location='Fairwood, WA', age=26, img_url='inTheWorks.jpg')
    user32 = User(first_name='Amayah', last_name='Searle', email='aryanna_berge8@gmail.com', username='budweiserwrestling', password='Password1!', gender=2, coach=True, discipline=6, location='Levittown,PA',age=38, img_url='inTheWorks.jpg')
    user33 = User(first_name='Ellie-May', last_name='Hulme', email='renee57@yahoo.com', username='allianzequipment', password='Password1!', gender=2, coach=False, discipline=0, location='Dix Hills,NY', age=29, img_url='inTheWorks.jpg')
    user34 = User(first_name='Sufyaan', last_name='Roach', email='waino67@yahoo.com', username='mcdonaldsathlete', password='Password1!', gender=1, coach=True, discipline=6, location='San Juan,TX', age=50, img_url='inTheWorks.jpg')
    user35 = User(first_name='Kaeden', last_name='Strong', email='arjun.okon96@gmail.com', username='ebayclub', password='Password1!', gender=1, coach=False, discipline=6, location='Lafayette,IN', age=64, img_url='inTheWorks.jpg')
    user36 = User(first_name='Mayson', last_name='Nelson', email='brown.heaney75@hotmail.com', username='delltarget', password='Password1!', gender=2, coach=True, discipline=7, location='China, ME', age=45, img_url='inTheWorks.jpg')
    user37 = User(first_name='Onur', last_name='Gonzalez', email='waylon.block@yahoo.com', username='chevroletmat', password='Password1!', gender=1, coach=False, discipline=7, location='Galena, IN', age=48, img_url='inTheWorks.jpg')
    user38 = User(first_name='Siena', last_name='Tate', email='cordia_klein@hotmail.com', username='ikeawrestler', password='Password1!', gender=2, coach=True, discipline=7, location='Saticoy, CA', age=43, img_url='inTheWorks.jpg')
    user39 = User(first_name='Alfie-Jay', last_name='Singh', email='nakia_prohaska46@hotmail.com', username='audiswimmer', password='Password1!', gender=0, coach=False, discipline=0, location='New Franklin, MO', age=19, img_url='inTheWorks.jpg')
    user40 = User(first_name='Ayden', last_name='Leon', email='oma_wolff97@gmail.com', username='exxonracer', password='Password1!', gender=1, coach=True, discipline=9, location='LaFollette, TN', age=66, img_url='inTheWorks.jpg')
    user41 = User(first_name='Kevin', last_name='Cordova', email='kevinsux@measdsad.com', username='facebookslalom', password='Password1!', gender=1, coach=True, discipline=8, location='Malad City, ID', age=44, img_url='inTheWorks.jpg')
    user42 = User(first_name='Amalia', last_name='Stewart', email='keara_hirthe98@hotmail.com', username='heinzsailing', password='Password1!', gender=2, coach=True, discipline=7, location='Glen Rose, TX', age=65, img_url='inTheWorks.jpg')
    user43 = User(first_name='Ajwa', last_name='Ferguson', email='emilia.friesen@hotmail.com',username='nikewaterski', password='Password1!', gender=2, coach=True, discipline=6, location='Malta, MT', age=59, img_url='inTheWorks.jpg')
    user44 = User(first_name='Chelsey', last_name='Weeks',email='cathy96@gmail.com', username='pradastrike', password='Password1!', gender=2, coach=False, discipline=5, location='North York, PA', age=33, img_url='inTheWorks.jpg')
    user45 = User(first_name='Zahrah', last_name='Fry', email='ona_medhurst@gmail.com',username='visatriathlete', password='Password1!', gender=1, coach=True, discipline=4, location='Newton, NJ', age=42, img_url='inTheWorks.jpg')
    user46 = User(first_name='Kabir', last_name='East', email='pattie70@hotmail.com',username='colapingpong', password='Password1!', gender=1, coach=False, discipline=3, location='Puhi, HI', age=20, img_url='inTheWorks.jpg')
    user47 = User(first_name='Ruby-Leigh', last_name='Drew', email='bettie.reynolds@hotmail.com',username='kraftdiver', password='Password1!', gender=1, coach=True, discipline=2, location='Cedar Hill, MO', age=52, img_url='inTheWorks.jpg')
    user48 = User(first_name='Connie', last_name='Norman', email='enoch_becker@gmail.com',username='fordarcher', password='Password1!', gender=0, coach=False, discipline=1, location='West Fairview, PA', age=69, img_url='inTheWorks.jpg')
    user49 = User(first_name='Osman', last_name='Ballard', email='rylan63@gmail.com',username='cartierfootball', password='Password1!', gender=1, coach=False, discipline=1, location='Dulles Town Center, VA', age=25, img_url='inTheWorks.jpg')
    user50 = User(first_name='Mohammad', last_name='Pearce', email='audrey_witting@yahoo.com',username='spritehandball', password='Password1!', gender=0, coach=True, discipline=1, location='Orange, MA', age=56, img_url='inTheWorks.jpg')
    user51 = User(first_name='Talia', last_name='Lang', email='watermelon@gmail.com',username='oraclepuck', password='Password1!', gender=1, coach=True, discipline=1, location='McGuire, NJ', age=37, img_url='inTheWorks.jpg')
    user52 = User(first_name='Alanna', last_name='Bowes', email='antonina.mayer50@gmail.com',username='kellogsiceskates', password='Password1!', gender=1, coach=True, discipline=1, location='Kenhorst, PA', age=34, img_url='inTheWorks.jpg')
    user53 = User(first_name='Usman', last_name='Cantrell', email='andreanne.morissette@hotmail.com',username='siemenscleats', password='Password1!', gender=1, coach=True, discipline=2, location='Waynesboro, VA', age=45, img_url='inTheWorks.jpg')
    user54 = User(first_name='Matas', last_name='Washington', email='camylle.abernathy55@yahoo.com',username='ferrarirugby', password='Password1!', gender=1, coach=True, discipline=2, location='Long Beach, CA', age=61, img_url='inTheWorks.jpg')
    user55 = User(first_name='Kylo', last_name='Kirk', email='janet76@gmail.com',username='pepsiparkour', password='Password1!', gender=2, coach=True, discipline=2, location='Fort Meade, MD', age=55, img_url='inTheWorks.jpg')
    user56 = User(first_name='Faisal', last_name='Cohen', email='jedidiah82@yahoo.com',username='rolexplayoffs', password='Password1!', gender=1, coach=False, discipline=2, location='Pocomoke City, MD', age=29, img_url='inTheWorks.jpg')
    user57 = User(first_name='Layla-Rose', last_name='Gibson',email='price87@yahoo.com', username='shellsport', password='Password1!', gender=1, coach=True, discipline=3,  location='Hamburg, PA', age=35, img_url='inTheWorks.jpg')
    user58 = User(first_name='Tevin', last_name='Schaefer', email='osborne.durgan58@gmail.com',username='burberrydiamond', password='Password1!', gender=1, coach=True, discipline=3, location='Lakewood Shores, IL', age=18, img_url='inTheWorks.jpg')
    user59 = User(first_name='Nicky', last_name='Chandler', email='verdie_walter37@yahoo.com',username='adidasluge', password='Password1!', gender=2, coach=True, discipline=3, location='Kansas City, MO', age=44, img_url='inTheWorks.jpg')
    user60 = User(first_name='Kayne', last_name='Holman', email='dewayne95@yahoo.com', username='ciscosled', password='Password1!', gender=1, coach=True, discipline=4, location='Oak Grove, LA', age=57, img_url='inTheWorks.jpg')
    user61 = User(first_name='Pixie', last_name='Lake', email='jovanny.bode56@gmail.com', username='malboropolevault', password='Password1!', gender=1, coach=True, discipline=4, location='Hudson Oaks, TX', age=25, img_url='inTheWorks.jpg')
    user62 = User(first_name='Bert', last_name='Barber', email='nelson_schowalter@hotmail.com',username='porschejumprope', password='Password1!', gender=1, coach=True, discipline=7, location='Kennesaw, GA', age=19, img_url='inTheWorks.jpg')
    user63 = User(first_name='Glen', last_name='Berry', email='scarlett_medhurst19@yahoo.com',username='ericssondugout', password='Password1!', gender=1, coach=True, discipline=9, location='Fobes Hill, WA', age=48, img_url='inTheWorks.jpg')
    user64 = User(first_name='Ira', last_name='Rowe', email='uriah_mcclure93@gmail.com',username='nescaferow', password='Password1!', gender=0, coach=False, discipline=9, location='Jacinto City, TX', age=46, img_url='inTheWorks.jpg')
    user65 = User(first_name='Leland', last_name='Alvarez', email='tiana_dooley@gmail.com', username='hondakickball', password='Password1!', gender=1, coach=True, discipline=9, location='Warminster Heights, PA', age=33, img_url='inTheWorks.jpg')
    user66 = User(first_name='Jonathan', last_name='Garner', email='helmer45@gmail.com',username='mercedespaddleball', password='Password1!', gender=1, coach=False, discipline=9, location='Riverside, PA', age=46, img_url='inTheWorks.jpg')
    user67 = User(first_name='Kristopher', last_name='Lucas', email='cyril_hills@gmail.com',username='subwayhometeam', password='Password1!', gender=1, coach=True, discipline=9, location='Germantown, TN', age=50, img_url='inTheWorks.jpg')
    user68 = User(first_name='Fredrick', last_name='Swanson', email='lane_mitchell97@gmail.com',username='nissancurling', password='Password1!', gender=0, coach=False, discipline=8, location='Avonmore, PA', age=24, img_url='inTheWorks.jpg')
    user69 = User(first_name='Joshua', last_name='Sims', email='orville_dare@yahoo.com',username='lexushighjump', password='Password1!', gender=1, coach=True, discipline=8, location='Granville, IL', age=23, img_url='inTheWorks.jpg')
    user70 = User(first_name='Carolyn', last_name='Wright', email='greta72@yahoo.com',username='nestleshortstop', password='Password1!', gender=0, coach=False, discipline=8, location='Hayneville, AL', age=29, img_url='inTheWorks.jpg')
    user71 = User(first_name='Alberto', last_name='Terry', email='yasmine43@gmail.com',username='heinekenbaseball', password='Password1!', gender=1, coach=True, discipline=8, location='Francis, UT', age=61, img_url='inTheWorks.jpg')
    user72 = User(first_name='Sarah', last_name='Kemp', email='leilani5@hotmail.com',username='microsofticehockey', password='Password1!', gender=1, coach=False, discipline=4, location='Narberth, PA', age=44, img_url='inTheWorks.jpg')
    user73 = User(first_name='Enid', last_name='Swan', email='roslyn78@yahoo.com', username='colgatecompetitor', password='Password1!', gender=2, coach=True, discipline=4, location='Brooklyn, WI', age=46, img_url='inTheWorks.jpg')
    user74 = User(first_name='Curtis', last_name='Bostock', email='andre.roob@gmail.com', username='starbucksicerink', password='Password1!', gender=1, coach=True, discipline=4, location='Vidalia, LA', age=32, img_url='inTheWorks.jpg')
    user75 = User(first_name='Raphael', last_name='Healy', email='norris38@yahoo.com', username='samsungscoreboard', password='Password1!', gender=1, coach=True, discipline=5, location='Sand Lake, MI', age=35, img_url='inTheWorks.jpg')
    user76 = User(first_name='Alyssia', last_name='Hansen', email='ettie64@gmail.com', username='gucciarena', password='Password1!', gender=2, coach=True, discipline=5, location='East Port Orchard, WA', age=54, img_url='inTheWorks.jpg')
    user77 = User(first_name='Fallon', last_name='Byrd', email='rachel99@yahoo.com', username='ibmhalftime', password='Password1!', gender=1, coach=True, discipline=5, location='Wheeler, TX', age=28, img_url='inTheWorks.jpg')
    user78 = User(first_name='Giles', last_name='Fowler', email='alexander.will0@hotmail.com', username='disneyboxer', password='Password1!', gender=2, coach=False, discipline=0, location='DeWitt, MI', age=49, img_url='inTheWorks.jpg')
    user79 = User(first_name='Ayomide', last_name='Horne', email='allene.mraz@yahoo.com', username='boeingplay', password='Password1!', gender=1, coach=True, discipline=5, location='Spring City, PA', age=43, img_url='inTheWorks.jpg')
    user80 = User(first_name='Bluebell', last_name='Mooney', email='ruth.smith@hotmail.com', username='santanderdiving', password='Password1!', gender=1, coach=True, discipline=6, location='Westville, IN', age=61, img_url='inTheWorks.jpg')

    user2.liked_by.append(user1)
    user3.liked_by.append(user22)
    user4.liked_by.append(user21)
    user5.liked_by.append(user15)
    user6.liked_by.append(user12)
    user7.liked_by.append(user1)
    user8.liked_by.append(user3)
    user9.liked_by.append(user1)
    user10.liked_by.append(user14)
    user11.liked_by.append(user1)
    user12.liked_by.append(user14)
    user13.liked_by.append(user1)
    user14.liked_by.append(user14)
    user15.liked_by.append(user1)
    user16.liked_by.append(user1)
    user17.liked_by.append(user4)
    user18.liked_by.append(user1)
    user19.liked_by.append(user11)
    user20.liked_by.append(user1)
    user21.liked_by.append(user1)
    user22.liked_by.append(user12)
    user23.liked_by.append(user1)
    user24.liked_by.append(user19)
    user25.liked_by.append(user13)
    user26.liked_by.append(user1)
    user27.liked_by.append(user1)
    user28.liked_by.append(user18)
    user29.liked_by.append(user1)
    user30.liked_by.append(user11)
    user1.liked_by.append(user27)
    user1.liked_by.append(user21)
    user1.liked_by.append(user18)
    user1.liked_by.append(user31)
    user1.liked_by.append(user32)
    user1.liked_by.append(user33)
    user1.liked_by.append(user34)
    user1.liked_by.append(user46)
    user1.liked_by.append(user57)
    user1.liked_by.append(user58)
    user1.liked_by.append(user60)
    user1.liked_by.append(user61)
    user1.liked_by.append(user62)
    user1.liked_by.append(user65)
    user1.liked_by.append(user66)
    user1.liked_by.append(user67)
    user1.liked_by.append(user68)
    user1.liked_by.append(user69)
    user1.liked_by.append(user70)
    user1.liked_by.append(user71)
    user1.liked_by.append(user72)
    user1.liked_by.append(user73)
    user65.liked_by.append(user1)
    user66.liked_by.append(user1)
    user67.liked_by.append(user1)
    user68.liked_by.append(user1)
    user69.liked_by.append(user1)
    user70.liked_by.append(user1)
    user71.liked_by.append(user1)
    user72.liked_by.append(user1)
    user73.liked_by.append(user1)
    user1.disliked_by.append(user30)

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
            user16,
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
            user30,
            user31,
            user32,
            user33,
            user34,
            user35,
            user36,
            user37,
            user38,
            user39,
            user40,
            user41,
            user42,
            user43,
            user44,
            user45,
            user46,
            user47,
            user48,
            user49,
            user50,
            user51,
            user52,
            user53,
            user54,
            user55,
            user56,
            user57,
            user58,
            user59,
            user60,
            user61,
            user62,
            user63,
            user64,
            user65,
            user66,
            user67,
            user68,
            user69,
            user70,
            user71,
            user72,
            user73,
            user74,
            user75,
            user76,
            user77,
            user78,
            user79,
            user80
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
