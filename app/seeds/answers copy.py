from app.models import db, Answer

def seed_answers():

    answer31= Answer(
        user_id=31,
        about="They call me Hummus",
        weight_class=1,
        reach=70,
        professional_level=0,
        fav_rocky_fighter="Rocky Balboa",
        vaccinated=True,
        nickname="Not hummus",
        walkout_song="'Redbone' by Childish Gambino",
        availability=2,
        in_person=True)

    answer32= Answer(
        user_id=32,
        about="I'm that guy pal",
        weight_class=2,
        reach=90,
        professional_level=1,
        current_record='1-0-0',
        fav_rocky_fighter="Rocky Balboa",
        vaccinated=True,
        nickname="That guy",
        walkout_song="'Wannabe' by Spice Girls",
        availability=2,
        in_person=True,
        rate=3)

    answer33= Answer(
        user_id=33,
        about="They call me Bam Bam",
        weight_class=2,
        reach=75,
        professional_level=2,
        current_record='13-0-0',
        fav_rocky_fighter="Apollo Creed",
        vaccinated=True,
        nickname="Bam bam",
        walkout_song="'Eye of the Tiger' by Survivor",
        pets="Dogs",
        availability=0,
        in_person=True)

    answer33= Answer(
        user_id=33,
        about="You are not prepared.",
        weight_class=6,
        reach=68,
        professional_level=2,
        current_record='12-2-0',
        fav_rocky_fighter="Rocky Balboa",
        vaccinated=True,
        nickname="Rowdy",
        has_kids=True,
        walkout_song="'Bad Reputation' by Joan Jett",
        availability=0,
        in_person=True,
        rate=45)

    answer34= Answer(user_id=34, about="Fight with the best, lose with the rest.", weight_class=6, reach=69, professional_level=2, current_record='21-4-0', previous_titles=6, vaccinated=True, nickname="The Lionness", has_kids=True, walkout_song="'Champion' by Carrie Underwood", availability=1, in_person=True)
    answer35= Answer(user_id=35, about="I have legs for days", weight_class=1, reach=80, professional_level=2, current_record='21-1-0', previous_titles="Middleweight", fav_rocky_fighter="Apollo Creed", vaccinated=False, nickname="The Last Stylebender", pets="Dogs", availability=1, in_person=True)
    answer36= Answer(user_id=36, about="I'm on another level", weight_class=0, reach=76, professional_level=2, current_record='21-13-0', vaccinated=True, availability=2, in_person=False)
    answer37= Answer(user_id=37, about="If you have a dream, don’t just sit there.",weight_class=2, reach=65, professional_level=1, previous_titles="President of the UFC", fav_rocky_fighter="Rocky Balboa", vaccinated=False, availability=2, in_person=False, rate=15000)
    answer38= Answer(user_id=38, about="When the going gets tough, put one foot in front of the other and just keep going.",weight_class=1, reach=74, professional_level=2, current_record='17-5-1', vaccinated=False, nickname="The Italian Dream", walkout_song="'Somewhere I Belong' by Linkin Park", availability=1, in_person=True)
    answer39= Answer(user_id=39, about="Courage doesn't always roar.",weight_class=1, reach=74, professional_level=1, current_record='1-0-0', vaccinated=False, availability=1, in_person=True, rate=55)
    answer40= Answer(user_id=40, about="Success is the sum of small efforts, repeated day in and day out.",weight_class=2, reach=160, professional_level=1, current_record='0-1-0', fav_rocky_fighter="Rocky Balboa", vaccinated=True, has_kids=True, walkout_song="'The Way I Am' by Eminem", pets="Cats", availability=0, in_person=True)
    answer41= Answer(user_id=41, about="It always seems impossible until it's done.", weight_class=6, reach=82, professional_level=0, vaccinated=False, availability=2, in_person=True)
    answer42= Answer(user_id=42, about="It does not matter how slowly you go so long as you do not stop.", weight_class=3, reach=66, professional_level=2, current_record='21-3-0', previous_titles=3, vaccinated=False, nickname="Bullet", has_kids=True, walkout_song="'How To Talk' by Lil Uzi Vert", pets="Cats", availability=2, in_person=True)
    answer43= Answer(user_id=43, about="My strength lies solely in my tenacity.", weight_class=3, reach=65, professional_level=2, current_record='11-4-0', fav_rocky_fighter="Rocky Balboa", vaccinated=False, nickname="Thug", availability=0, in_person=False)
    answer44= Answer(user_id=44, about="How long should you try? Until.", weight_class=6, reach=68, professional_level=2, current_record='9-8-1', vaccinated=True, nickname="The Belizean Bruiser", availability=2, in_person=True)
    answer45= Answer(user_id=45, about="Don’t be discouraged. It’s often the last key in the bunch that opens the lock.", weight_class=6, reach=65, professional_level=2, current_record='19-7-0', fav_rocky_fighter="Rocky Balboa", vaccinated=True, nickname="Cupcake", walkout_song="'The Ecstasy of Gold' by Enniocone", pets="Iguana", availability=0, in_person=True, rate=150)
    answer46= Answer(user_id=46, about="I'm on another level", weight_class=6, reach=67, professional_level=2, current_record='11-9-0', vaccinated=False, nickname="Rocky", availability=2, in_person=True)
    answer47= Answer(user_id=47, about="You just can’t beat the person who won’t give up.", weight_class=6, reach=69, professional_level=2, current_record='14-5-0', fav_rocky_fighter="Ivan Drago", vaccinated=False, nickname="The Preacher's Daughter", has_kids=True, pets="Whale", availability=2, in_person=False, rate=125)
    answer48= Answer(user_id=48, about="Lights out", weight_class=4, reach=72, professional_level=2, current_record='11-5-0', vaccinated=True, availability=2, in_person=True, rate=300)
    answer49= Answer(user_id=49, about="Success is what happens after you have survived all your mistakes.",weight_class=1, reach=65, professional_level=0, fav_rocky_fighter="Rocky Balboa", vaccinated=False, availability=2, in_person=True)
    answer50= Answer(user_id=50, about="Every master was once a disaster.", weight_class=0, reach=74, professional_level=2, current_record='22-6-0', vaccinated=True, nickname="The Notorious", availability=2, in_person=True)
    answer51= Answer(user_id=51, about="I have not failed. I've just found 10,000 ways that won't work.", weight_class=0, reach=72, professional_level=2, current_record='28-6-0', fav_rocky_fighter="Adonis Johnson", vaccinated=False, nickname="The Diamond", pets="Shark", availability=2, in_person=False)
    answer52= Answer(user_id=52, about="The supreme art of war is to subdue the enemy without fighting.", weight_class=1, reach=81, professional_level=2, current_record='21-7-0', fav_rocky_fighter="Rocky Balboa", vaccinated=False, nickname="The Trailblazer", pets="Cats", availability=1, in_person=True)
    answer53= Answer(user_id=53, about="If you are going through hell, keep going.", weight_class=1, reach=74, professional_level=2, current_record='9-4-0', fav_rocky_fighter="Ivan Drago", vaccinated=False, nickname="Baby K", availability=1, in_person=True)
    answer54= Answer(user_id=54, about="Sometimes even to live is an act of courage.", weight_class=1, reach=73, professional_level=2, current_record='24-5-0', fav_rocky_fighter="Adonis Johnson", vaccinated=True, nickname="Baby Reaper", pets="Dogs", availability=2, in_person=True)
    answer55= Answer(user_id=55, about="I am a slow walker, but I never walk back.", weight_class=1, reach=77, professional_level=2, current_record='22-7-0', vaccinated=False, walkout_song="'The Foggy Dew' by Father Charles O'Neill", availability=0, in_person=True, rate=99)
    answer56= Answer(user_id=56, about="Never confuse a single defeat with a final defeat.", weight_class=1, reach=72, professional_level=2, current_record='13-1-0', fav_rocky_fighter="Rocky Balboa", vaccinated=True, nickname="The Eraser", pets="Dogs", availability=2, in_person=True)
    answer57= Answer(user_id=57, about="Just because you fail once doesn't mean you're gonna fail at everything.", weight_class=2, reach=99999, professional_level=1, fav_rocky_fighter="Apollo Creed", vaccinated=True, nickname="King of Monsters", availability=1, in_person=True)
    answer58= Answer(user_id=58, about="Dripping water hollows out stone, not through force but through persistence.", weight_class=0, reach=64, professional_level=1, current_record='1-0-0', fav_rocky_fighter="Adonis Johnson", vaccinated=True, nickname="Magnum", availability=2, in_person=False, rate=100000)
    answer59= Answer(user_id=59, about="The difference between a successful person and others is not a lack of strength, not a lack of knowledge, but rather a lack in will.", weight_class=3, reach=63, professional_level=2, current_record='21-2-0', previous_titles=3, fav_rocky_fighter="Apollo Creed", vaccinated=False, availability=2, in_person=True, rate=500)
    answer60= Answer(user_id=60, about="I am not in danger, Skyler. I am the danger", weight_class=0, reach=64, professional_level=1, current_record='1-0-0', fav_rocky_fighter="Adonis Johnson", vaccinated=True, nickname="Heisenberg", walkout_song="'Crystal Blue Persuasion' by Tommy James & The Shondells", availability=0, in_person=False, rate=1000000)
    answer61= Answer(user_id=61, about="It always seems impossible until it's done.", weight_class=6, reach=82, professional_level=0, vaccinated=False, availability=2, in_person=True)
    answer62= Answer(user_id=62, about="It does not matter how slowly you go so long as you do not stop.", weight_class=3, reach=66, professional_level=2, current_record='21-3-0', previous_titles=3, vaccinated=False, nickname="Bullet", has_kids=True, walkout_song="'How To Talk' by Lil Uzi Vert", pets="Cats", availability=2, in_person=True)
    answer63= Answer(user_id=63, about="My strength lies solely in my tenacity.", weight_class=3, reach=65, professional_level=2, current_record='11-4-0', fav_rocky_fighter="Rocky Balboa", vaccinated=False, nickname="Thug", availability=0, in_person=False)
    answer64= Answer(user_id=64, about="How long should you try? Until.", weight_class=6, reach=68, professional_level=2, current_record='9-8-1', vaccinated=True, nickname="The Belizean Bruiser", availability=2, in_person=True)
    answer65= Answer(user_id=65, about="Don’t be discouraged. It’s often the last key in the bunch that opens the lock.", weight_class=6, reach=65, professional_level=2, current_record='19-7-0', fav_rocky_fighter="Rocky Balboa", vaccinated=True, nickname="Cupcake", walkout_song="'The Ecstasy of Gold' by Enniocone", pets="Iguana", availability=0, in_person=True, rate=150)
    answer66= Answer(user_id=66, about="I'm on another level", weight_class=6, reach=67, professional_level=2, current_record='11-9-0', vaccinated=False, nickname="Rocky", availability=2, in_person=True)
    answer67= Answer(user_id=67, about="You just can’t beat the person who won’t give up.", weight_class=6, reach=69, professional_level=2, current_record='14-5-0', fav_rocky_fighter="Ivan Drago", vaccinated=False, nickname="The Preacher's Daughter", has_kids=True, pets="Whale", availability=2, in_person=False, rate=125)
    answer68= Answer(user_id=68, about="Lights out", weight_class=4, reach=72, professional_level=2, current_record='11-5-0', vaccinated=True, availability=2, in_person=True, rate=300)
    answer69= Answer(user_id=69, about="Success is what happens after you have survived all your mistakes.",weight_class=1, reach=65, professional_level=0, fav_rocky_fighter="Rocky Balboa", vaccinated=False, availability=2, in_person=True)
    answer70= Answer(user_id=70, about="Every master was once a disaster.", weight_class=0, reach=74, professional_level=2, current_record='22-6-0', vaccinated=True, nickname="The Notorious", availability=2, in_person=True)
    answer71= Answer(user_id=71, about="I have not failed. I've just found 10,000 ways that won't work.", weight_class=0, reach=72, professional_level=2, current_record='28-6-0', fav_rocky_fighter="Adonis Johnson", vaccinated=False, nickname="The Diamond", pets="Shark", availability=2, in_person=False)
    answer72= Answer(user_id=72, about="The supreme art of war is to subdue the enemy without fighting.", weight_class=1, reach=81, professional_level=2, current_record='21-7-0', fav_rocky_fighter="Rocky Balboa", vaccinated=False, nickname="The Trailblazer", pets="Cats", availability=1, in_person=True)
    answer73= Answer(user_id=73, about="If you are going through hell, keep going.", weight_class=1, reach=74, professional_level=2, current_record='9-4-0', fav_rocky_fighter="Ivan Drago", vaccinated=False, nickname="Baby K", availability=1, in_person=True)
    answer74= Answer(user_id=74, about="Sometimes even to live is an act of courage.", weight_class=1, reach=73, professional_level=2, current_record='24-5-0', fav_rocky_fighter="Adonis Johnson", vaccinated=True, nickname="Baby Reaper", pets="Dogs", availability=2, in_person=True)
    answer75= Answer(user_id=75, about="I am a slow walker, but I never walk back.", weight_class=1, reach=77, professional_level=2, current_record='22-7-0', vaccinated=False, walkout_song="'The Foggy Dew' by Father Charles O'Neill", availability=0, in_person=True, rate=99)
    answer76= Answer(user_id=76, about="Never confuse a single defeat with a final defeat.", weight_class=1, reach=72, professional_level=2, current_record='13-1-0', fav_rocky_fighter="Rocky Balboa", vaccinated=True, nickname="The Eraser", pets="Dogs", availability=2, in_person=True)
    answer77= Answer(user_id=77, about="Just because you fail once doesn't mean you're gonna fail at everything.", weight_class=2, reach=99999, professional_level=1, fav_rocky_fighter="Apollo Creed", vaccinated=True, nickname="King of Monsters", availability=1, in_person=True)
    answer78= Answer(user_id=78, about="Dripping water hollows out stone, not through force but through persistence.", weight_class=0, reach=64, professional_level=1, current_record='1-0-0', fav_rocky_fighter="Adonis Johnson", vaccinated=True, nickname="Magnum", availability=2, in_person=False, rate=100000)
    answer79= Answer(user_id=79, about="The difference between a successful person and others is not a lack of strength, not a lack of knowledge, but rather a lack in will.", weight_class=3, reach=63, professional_level=2, current_record='21-2-0', previous_titles=3, fav_rocky_fighter="Apollo Creed", vaccinated=False, availability=2, in_person=True, rate=500)
    answer80= Answer(user_id=80, about="I am not in danger, Skyler. I am the danger", weight_class=0, reach=64, professional_level=1, current_record='1-0-0', fav_rocky_fighter="Adonis Johnson", vaccinated=True, nickname="Heisenberg", walkout_song="'Crystal Blue Persuasion' by Tommy James & The Shondells", availability=0, in_person=False, rate=1000000)

    