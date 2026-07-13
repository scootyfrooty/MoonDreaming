# script_chapter3.rpy
#
# Chapter 3. The scene where Ana goes to a cafe.

label chapter_three:
    nvl clear
    scene bg cafe day with fadehold
    play music "pad_low.mp3"

    show ana default with easeinleft:
        xpos 100
        ypos 30

    n "Despite the early hour, it was bustling at the cafe down the street. Students filled most of the booths. 
    Loud, but comfortingly familiar.  I used to go here with Emily and my friends when I was in college, 
    but now I usually go by myself. It feels awkward being alone in a space like this, when so many people are 
    filling up the booths with groups of friends."

    b "Matcha latte for Ana!"

    show ana default at hop

    a "Ah, thank you!"

    n "The barista had a big septum ring and tattoos peaking out from under her apron. 
    Makes sense that she'd end up in a job like this."

    n "I've never loved the grassy taste of matcha, but it looks so cute in photos... caffeine is caffeine, anyway. "

    n "Looking around the room, I wish I had the same energy as those annoyingly chatty first years. "

    n "I thought things would fall into place once I graduated. I'm a real accountant now, sort of? An accounting 
    assistant, at least. "

    n "It's so mind-numbing though! I'm bored out of my mind all the time at work — spreadsheets, on spreadsheets, 
    on spreadsheets, forever."
    
    n "Making the \"safe choice\" to keep my parents happy was overrated. But what else was 
    I supposed to do? They don't pay you to watch Netflix all night and sleep all day. And one wrong step would've landed 
    me with the  baristas here, shucking drinks and getting paid pennies for it. At least now I don't have to slink home to 
    beg my parents for money. "

    nvl clear
    

    n "I scrolled on my phone to keep my hands busy. When I see my college friends posts on Instagram, they look like 
    they've made it. Thriving in their careers and looking hot while doing it....I guess the #GirlBoss life really is 
    possible."

    n "So many of them moved away, and the ones who stayed here barely invite me to anything any more. I haven't seen 
    them in months, really."
    
    n "I guess they think they're better than me? Because they earn a salary, their hair is 
    styled perfectly, and they have the perfect photogenic boyfriend to compliment their outfit pics? Did the time 
    we spent kneeling by the toilet at a frat party mean nothing to them now that they have everything?"

    n "Mid-scroll, I got a dating app ad. Ugh, way to rub it in. Besides an occasional good dick appointment (among a 
    ton of mediocre dick appointments),  none of my dates have gone anywhere. "

    nvl clear

    n "Emily is the only friend I've really seen, and we live together so it would be hard not to cross paths. She has 
    her own group of friends, her own girlfriend." 
    
    n "I don't get along with them....they're the type who make being gay their whole 
    personality. They're loud, they dress kinda sloppy." 
    
    n "Emily is the least intense of the bunch, but we usually only hang out to 
    watch shows together. "

    nvl clear

    n "As I continued to scroll my feed, I saw a new face." 

    show ana default with ease:
        xzoom -1.0
        xpos 600
        ypos 30

    show instagram sprite with easeinbottom:
        xpos 60
        ypos 5
    
    n "Another beautiful woman, of course, because there's a million of those. "


    n "This woman was in the middle of a crowded public park, chanting and singing something new-age-y. The caption read 
    \"Vibrate at your truest frequency, and you will be unstoppable.\" "

    n "I recognized the park from a couple of towns over, but this woman looked like she belonged on a hippie retreat in 
    Tulum. "
    
    n "Surrounded by people in jeans and tshirts, she stood out with her skimpy, loose clothing, pashminas, and 
    sun-kissed blonde hair against that familiar park backdrop. People turned their heads to stare at her, but she continued 
    chanting, appearing peaceful and unbothered."

    nvl clear

    n "I cringed... that just wasn't normal behavior. "
    
    n "God, you have to admire the audacity though. It's definitely more 
    interesting than being the latest #BossBabe career-woman. "

    n "I tapped into her page and was greeted with lush scenery, upscale vegan food, yoga exercises, and 
    motivational quotes."
    
    n "And in the center of it was her, over and over again. Immersed in greenery, in lotus pose, 
    swimming under a full moon, posing with other equally beautiful women."

    nvl clear

    n "Her bio proclaimed: \n {b}Silvia Garcia{/b} \n@becoming-silvia \nSomatic ritual + Tantric surrender + Divine femininity \n {b}Ready to 
    become your highest self? Join me for courses and workshops at the link below!{/b}  "

    n "In each picture, her hair fell over her shoulder in effortless-seeming waves that probably actually took hours to style. 
    Her eyes had a hypnotic, intense quality. She looked ethereal and radiant."

    n "The other women in the pictures couldn't match up, even when they were touching, or holding hands, in the midst of some 
    feminine ritual — her presence brought all attention back to her." 
    n "She towered over them, sometimes literally as they knelt in front of her. Their eyes were always trained on her."

    n "On other people it would look cringey, but she made it look natural, somehow. "

    nvl clear

    n ".....ugh."

    n "Uggggggghhhhh."

    n "I want that kind of confidence! I want that kind of body! I want people to look at me that way! "

    n "Her main character energy is unmatched. Oh my god."

    n "If I got a transformation potion that turned me into a blonde white lady, would my life look like this too?? I mean, 
    with her last name, maybe she's Latina like me? Or maybe she just married into it. Who knows. "

    n "She's certainly playing a convincing white woman. Everyone would be sooo sad if she got murdered. You know they'd make a 
    whole documentary about her and sign petitions about finding her killer. She'd be the center of the internet for at least a 
    week. "

    nvl clear

    n "I looked around her page some more. A video of her seated in a yoga studio, with soft music playing in the background."

    s "I was thinking this morning — we spend so much time avoiding pain. 
    Trying not to expose our weak spots, trying to make everyone like us, trying to tread the safest path."

    s "But opening yourself up to pain is how you can transcend and surpass it. "
    
    s "Let it wash over and through you, and know that you choose your reality. 
    You choose what you feel."

    s "In that, you are invincible. You can master that pain, and turn it into your power. 
    So go out there and choose your reality like the goddess you know you are."

    n "Okay, girlie. Easy for you to say when you don't look like you've ever had a single real problem in your life."

    nvl clear

    hide instagram sprite with easeoutbottom

    show ana default with ease:
        xzoom 1.0
        xpos 100
        ypos 30

    n "I flipped my phone over, and finished the last dregs of my matcha." 
    
    n "Too distracting, it was time to head to work."

    hide ana default
    stop music fadeout 0.5
    nvl clear
    scene bg office

    cn "46 unread emails had flooded my inbox, and I was drowning in spreadsheets."
    
    cn "New day, but exactly the same bullshit! \nThere's gotta be more to life than this."

    


call chapter_four from _call_chapter_four
