from app.models import db, Answer

def seed_answers():

    answers = [
        Answer(about="Hey I'm demo user and I bet I can spar really good", weight_class='Middleweight', reach=70, professional_level='Amateur'),
        Answer(about="I'm that guy pal", weight_class='Heavyweight', reach=90, professional_level='Amateur', current_record='1-0-0'),
        Answer(about="They call me Bam Bam", weight_class='Heavyweight', reach=75, professional_level='Professional', current_record='13-0-0'),
        Answer(about="You are not prepared.", weight_class="Women's Bantamweight", reach=68, professional_level='Professional', current_record='12-2-0'),
        Answer(about="Fight with the best, lose with the rest.", weight_class="Women's Bantamweight", reach=69, professional_level='Professional', current_record='21-4-0'),
        Answer(about="I have legs for days", weight_class='Middleweight', reach=80, professional_level='Professional', current_record='21-1-0'),
        Answer(about="I'm on another level", weight_class='Lightweight', reach=76, professional_level='Professional', current_record='21-13-0'),
        Answer(about="If you have a dream, don’t just sit there.",weight_class='Heavyweight', reach=65, professional_level='Amateur'),
        Answer(about="When the going gets tough, put one foot in front of the other and just keep going.",weight_class='Middleweight', reach=74, professional_level='Professional', current_record='17-5-1'),
        Answer(about="Courage doesn't always roar.",weight_class='Middleweight', reach=74, professional_level='Amateur', current_record='1-0-0'),
        Answer(about="Success is the sum of small efforts, repeated day in and day out.",weight_class='Heavyweight', reach=160, professional_level='Amateur', current_record='0-1-0'),
        Answer(about="It always seems impossible until it's done.", weight_class="Women's Bantamweight", reach=82, professional_level='Amateur'),
        Answer(about="It does not matter how slowly you go so long as you do not stop.", weight_class="Women's Flyweight", reach=66, professional_level='Professional', current_record='21-3-0'),
        Answer(about="My strength lies solely in my tenacity.", weight_class="Women's Strawweight", reach=65, professional_level='Professional', current_record='11-4-0'),
        Answer(about="How long should you try? Until.", weight_class="Women's Bantamweight", reach=68, professional_level='Professional', current_record='9-8-1'),
        Answer(about="Don’t be discouraged. It’s often the last key in the bunch that opens the lock.", weight_class="Women's Bantamweight", reach=65, professional_level='Professional', current_record='19-7-0'),
        Answer(about="I'm on another level", weight_class="Women's Bantamweight", reach=67, professional_level='Professional', current_record='11-9-0'),
        Answer(about="You just can’t beat the person who won’t give up.", weight_class="Women's Bantamweight", reach=69, professional_level='Professional', current_record='14-5-0'),
        Answer(about="Lights out", weight_class="Women's Featherweight", reach=72, professional_level='Professional', current_record='11-5-0'),
        Answer(about="Success is what happens after you have survived all your mistakes.",weight_class='Middleweight', reach=65, professional_level='Amateur'),
        Answer(about="Every master was once a disaster.", weight_class='Lightweight', reach=74, professional_level='Professional', current_record='22-6-0'),
        Answer(about="I have not failed. I've just found 10,000 ways that won't work.", weight_class='Lightweight', reach=72, professional_level='Professional', current_record='28-6-0'),
        Answer(about="The supreme art of war is to subdue the enemy without fighting.", weight_class='Middleweight', reach=81, professional_level='Professional', current_record='21-7-0'),
        Answer(about="If you are going through hell, keep going.", weight_class='Middleweight', reach=74, professional_level='Professional', current_record='9-4-0'),
        Answer(about="Sometimes even to live is an act of courage.", weight_class='Middleweight', reach=73, professional_level='Professional', current_record='24-5-0'),
        Answer(about="I am a slow walker, but I never walk back.", weight_class='Middleweight', reach=77, professional_level='Professional', current_record='22-7-0'),
        Answer(about="Never confuse a single defeat with a final defeat.", weight_class='Middleweight', reach=72, professional_level='Professional', current_record='13-1-0'),
        Answer(about="Just because you fail once doesn't mean you're gonna fail at everything.", weight_class='Heavyweight', reach=99999, professional_level='Amateur'),
        Answer(about="Dripping water hollows out stone, not through force but through persistence.", weight_class="Women's Strawweight", reach=63, professional_level='Professional', current_record='21-2-0'),
        Answer(about="The difference between a successful person and others is not a lack of strength, not a lack of knowledge, but rather a lack in will.", weight_class='Lightweight', reach=64, professional_level='Amateur', current_record='1-0-0'),
        Answer(about="I am not in danger, Skyler. I am the danger")
        ]











    db.bulk_save_objects(answers)
    db.session.commit()



def undo_answers():
    db.session.execute('TRUNCATE answers RESTART IDENTITY CASCADE;')
    db.session.commit()
