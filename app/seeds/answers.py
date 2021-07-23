from app.models import db, Answer

def seed_answers():

    answer1= Answer(user_id=1, about="Hey I'm demo user and I bet I can spar really good", weight_class=1, reach=70, professional_level=0, fav_rocky_fighter="Rocky Balboa", vaccinated=True, nickname="Demo-lition", walkout_song="'Eye of the Tiger' by Survivor", availability=2, in_person=True)
    answer2= Answer(user_id=2, about="I'm that guy pal", weight_class=2, reach=90, professional_level=1, current_record='1-0-0', fav_rocky_fighter="Rocky Balboa", vaccinated=True, nickname="That guy", walkout_song="'Wannabe' by Spice Girls", availability=2, in_person=True, rate=3)
    answer3= Answer(user_id=3, about="They call me Bam Bam", weight_class=2, reach=75, professional_level=2, current_record='13-0-0', fav_rocky_fighter="Apollo Creed", vaccinated=True, nickname="Bam bam", walkout_song="'Eye of the Tiger' by Survivor", pets="Dogs", availability=0, in_person=True)
    answer3= Answer(user_id=3, about="You are not prepared.", weight_class=6, reach=68, professional_level=2, current_record='12-2-0', fav_rocky_fighter="Rocky Balboa", vaccinated=True, nickname="Rowdy", has_kids=True, walkout_song="'Bad Reputation' by Joan Jett", availability=0, in_person=True, rate=45)
    answer4= Answer(user_id=4, about="Fight with the best, lose with the rest.", weight_class=6, reach=69, professional_level=2, current_record='21-4-0', previous_titles=6, vaccinated=True, nickname="The Lionness", has_kids=True, walkout_song="'Champion' by Carrie Underwood", availability=1, in_person=True)
    answer5= Answer(user_id=5, about="I have legs for days", weight_class=1, reach=80, professional_level=2, current_record='21-1-0', previous_titles="Middleweight", fav_rocky_fighter="Apollo Creed", vaccinated=False, nickname="The Last Stylebender", pets="Dogs", availability=1, in_person=True)
    answer6= Answer(user_id=6, about="I'm on another level", weight_class=0, reach=76, professional_level=2, current_record='21-13-0', vaccinated=True, availability=2, in_person=False)
    answer7= Answer(user_id=7, about="If you have a dream, don’t just sit there.",weight_class=2, reach=65, professional_level=1, previous_titles="President of the UFC", fav_rocky_fighter="Rocky Balboa", vaccinated=False, availability=2, in_person=False, rate=15000)
    answer8= Answer(user_id=8, about="When the going gets tough, put one foot in front of the other and just keep going.",weight_class=1, reach=74, professional_level=2, current_record='17-5-1', vaccinated=False, nickname="The Italian Dream", walkout_song="'Somewhere I Belong' by Linkin Park", availability=1, in_person=True)
    answer9= Answer(user_id=9, about="Courage doesn't always roar.",weight_class=1, reach=74, professional_level=1, current_record='1-0-0', vaccinated=False, availability=1, in_person=True, rate=55)
    answer10= Answer(user_id=10, about="Success is the sum of small efforts, repeated day in and day out.",weight_class=2, reach=160, professional_level=1, current_record='0-1-0', fav_rocky_fighter="Rocky Balboa", vaccinated=True, has_kids=True, walkout_song="'The Way I Am' by Eminem", pets="Cats", availability=0, in_person=True)
    answer11= Answer(user_id=11, about="It always seems impossible until it's done.", weight_class=6, reach=82, professional_level=0, vaccinated=False, availability=2, in_person=True)
    answer12= Answer(user_id=12, about="It does not matter how slowly you go so long as you do not stop.", weight_class=3, reach=66, professional_level=2, current_record='21-3-0', previous_titles=3, vaccinated=False, nickname="Bullet", has_kids=True, walkout_song="'How To Talk' by Lil Uzi Vert", pets="Cats", availability=2, in_person=True)
    answer13= Answer(user_id=13, about="My strength lies solely in my tenacity.", weight_class=3, reach=65, professional_level=2, current_record='11-4-0', fav_rocky_fighter="Rocky Balboa", vaccinated=False, nickname="Thug", availability=0, in_person=False)
    answer14= Answer(user_id=14, about="How long should you try? Until.", weight_class=6, reach=68, professional_level=2, current_record='9-8-1', vaccinated=True, nickname="The Belizean Bruiser", availability=2, in_person=True)
    answer15= Answer(user_id=15, about="Don’t be discouraged. It’s often the last key in the bunch that opens the lock.", weight_class=6, reach=65, professional_level=2, current_record='19-7-0', fav_rocky_fighter="Rocky Balboa", vaccinated=True, nickname="Cupcake", walkout_song="'The Ecstasy of Gold' by Enniocone", pets="Iguana", availability=0, in_person=True, rate=150)
    answer16= Answer(user_id=16, about="I'm on another level", weight_class=6, reach=67, professional_level=2, current_record='11-9-0', vaccinated=False, nickname="Rocky", availability=2, in_person=True)
    answer17= Answer(user_id=17, about="You just can’t beat the person who won’t give up.", weight_class=6, reach=69, professional_level=2, current_record='14-5-0', fav_rocky_fighter="Ivan Drago", vaccinated=False, nickname="The Preacher's Daughter", has_kids=True, pets="Whale", availability=2, in_person=False, rate=125)
    answer18= Answer(user_id=18, about="Lights out", weight_class=4, reach=72, professional_level=2, current_record='11-5-0', vaccinated=True, availability=2, in_person=True, rate=300)
    answer19= Answer(user_id=19, about="Success is what happens after you have survived all your mistakes.",weight_class=1, reach=65, professional_level=0, fav_rocky_fighter="Rocky Balboa", vaccinated=False, availability=2, in_person=True)
    answer20= Answer(user_id=20, about="Every master was once a disaster.", weight_class=0, reach=74, professional_level=2, current_record='22-6-0', vaccinated=True, nickname="The Notorious", availability=2, in_person=True)
    answer21= Answer(user_id=21, about="I have not failed. I've just found 10,000 ways that won't work.", weight_class=0, reach=72, professional_level=2, current_record='28-6-0', fav_rocky_fighter="Adonis Johnson", vaccinated=False, nickname="The Diamond", pets="Shark", availability=2, in_person=False)
    answer22= Answer(user_id=22, about="The supreme art of war is to subdue the enemy without fighting.", weight_class=1, reach=81, professional_level=2, current_record='21-7-0', fav_rocky_fighter="Rocky Balboa", vaccinated=False, nickname="The Trailblazer", pets="Cats", availability=1, in_person=True)
    answer23= Answer(user_id=23, about="If you are going through hell, keep going.", weight_class=1, reach=74, professional_level=2, current_record='9-4-0', fav_rocky_fighter="Ivan Drago", vaccinated=False, nickname="Baby K", availability=1, in_person=True)
    answer24= Answer(user_id=24, about="Sometimes even to live is an act of courage.", weight_class=1, reach=73, professional_level=2, current_record='24-5-0', fav_rocky_fighter="Adonis Johnson", vaccinated=True, nickname="Baby Reaper", pets="Dogs", availability=2, in_person=True)
    answer25= Answer(user_id=25, about="I am a slow walker, but I never walk back.", weight_class=1, reach=77, professional_level=2, current_record='22-7-0', vaccinated=False, walkout_song="'The Foggy Dew' by Father Charles O'Neill", availability=0, in_person=True, rate=99)
    answer26= Answer(user_id=26, about="Never confuse a single defeat with a final defeat.", weight_class=1, reach=72, professional_level=2, current_record='13-1-0', fav_rocky_fighter="Rocky Balboa", vaccinated=True, nickname="The Eraser", pets="Dogs", availability=2, in_person=True)
    answer27= Answer(user_id=27, about="Just because you fail once doesn't mean you're gonna fail at everything.", weight_class=2, reach=99999, professional_level=1, fav_rocky_fighter="Apollo Creed", vaccinated=True, nickname="King of Monsters", availability=1, in_person=True)
    answer28= Answer(user_id=28, about="Dripping water hollows out stone, not through force but through persistence.", weight_class=0, reach=64, professional_level=1, current_record='1-0-0', fav_rocky_fighter="Adonis Johnson", vaccinated=True, nickname="Magnum", availability=2, in_person=False, rate=100000)
    answer29= Answer(user_id=29, about="The difference between a successful person and others is not a lack of strength, not a lack of knowledge, but rather a lack in will.", weight_class=3, reach=63, professional_level=2, current_record='21-2-0', previous_titles=3, fav_rocky_fighter="Apollo Creed", vaccinated=False, availability=2, in_person=True, rate=500)
    answer30= Answer(user_id=30, about="I am not in danger, Skyler. I am the danger", weight_class=0, reach=64, professional_level=1, current_record='1-0-0', fav_rocky_fighter="Adonis Johnson", vaccinated=True, nickname="Heisenberg", walkout_song="'Crystal Blue Persuasion' by Tommy James & The Shondells", availability=0, in_person=False, rate=1000000)
    answer31= Answer(
        user_id=31, about="They call me Hummus", weight_class=1, reach=55,
        professional_level=0, fav_rocky_fighter="Apollo Creed", vaccinated=True,
        nickname="Joey B", walkout_song="'Boyfriend' by Justin Bieber", availability=1,
        has_kids=False, religion='Atheist', pets='Justin', rate=200, in_person=True)

    answer32= Answer(
        user_id=32, about="Big Dawg is Big Chillin", weight_class=2, reach=56,
        professional_level=1, fav_rocky_fighter="Ivan Drago", vaccinated=False,
        nickname="Drake", walkout_song="'Beauty And A Beat' by Justin Bieber", availability=2,
        has_kids=True, religion='Hindu', pets='Bieber', rate=100, in_person=False)

    answer33= Answer(
        user_id=33, about="I eat hummus for breakfast.", weight_class=3, reach=57,
        professional_level=2, fav_rocky_fighter="Rocky Balboa", vaccinated=True,
        nickname="Yeezy", walkout_song="'Sweatpants' by Childish Gambino", availability=1,
        has_kids=False, religion='Hindu', pets='Iron Man', rate=20, in_person=True)

    answer34= Answer(
        user_id=34, about="I am a pacifist honestly.", weight_class=4, reach=58,
        professional_level=0, fav_rocky_fighter="Ivan Drago", vaccinated=False,
        nickname="Childish", walkout_song="'3005' by Childish Gambino", availability=2,
        has_kids=True, religion='Atheist', pets='Vitamin B12', rate=10, in_person=False)

    answer35= Answer(
        user_id=35, about="My mind is wandering and my fists are clobbering", weight_class=5, reach=59,
        professional_level=1, fav_rocky_fighter="Apollo Creed", vaccinated=True,
        nickname="Chance", walkout_song="'Chanel' by Frank Ocean", availability=1,
        has_kids=True, religion='Roman Catholic', pets='Childish', rate=1, in_person=True)

    answer36= Answer(
        user_id=36, about="I regret nothing", weight_class=6, reach=60,
        professional_level=1, fav_rocky_fighter="Ivan Drago", vaccinated=True,
        nickname="Hermione", walkout_song="'No Problem' by Chance The Rapper", availability=2,
        has_kids=False, religion='Muslim', pets='Chance', rate=25, in_person=False)

    answer37= Answer(
        user_id=37, about="Whoever fights monsters should see to it that in the process he does not become a monster.", weight_class=0, reach=61,
        professional_level=2, fav_rocky_fighter="Rocky Balboa", vaccinated=False,
        nickname="Dorito", walkout_song="'Last Time That I Checc'd' by Nipsey Hussle", availability=0,
        has_kids=True, religion='Atheist', pets='Nip', rate=50, in_person=True)

    answer38= Answer(
        user_id=38, about="Nobody can hurt me without my permission.", weight_class=1, reach=62,
        professional_level=2, fav_rocky_fighter="Ivan Drago", vaccinated=False,
        nickname="Champ", walkout_song="'FDT' by YG", availability=0,
        has_kids=False, religion='Muslim', pets='T-Bone', rate=50, in_person=False)
    answer39= Answer(
        user_id=39, about="Older men declare war. But it is youth that must fight and die.", weight_class=2, reach=63,
        professional_level=1, fav_rocky_fighter="Apollo Creed", vaccinated=True,
        nickname="Coke Zero", walkout_song="'I Just Wanna Party' by YG", availability=2,
        has_kids=True, religion='Hindu', pets='Woman', rate=50, in_person=True)



    answer40= Answer(
        user_id=40, about="We are twice armed if we fight with faith.", weight_class=3, reach=64,
        professional_level=1, fav_rocky_fighter="Ivan Drago", vaccinated=True,
        nickname="Cricket", walkout_song="'Toot It and Boot It' by YG", availability=1,
        has_kids=False, religion='Hindu', pets='Man', rate=1000, in_person=False)

    answer41= Answer(
        user_id=41, about="That's how winning is done.", weight_class=4, reach=65,
        professional_level=2, fav_rocky_fighter="Adonis Johnson", vaccinated=True,
        nickname="Twix", walkout_song="'Stay With Me' by Sam Smith", availability=0,
        has_kids=True, religion='Roman Catholic', pets='YG', rate=5000, in_person=True)



    answer42= Answer(
        user_id=42, about="Cue up the Rocky Song", weight_class=5, reach=66,
        professional_level=1, fav_rocky_fighter="Ivan Drago", vaccinated=True,
        nickname="Cherry", walkout_song="'WAP' by Cardi B", availability=2,
        has_kids=True, religion='Hindu', pets='Sparky The Dog', rate=5050, in_person=False)

    answer43= Answer(
        user_id=43, about="Fights begin and end with handshakes.", weight_class=6, reach=66,
        professional_level=1, fav_rocky_fighter="Apollo Creed", vaccinated=True,
        nickname="Cloud", walkout_song="'Redbone' by Childish Gambino", availability=2,
        has_kids=False, religion='Atheist', pets='10 Sharks', rate=50, in_person=True)

    answer44= Answer(
        user_id=44, about="You will never be entirely comfortable.", weight_class=0, reach=67,
        professional_level=2, fav_rocky_fighter="Rocky Balboa", vaccinated=False,
        nickname="Knucklebutt", walkout_song="'Scorpion' by Drake", availability=2,
        has_kids=True, religion='Muslim', pets='DogCat', rate=10, in_person=False)

    answer45= Answer(
        user_id=45, about="There was no such thing as a fair fight.", weight_class=0, reach=67,
        professional_level=1, fav_rocky_fighter="Rocky Balboa", vaccinated=True,
        nickname="Pinata", walkout_song="'Marvin's Room' by Drake", availability=2,
        has_kids=False, religion='Muslim', pets='CatDog', rate=10, in_person=True)

    answer46= Answer(
        user_id=46, about="Everyone has a plan until they’ve been hit.", weight_class=1, reach=67,
        professional_level=1, fav_rocky_fighter="Rocky Balboa", vaccinated=True,
        nickname="The King", walkout_song="'What's My Age Again?' by Blink-182", availability=1,
        has_kids=True, religion='Atheist', pets='Kyedae', rate=10, in_person=False)

    answer47= Answer(
        user_id=47, about="He who hesitates, meditates in a horizontal position.", weight_class=1, reach=68,
        professional_level=0, fav_rocky_fighter="Ivan Drago", vaccinated=False,
        nickname="Big Nasty", walkout_song="'All The Small Things' by Blink-182", availability=2,
        has_kids=False, religion='Buddhist', pets='Spar', rate=500, in_person=False)

    answer48= Answer(
        user_id=48, about="You may have to fight a battle more than once to win it.", weight_class=2, reach=68,
        professional_level=1, fav_rocky_fighter="Apollo Creed", vaccinated=True,
        nickname="Joker", walkout_song="'Love Me Harder' by Ariana Grande", availability=1,
        has_kids=True, religion='Hindu', pets='5 Cats', rate=500, in_person=True)

    answer49= Answer(
        user_id=49, about="I will never reach perfection.", weight_class=2, reach=69,
        professional_level=1, fav_rocky_fighter="Rocky Balboa", vaccinated=False,
        nickname="Snickerdoodle", walkout_song="'Starships' by Nicki Minaj", availability=2,
        has_kids=True, religion='Roman Catholic', pets='Golfwang', rate=500, in_person=False)

    answer50= Answer(
        user_id=50, about="You have no fear.", weight_class=3, reach=69,
        professional_level=2, fav_rocky_fighter="Ivan Drago", vaccinated=True,
        nickname="Gingersnap", walkout_song="'Monsters' by Kanye West", availability=2,
        has_kids=False, religion='Muslim', pets='Taco', rate=500, in_person=True)

    answer51= Answer(
        user_id=51, about="There’s three things in life that excite me: a woman, dinosaurs, and the violence of the Octagon.", weight_class=3, reach=70,
        professional_level=2, fav_rocky_fighter="Rocky Balboa", vaccinated=True,
        nickname="Rainbow", walkout_song="'Blood on the Leaves' by Kanye West", availability=1,
        has_kids=True, religion='Roman Catholic', pets='Gata', rate=500, in_person=False)

    answer52= Answer(
        user_id=52, about="I want to outlive my children.", weight_class=4, reach=70,
        professional_level=2, fav_rocky_fighter="Ivan Drago", vaccinated=True,
        nickname="Mouse", walkout_song="'Professional Rapper' by Lil Dicky", availability=2,
        has_kids=False, religion='Christian', pets='Dave Burd', rate=300, in_person=False)

    answer53= Answer(
        user_id=53, about="They took headbutts away so I had to learn some skills.", weight_class=4, reach=71,
        professional_level=1, fav_rocky_fighter="Rocky Balboa", vaccinated=True,
        nickname="Pickle", walkout_song="'WAWA' by Party Favor", availability=1,
        has_kids=True, religion='Roman Catholic', pets='Sparkz the Second', rate=300, in_person=True)

    answer54= Answer(
        user_id=54, about="Success is not final, failure is not fatal", weight_class=4, reach=72,
        professional_level=1, fav_rocky_fighter="Rocky Balboa", vaccinated=False,
        nickname="Con", walkout_song="'Runaway' by Galantis", availability=2,
        has_kids=False, religion='Hindu', pets='Klawhi', rate=20, in_person=False)

    answer55= Answer(
        user_id=55, about="Never bend your head. Always hold it high. ", weight_class=5, reach=73,
        professional_level=1, fav_rocky_fighter="Adonis Johnson", vaccinated=False,
        nickname="Green Giant", walkout_song="'NASA' by Ariana Grande", availability=1,
        has_kids=False, religion='Christian', pets='The Brow', rate=20, in_person=True)

    answer56= Answer(
        user_id=56, about="What you get by achieving your goals is not as important as what you become by achieving your goals.", weight_class=5, reach=74,
        professional_level=0, fav_rocky_fighter="Rocky Balboa", vaccinated=True,
        nickname="Mad Max", walkout_song="'34+35' by Ariana Grande", availability=2,
        has_kids=True, religion='Hindu', pets='King James', rate=500, in_person=False)

    answer57= Answer(
        user_id=57, about="Believe you can and you're halfway there.", weight_class=5, reach=75,
        professional_level=0, fav_rocky_fighter="Ivan Drago", vaccinated=False,
        nickname="Amethyst", walkout_song="'Break Free' by Ariana Grande", availability=2,
        has_kids=True, religion='Roman Catholic', pets='Jisoo', rate=500, in_person=True)

    answer58= Answer(
        user_id=58, about="When you have a dream, you've got to grab it and never let go.", weight_class=6, reach=76,
        professional_level=1, fav_rocky_fighter="Rocky Balboa", vaccinated=True,
        nickname="Bub", walkout_song="'That Should Be Me' by Justin Bieber", availability=0,
        has_kids=True, religion='Jewish', pets='Rose', rate=20, in_person=False)



    answer59= Answer(
        user_id=59, about="I can't change the direction of the wind, but I can adjust my sails to always reach my destination.", weight_class=6, reach=77,
        professional_level=1, fav_rocky_fighter="Rocky Balboa", vaccinated=False,
        nickname="Babs", walkout_song="'Homecoming' by Kanye West", availability=2,
        has_kids=False, religion='Christian', pets='Jennie', rate=50, in_person=False)

    answer60= Answer(
        user_id=60, about="No matter what you're going through, there's a light at the end of the tunnel.", weight_class=6, reach=76,
        professional_level=0, fav_rocky_fighter="Rocky Balboa", vaccinated=False,
        nickname="Twinkie", walkout_song="'All I Want For Christmas' by Mariah Carey", availability=0,
        has_kids=True, religion='Jewish', pets='Lisa', rate=10, in_person=True)

    answer61= Answer(
        user_id=61, about="It is our attitude at the beginning of a difficult task which, more than anything else, will affect its successful outcome.", weight_class=6, reach=76,
        professional_level=2, fav_rocky_fighter="Rocky Balboa", vaccinated=True,
        nickname="Brown Sugar", walkout_song="'All I Want For Christmas' by Mariah Carey", availability=2,
        has_kids=False, religion='Roman Catholic', pets='Doja Cat', rate=500, in_person=True)



    answer62= Answer(
        user_id=62, about="Life is like riding a bicycle. To keep your balance, you must keep moving.", weight_class=1, reach=75,
        professional_level=0, fav_rocky_fighter="Rocky Balboa", vaccinated=True,
        nickname="Robin", walkout_song="'All I Want For Christmas' by Mariah Carey", availability=1,
        has_kids=True, religion='Christian', pets='Sparkz', rate=30, in_person=True)

    answer63= Answer(
        user_id=63, about="Just don't give up trying to do what you really want to do.", weight_class=1, reach=74,
        professional_level=0, fav_rocky_fighter="Rocky Balboa", vaccinated=False,
        nickname="Papito", walkout_song="'All I Want For Christmas' by Mariah Carey", availability=2,
        has_kids=False, religion='Jewish', pets='Dog and Cat', rate=500, in_person=False)

    answer64= Answer(
        user_id=64, about="Limit your 'always 'and your 'nevers.'", weight_class=2, reach=74,
        professional_level=1, fav_rocky_fighter="Rocky Balboa", vaccinated=True,
        nickname="Goldilocks", walkout_song="'Bonfire' by Childish Gambino", availability=2,
        has_kids=True, religion='Buddhist', pets='Big Bear', rate=500, in_person=True)

    answer65= Answer(
        user_id=65, about="Nothing is impossible.", weight_class=2, reach=73,
        professional_level=1, fav_rocky_fighter="Ivan Drago", vaccinated=False,
        nickname="Bebe", walkout_song="'Bounce Back' by Big Sean", availability=0,
        has_kids=True, religion='Jewish', pets='Spinal the Snake', rate=500, in_person=False)

    answer66= Answer(
        user_id=66, about="You are never too old to set another goal or to dream a new dream.", weight_class=3, reach=72,
        professional_level=2, fav_rocky_fighter="Rocky Balboa", vaccinated=True,
        nickname="MomBod", walkout_song="'Redbone' by Childish Gambino", availability=0,
        has_kids=False, religion='Roman Catholic',  rate=40, in_person=False)

    answer67= Answer(
        user_id=67, about="Try to be a rainbow in someone else's cloud.", weight_class=3, reach=70,
        professional_level=0, fav_rocky_fighter="Adonis Johnson", vaccinated=False,
        nickname="Pretty Lady", walkout_song="'Bound 2' by Kanye West", availability=2,
        has_kids=True, religion='Roman Catholic', pets='Yeezus Christ', rate=500, in_person=False)

    answer68= Answer(
        user_id=68, about="You do not find the happy life. You make it.", weight_class=3, reach=71,
        professional_level=1, fav_rocky_fighter="Rocky Balboa", vaccinated=True,
        nickname="Butternut", walkout_song="'Cocoa Butter Kisses' by Chance The Rapper", availability=1,
        has_kids=True, religion='Jewish', rate=500, in_person=True)

    answer69= Answer(
        user_id=69, about="Inspiration comes from within yourself.", weight_class=0, reach=69,
        professional_level=0, fav_rocky_fighter="Adonis Johnson", vaccinated=True,
        nickname="Lobster", walkout_song="'Redbone' by Childish Gambino", availability=1,
        has_kids=True, religion='Roman Catholic', rate=50, in_person=True)

    answer70= Answer(
        user_id=70, about="Sometimes you will never know the value of a moment, until it becomes a memory.", weight_class=0, reach=68,
        professional_level=0, fav_rocky_fighter="Rocky Balboa", vaccinated=True,
        nickname="Schnookums", walkout_song="'Molly' by Lil Dicky", availability=1,
        has_kids=True, religion='Buddhist', pets='Lovebug', rate=50000, in_person=False)

    answer71= Answer(
        user_id=71, about="The most wasted of days is one without laughter.", weight_class=0, reach=67,
        professional_level=2, fav_rocky_fighter="Adonis Johnson", vaccinated=False,
        nickname="Buds", walkout_song="'Panda' by Desiigner", availability=2,
        has_kids=False, religion='Jewish', pets='Cheesy', rate=30, in_person=True)



    answer72= Answer(
        user_id=72, about="You must do the things you think you cannot do.", weight_class=4, reach=66,
        professional_level=2, fav_rocky_fighter="Rocky Balboa", vaccinated=True,
        nickname="Diesel", walkout_song="'Congratulations' by Post Malone", availability=2,
        has_kids=True, religion='Roman Catholic', rate=50000, in_person=False)

    answer73= Answer(
        user_id=73, about="It isn't where you came from. It's where you're going that counts.", weight_class=3, reach=65,
        professional_level=0, fav_rocky_fighter="Adonis Johnson", vaccinated=True,
        nickname="Chewbacca", walkout_song="'Freaks and Geeks' by Childish Gambino", availability=2,
        has_kids=False, religion='Roman Catholic', pets='Sparky The Dog', rate=50000, in_person=True)

    answer74= Answer(
        user_id=74, about="It is never too late to be what you might have been.", weight_class=3, reach=64,
        professional_level=1, fav_rocky_fighter="Rocky Balboa", vaccinated=False,
        nickname="Cheeky", walkout_song="'Feels Like Summer' by Childish Gambino", availability=1,
        has_kids=True, religion='Roman Catholic', pets='Sparky The Dog', rate=500, in_person=True)

    answer75= Answer(
        user_id=75, about="Stay close to anything that makes you glad you are alive.", weight_class=5, reach=64,
        professional_level=1, fav_rocky_fighter="Adonis Johnson", vaccinated=True,
        nickname="Gordo", walkout_song="'My Own Thing' by Chance The Rapper", availability=0,
        has_kids=False, religion='Jewish',rate=500, in_person=False)

    answer76= Answer(
        user_id=76, about="You get what you give.", weight_class=5, reach=65,
        professional_level=2, fav_rocky_fighter="Rocky Balboa", vaccinated=True,
        nickname="Ghoulie", walkout_song="'Pretty Savage' by BLACKPINK", availability=0,
        has_kids=True, religion='Roman Catholic', rate=10, in_person=True)

    answer77= Answer(
        user_id=77, about="Some people look for a beautiful place. Others make a place beautiful.", weight_class=6, reach=66,
        professional_level=2, fav_rocky_fighter="Adonis Johnson", vaccinated=False,
        nickname="Ace", walkout_song="'Lovesick Girls' by BLACKPINK", availability=0,
        has_kids=False, religion='Roman Catholic', pets='Sparky The Dog', rate=25, in_person=False)

    answer78= Answer(
        user_id=78, about="Happiness often sneaks in through a door you didn't know you left open.", weight_class=6, reach=67,
        professional_level=2, fav_rocky_fighter="Rocky Balboa", vaccinated=True,
        nickname="Toots", walkout_song="'Hometown Girl' by ZHU", availability=1,
        has_kids=True, religion='Buddhist', pets='Ssssebastian the Snake', rate=25, in_person=True)

    answer79= Answer(
        user_id=79, about="We must be willing to let go of the life we planned so as to have the life that is waiting for us.", weight_class=6, reach=68,
        professional_level=1, fav_rocky_fighter="Adonis Johnson", vaccinated=False,
        nickname="Grease", walkout_song="'Living Single' by Big Sean", availability=2,
        has_kids=True, religion='Jewish', pets='3 Cats', rate=50, in_person=True)

    answer80= Answer(
        user_id=80, about="Happiness is not by chance, but by choice.", weight_class=1, reach=69,
        professional_level=0, fav_rocky_fighter="Adonis Johnson", vaccinated=True,
        nickname="Wilma", walkout_song="'Single Again' by Big Sean", availability=1,
        has_kids=False, religion='Jewish', pets='3 Dogs', rate=500, in_person=False)



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
