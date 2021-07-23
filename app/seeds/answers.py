from app.models import db, Answer

def seed_answers():


    answer1= Answer(user_id=1, about="Hey I'm demo user and I bet I can spar really good", weight_class='Middleweight', reach=70, professional_level='Amateur', fav_rocky_fighter="Rocky Balboa", vaccinated=True, nickname="Demo-lition", walkout_song="'Eye of the Tiger' by Survivor", availability="All Week", in_person=True)
    answer2= Answer(user_id=2, about="I'm that guy pal", weight_class='Heavyweight', reach=90, professional_level='Amateur', current_record='1-0-0', fav_rocky_fighter="Rocky Balboa", vaccinated=True, nickname="That guy", walkout_song="'Wannabe' by Spice Girls", availability="All Week", in_person=True, rate=3)
    answer3= Answer(user_id=3, about="They call me Bam Bam", weight_class='Heavyweight', reach=75, professional_level='Professional', current_record='13-0-0', fav_rocky_fighter="Apollo Creed", vaccinated=True, nickname="Bam bam", walkout_song="'Eye of the Tiger' by Survivor", pets="Dogs", availability="Weekends", in_person=True)
    answer3= Answer(user_id=3, about="You are not prepared.", weight_class="Women's Bantamweight", reach=68, professional_level='Professional', current_record='12-2-0', fav_rocky_fighter="Rocky Balboa", vaccinated=True, nickname="Rowdy", has_kids=True, walkout_song="'Bad Reputation' by Joan Jett", availability="Weekends", in_person=True, rate=45)
    answer4= Answer(user_id=4, about="Fight with the best, lose with the rest.", weight_class="Women's Bantamweight", reach=69, professional_level='Professional', current_record='21-4-0', previous_titles="Women's Bantamweight", vaccinated=True, nickname="The Lionness", has_kids=True, walkout_song="'Champion' by Carrie Underwood", availability="Weekdays", in_person=True)
    answer5= Answer(user_id=5, about="I have legs for days", weight_class='Middleweight', reach=80, professional_level='Professional', current_record='21-1-0', previous_titles="Middleweight", fav_rocky_fighter="Apollo Creed", vaccinated=False, nickname="The Last Stylebender", pets="Dogs", availability="Weekdays", in_person=True)
    answer6= Answer(user_id=6, about="I'm on another level", weight_class='Lightweight', reach=76, professional_level='Professional', current_record='21-13-0', vaccinated=True, availability="All Week", in_person=False)
    answer7= Answer(user_id=7, about="If you have a dream, don’t just sit there.",weight_class='Heavyweight', reach=65, professional_level='Amateur', previous_titles="President of the UFC", fav_rocky_fighter="Rocky Balboa", vaccinated=False, availability="All Week", in_person=False, rate=15000)
    answer8= Answer(user_id=8, about="When the going gets tough, put one foot in front of the other and just keep going.",weight_class='Middleweight', reach=74, professional_level='Professional', current_record='17-5-1', vaccinated=False, nickname="The Italian Dream", walkout_song="'Somewhere I Belong' by Linkin Park", availability="Weekdays", in_person=True)
    answer9= Answer(user_id=9, about="Courage doesn't always roar.",weight_class='Middleweight', reach=74, professional_level='Amateur', current_record='1-0-0', vaccinated=False, availability="Weekdays", in_person=True, rate=55)
    answer10= Answer(user_id=10, about="Success is the sum of small efforts, repeated day in and day out.",weight_class='Heavyweight', reach=160, professional_level='Amateur', current_record='0-1-0', fav_rocky_fighter="Rocky Balboa", vaccinated=True, has_kids=True, walkout_song="'The Way I Am' by Eminem", pets="Cats", availability="Weekends", in_person=True)
    answer11= Answer(user_id=11, about="It always seems impossible until it's done.", weight_class="Women's Bantamweight", reach=82, professional_level='Amateur', vaccinated=False, availability="All Week", in_person=True)
    answer12= Answer(user_id=12, about="It does not matter how slowly you go so long as you do not stop.", weight_class="Women's Flyweight", reach=66, professional_level='Professional', current_record='21-3-0', previous_titles="Women's Flyweight", vaccinated=False, nickname="Bullet", has_kids=True, walkout_song="'How To Talk' by Lil Uzi Vert", pets="Cats", availability="All Week", in_person=True)
    answer13= Answer(user_id=13, about="My strength lies solely in my tenacity.", weight_class="Women's Strawweight", reach=65, professional_level='Professional', current_record='11-4-0', fav_rocky_fighter="Rocky Balboa", vaccinated=False, nickname="Thug", availability="Weekends", in_person=False)
    answer14= Answer(user_id=14, about="How long should you try? Until.", weight_class="Women's Bantamweight", reach=68, professional_level='Professional', current_record='9-8-1', vaccinated=True, nickname="The Belizean Bruiser", availability="All Week", in_person=True)
    answer15= Answer(user_id=15, about="Don’t be discouraged. It’s often the last key in the bunch that opens the lock.", weight_class="Women's Bantamweight", reach=65, professional_level='Professional', current_record='19-7-0', fav_rocky_fighter="Rocky Balboa", vaccinated=True, nickname="Cupcake", walkout_song="'The Ecstasy of Gold' by Enniocone", pets="Iguana", availability="Weekends", in_person=True, rate=150)
    answer16= Answer(user_id=16, about="I'm on another level", weight_class="Women's Bantamweight", reach=67, professional_level='Professional', current_record='11-9-0', vaccinated=False, nickname="Rocky", availability="All Week", in_person=True)
    answer17= Answer(user_id=17, about="You just can’t beat the person who won’t give up.", weight_class="Women's Bantamweight", reach=69, professional_level='Professional', current_record='14-5-0', fav_rocky_fighter="Ivan Drago", vaccinated=False, nickname="The Preacher's Daughter", has_kids=True, pets="Whale", availability="All Week", in_person=False, rate=125)
    answer18= Answer(user_id=18, about="Lights out", weight_class="Women's Featherweight", reach=72, professional_level='Professional', current_record='11-5-0', vaccinated=True, availability="All Week", in_person=True, rate=300)
    answer19= Answer(user_id=19, about="Success is what happens after you have survived all your mistakes.",weight_class='Middleweight', reach=65, professional_level='Amateur', fav_rocky_fighter="Rocky Balboa", vaccinated=False, availability="All Week", in_person=True)
    answer20= Answer(user_id=20, about="Every master was once a disaster.", weight_class='Lightweight', reach=74, professional_level='Professional', current_record='22-6-0', vaccinated=True, nickname="The Notorious", availability="All Week", in_person=True)
    answer21= Answer(user_id=21, about="I have not failed. I've just found 10,000 ways that won't work.", weight_class='Lightweight', reach=72, professional_level='Professional', current_record='28-6-0', fav_rocky_fighter="Adonis Johnson", vaccinated=False, nickname="The Diamond", pets="Shark", availability="All Week", in_person=False)
    answer22= Answer(user_id=22, about="The supreme art of war is to subdue the enemy without fighting.", weight_class='Middleweight', reach=81, professional_level='Professional', current_record='21-7-0', fav_rocky_fighter="Rocky Balboa", vaccinated=False, nickname="The Trailblazer", pets="Cats", availability="Weekdays", in_person=True)
    answer23= Answer(user_id=23, about="If you are going through hell, keep going.", weight_class='Middleweight', reach=74, professional_level='Professional', current_record='9-4-0', fav_rocky_fighter="Ivan Drago", vaccinated=False, nickname="Baby K", availability="Weekdays", in_person=True)
    answer24= Answer(user_id=24, about="Sometimes even to live is an act of courage.", weight_class='Middleweight', reach=73, professional_level='Professional', current_record='24-5-0', fav_rocky_fighter="Adonis Johnson", vaccinated=True, nickname="Baby Reaper", pets="Dogs", availability="All Week", in_person=True)
    answer25= Answer(user_id=25, about="I am a slow walker, but I never walk back.", weight_class='Middleweight', reach=77, professional_level='Professional', current_record='22-7-0', vaccinated=False, walkout_song="'The Foggy Dew' by Father Charles O'Neill", availability="Weekends", in_person=True, rate=99)
    answer26= Answer(user_id=26, about="Never confuse a single defeat with a final defeat.", weight_class='Middleweight', reach=72, professional_level='Professional', current_record='13-1-0', fav_rocky_fighter="Rocky Balboa", vaccinated=True, nickname="The Eraser", pets="Dogs", availability="All Week", in_person=True)
    answer27= Answer(user_id=27, about="Just because you fail once doesn't mean you're gonna fail at everything.", weight_class='Heavyweight', reach=99999, professional_level='Amateur', fav_rocky_fighter="Apollo Creed", vaccinated=True, nickname="King of Monsters", availability="Weekdays", in_person=True)
    answer28= Answer(user_id=28, about="Dripping water hollows out stone, not through force but through persistence.", weight_class='Lightweight', reach=64, professional_level='Amateur', current_record='1-0-0', fav_rocky_fighter="Adonis Johnson", vaccinated=True, nickname="Magnum", availability="All Week", in_person=False, rate=100000)
    answer29= Answer(user_id=29, about="The difference between a successful person and others is not a lack of strength, not a lack of knowledge, but rather a lack in will.", weight_class="Women's Strawweight", reach=63, professional_level='Professional', current_record='21-2-0', previous_titles="Women's Strawweight", fav_rocky_fighter="Apollo Creed", vaccinated=False, availability="All Week", in_person=True, rate=500)
    answer30= Answer(user_id=30, about="I am not in danger, Skyler. I am the danger", weight_class='Lightweight', reach=64, professional_level='Amateur', current_record='1-0-0', fav_rocky_fighter="Adonis Johnson", vaccinated=True, nickname="Heisenberg", walkout_song="'Crystal Blue Persuasion' by Tommy James & The Shondells", availability="Weekends", in_person=False, rate=1000000)


    db.session.add_all([
        answer1,
        answer2,
        answer3,
        answer4,
        answer5,
        answer6,
        answer7,
        answer8,
        answer9,
        answer10,
        answer11,
        answer12,
        answer13,
        answer14,
        answer15,
        answer16,
        answer17,
        answer18,
        answer19,
        answer20,
        answer21,
        answer22,
        answer23,
        answer24,
        answer25,
        answer26,
        answer27,
        answer28,
        answer29,
        answer30,
        answer31,
        answer32,
        answer33,
        answer34,
        answer35,
        answer36,
        answer37,
        answer38,
        answer39,
        answer40,
        answer41,
        answer42,
        answer43,
        answer44,
        answer45,
        answer46,
        answer47,
        answer48,
        answer49,
        answer50,
        answer51,
        answer52,
        answer53,
        answer54,
        answer55,
        answer56,
        answer57,
        answer58,
        answer59,
        answer60,
        answer61,
        answer62,
        answer63,
        answer64,
        answer65,
        answer66,
        answer67,
        answer68,
        answer69,
        answer70,
        answer71,
        answer72,
        answer73,
        answer74,
        answer75,
        answer76,
        answer77,
        answer78,
        answer79,
        answer80,
    ])
    db.session.commit()


def undo_answers():
    db.session.execute('TRUNCATE answers RESTART IDENTITY CASCADE;')
    db.session.commit()
