from app.models import db, Answer

def seed_answers():

    answers = [
        Answer(about="Hey I'm demo user and I bet I can spar really good", weight_class='Middleweight', reach=70, professional_level='Amateur', fav_rocky_fighter="Rocky Balboa", vaccinated=True, nickname="Demo-lition", walkout_song="'Eye of the Tiger' by Survivor", availability="All Week", in_person=True),
        Answer(about="I'm that guy pal", weight_class='Heavyweight', reach=90, professional_level='Amateur', current_record='1-0-0', fav_rocky_fighter="Rocky Balboa", vaccinated=True, nickname="That guy", walkout_song="'Wannabe' by Spice Girls", availability="All Week", in_person=True, rate=3),
        Answer(about="They call me Bam Bam", weight_class='Heavyweight', reach=75, professional_level='Professional', current_record='13-0-0', fav_rocky_fighter="Apollo Creed", vaccinated=True, nickname="Bam bam", walkout_song="'Eye of the Tiger' by Survivor", pets="Dogs", availability="Weekends", in_person=True),
        Answer(about="You are not prepared.", weight_class="Women's Bantamweight", reach=68, professional_level='Professional', current_record='12-2-0', fav_rocky_fighter="Rocky Balboa", vaccinated=True, nickname="Rowdy", has_kids=True, walkout_song="'Bad Reputation' by Joan Jett", availability="Weekends", in_person=True, rate=45),
        Answer(about="Fight with the best, lose with the rest.", weight_class="Women's Bantamweight", reach=69, professional_level='Professional', current_record='21-4-0', previous_titles="Women's Bantamweight", vaccinated=True, nickname="The Lionness", has_kids=True, walkout_song="'Champion' by Carrie Underwood", availability="Weekdays", in_person=True),
        Answer(about="I have legs for days", weight_class='Middleweight', reach=80, professional_level='Professional', current_record='21-1-0', previous_titles="Middleweight", fav_rocky_fighter="Apollo Creed", vaccinated=False, nickname="The Last Stylebender", pets="Dogs", availability="Weekdays", in_person=True),
        Answer(about="I'm on another level", weight_class='Lightweight', reach=76, professional_level='Professional', current_record='21-13-0', vaccinated=True, availability="All Week", in_person=False),
        Answer(about="If you have a dream, don’t just sit there.",weight_class='Heavyweight', reach=65, professional_level='Amateur', previous_titles="President of the UFC", fav_rocky_fighter="Rocky Balboa", vaccinated=False, availability="All Week", in_person=False, rate=15000),
        Answer(about="When the going gets tough, put one foot in front of the other and just keep going.",weight_class='Middleweight', reach=74, professional_level='Professional', current_record='17-5-1', vaccinated=False, nickname="The Italian Dream", walkout_song="'Somewhere I Belong' by Linkin Park", availability="Weekdays", in_person=True),
        Answer(about="Courage doesn't always roar.",weight_class='Middleweight', reach=74, professional_level='Amateur', current_record='1-0-0', vaccinated=False, availability="Weekdays", in_person=True, rate=55),
        Answer(about="Success is the sum of small efforts, repeated day in and day out.",weight_class='Heavyweight', reach=160, professional_level='Amateur', current_record='0-1-0', fav_rocky_fighter="Rocky Balboa", vaccinated=True, has_kids=True, walkout_song="'The Way I Am' by Eminem", pets="Cats", availability="Weekends", in_person=True),
        Answer(about="It always seems impossible until it's done.", weight_class="Women's Bantamweight", reach=82, professional_level='Amateur', vaccinated=False, availability="All Week", in_person=True),
        Answer(about="It does not matter how slowly you go so long as you do not stop.", weight_class="Women's Flyweight", reach=66, professional_level='Professional', current_record='21-3-0', previous_titles="Women's Flyweight", vaccinated=False, nickname="Bullet", has_kids=True, walkout_song="'How To Talk' by Lil Uzi Vert", pets="Cats", availability="All Week", in_person=True),
        Answer(about="My strength lies solely in my tenacity.", weight_class="Women's Strawweight", reach=65, professional_level='Professional', current_record='11-4-0', fav_rocky_fighter="Rocky Balboa", vaccinated=False, nickname="Thug", availability="Weekends", in_person=False),
        Answer(about="How long should you try? Until.", weight_class="Women's Bantamweight", reach=68, professional_level='Professional', current_record='9-8-1', vaccinated=True, nickname="The Belizean Bruiser", availability="All Week", in_person=True),
        Answer(about="Don’t be discouraged. It’s often the last key in the bunch that opens the lock.", weight_class="Women's Bantamweight", reach=65, professional_level='Professional', current_record='19-7-0', fav_rocky_fighter="Rocky Balboa", vaccinated=True, nickname="Cupcake", walkout_song="'The Ecstasy of Gold' by Enniocone", pets="Iguana", availability="Weekends", in_person=True, rate=150),
        Answer(about="I'm on another level", weight_class="Women's Bantamweight", reach=67, professional_level='Professional', current_record='11-9-0', vaccinated=False, nickname="Rocky", availability="All Week", in_person=True),
        Answer(about="You just can’t beat the person who won’t give up.", weight_class="Women's Bantamweight", reach=69, professional_level='Professional', current_record='14-5-0', fav_rocky_fighter="Ivan Drago", vaccinated=False, nickname="The Preacher's Daughter", has_kids=True, pets="Whale", availability="All Week", in_person=False, rate=125),
        Answer(about="Lights out", weight_class="Women's Featherweight", reach=72, professional_level='Professional', current_record='11-5-0', vaccinated=True, availability="All Week", in_person=True, rate=300),
        Answer(about="Success is what happens after you have survived all your mistakes.",weight_class='Middleweight', reach=65, professional_level='Amateur', fav_rocky_fighter="Rocky Balboa", vaccinated=False, availability="All Week", in_person=True),
        Answer(about="Every master was once a disaster.", weight_class='Lightweight', reach=74, professional_level='Professional', current_record='22-6-0', vaccinated=True, nickname="The Notorious", availability="All Week", in_person=True),
        Answer(about="I have not failed. I've just found 10,000 ways that won't work.", weight_class='Lightweight', reach=72, professional_level='Professional', current_record='28-6-0', fav_rocky_fighter="Adonis Johnson", vaccinated=False, nickname="The Diamond", pets="Shark", availability="All Week", in_person=False),
        Answer(about="The supreme art of war is to subdue the enemy without fighting.", weight_class='Middleweight', reach=81, professional_level='Professional', current_record='21-7-0', fav_rocky_fighter="Rocky Balboa", vaccinated=False, nickname="The Trailblazer", pets="Cats", availability="Weekdays", in_person=True),
        Answer(about="If you are going through hell, keep going.", weight_class='Middleweight', reach=74, professional_level='Professional', current_record='9-4-0', fav_rocky_fighter="Ivan Drago", vaccinated=False, nickname="Baby K", availability="Weekdays", in_person=True),
        Answer(about="Sometimes even to live is an act of courage.", weight_class='Middleweight', reach=73, professional_level='Professional', current_record='24-5-0', fav_rocky_fighter="Adonis Johnson", vaccinated=True, nickname="Baby Reaper", pets="Dogs", availability="All Week", in_person=True),
        Answer(about="I am a slow walker, but I never walk back.", weight_class='Middleweight', reach=77, professional_level='Professional', current_record='22-7-0', vaccinated=False, walkout_song="'The Foggy Dew' by Father Charles O'Neill", availability="Weekends", in_person=True, rate=99),
        Answer(about="Never confuse a single defeat with a final defeat.", weight_class='Middleweight', reach=72, professional_level='Professional', current_record='13-1-0', fav_rocky_fighter="Rocky Balboa", vaccinated=True, nickname="The Eraser", pets="Dogs", availability="All Week", in_person=True),
        Answer(about="Just because you fail once doesn't mean you're gonna fail at everything.", weight_class='Heavyweight', reach=99999, professional_level='Amateur', fav_rocky_fighter="Apollo Creed", vaccinated=True, nickname="King of Monsters", availability="Weekdays", in_person=True),
        Answer(about="Dripping water hollows out stone, not through force but through persistence.", weight_class='Lightweight', reach=64, professional_level='Amateur', current_record='1-0-0', fav_rocky_fighter="Adonis Johnson", vaccinated=True, nickname="Magnum", availability="All Week", in_person=False, rate=100000),
        Answer(about="The difference between a successful person and others is not a lack of strength, not a lack of knowledge, but rather a lack in will.", weight_class="Women's Strawweight", reach=63, professional_level='Professional', current_record='21-2-0', previous_titles="Women's Strawweight", fav_rocky_fighter="Apollo Creed", vaccinated=False, availability="All Week", in_person=True, rate=500),
        Answer(about="I am not in danger, Skyler. I am the danger", weight_class='Lightweight', reach=64, professional_level='Amateur', current_record='1-0-0', fav_rocky_fighter="Adonis Johnson", vaccinated=True, nickname="Heisenberg", walkout_song="'Crystal Blue Persuasion' by Tommy James & The Shondells", availability="Weekends", in_person=False, rate=1000000)
        ]











    db.bulk_save_objects(answers)
    db.session.commit()



def undo_answers():
    db.session.execute('TRUNCATE answers RESTART IDENTITY CASCADE;')
    db.session.commit()
