# script_chapter9.rpy
#
# Chapter 9. Ana has an upsetting call with her family.

label chapter_nine:

    play music "pad_low.mp3"

    scene bg bedroom day 
    cn "The next few days passed in a haze."
    scene bg livingroom day
    cn "I woke up, I went to work, I came home, I went to sleep."
    scene bg office
    cn "The next day I did it again."
    scene bg apt night

    cn "Half formed thoughts whirled in my head. \nWhat the fuck was that session? Why did I talk about my family so badly?"
    scene bg bedroom day 

    cn "Why did she touch me?  Did I actually do something wrong?" 
    scene bg livingroom day
    
    cn "I tried to sort through it, but it made my head hurt."
    scene bg office

    cn "I did my best to act normal around Emily. She teased me about the session afterwards, of course."
    scene bg apt night
    
    cn "I told her it went fine. \nBy the face  she made, I could tell she was concerned that I suddenly didn't want to share, but after a bit, she stopped asking. "
    scene bg bedroom night 

    cn "I tried to watch new episodes of my favorite true crime shows, but something about them just wouldn't stick in my head. \nI put on re-runs 
    instead. \nFamiliar. Less likely to disappoint."

    show ana default with easeinleft:
        xpos 100
        ypos 60

    stop music fadeout 3.0

    n "One night, my sister called as I was in the middle of watching."

    show sophia sprite with easeinbottom:
        xpos 60
        ypos 5

    show ana default with ease:
        xzoom -1.0
        xpos 600
        ypos 30

    show ana default at hop

    a "Hey Sophia."

    show sophia sprite at hop

    o "Ana, hello!"

    o "I'm at Mama and Papa's right now — guys, Ana's on the phone!"

    nvl clear

    n "There was a rustling against the microphone as the phone was jostled around."

    m "Ana, mija!"

    p "Hi Ana!"

    m "How have you been sleeping? Eating? How is it at work?"

    a "Hi Mama, hi Papa! It's been okay, I haven't been sleeping the best but work is good."

    m "Ahh, wonderful! You should really go to bed earlier, sleep will come easier if you do that. "

    p "I'm looking forward to hearing about a promotion soon! I know you've got it in you, mijita."

    nvl clear

    a "Ah, thank you, I'll try my best. "

    a "I'm not really sure what opportunities for advancement there are in this job, I'm just an intern right now so it might only be for one season."

    p "I'm sure there's something there for you, if you talk to the right people! Ask around, see what's out there. "

    play music soundscape fadein 8.0

    m "Yes, what your Papa said! But even if jobs don't come right away, maybe you'll meet a nice young man to help get you set up. "

    a "I'm trying, I swear! The young men here aren't so nice. "

    o "She is right about that, she's been telling me all about it."

    nvl clear

    m "You're telling Sophia all of this, but not us?! Ana, we're your parents. We want to know."

    a "It's not that easy! None of those dates were any good, I swear."

    a "Even if dating isn't going well right now, I've been working on myself."

    a "I've been going to yoga classes every week at this local studio and I've gotten a lot better at it! I've gotten so much more 
    flexible, and I've started talking to the other women in class. It makes me feel really powerful! "

    nvl clear

    n "Desperately grasping for something that was going right in my life, I'd fallen back on my yoga journey over the past few weeks. 
    It's true, I was proud of my progress, and it had been making me feel better... until that session with Silvia. I squashed those feelings down."

    a "And I really like the instructor who runs the classes."

    a "She's very..."

    a "...cool."

    nvl clear

    n "There was a brief pause at the other end of the line, it felt like an eternity."

    m "Ah, mija, I'm glad you've been doing something that feels good to you! But don't you think it would be better to spend your time setting 
    up your future? Setting aside money for your family?"

    p "The smart move would be to have a steady career before getting into hobbies like that. It can be expensive, you know? And it's not going 
    to bring in any money."

    o "You're both being too harsh on her. She just graduated! I might've had a full-time job lined up by then but it doesn't mean everyone has to. "

    a "Guys — "

    nvl clear

    p "Someone has to keep her on track, personal responsibility is important. "

    o "She was trying to share something that was important to her!"

    m "Sophia, we're your parents too, please treat us like it. We just want what's best for both of you.  "

    o "Mama — "

    a "GUYS."

    nvl clear

    a "Please stop. It's okay."

    a "I get it. "

    a "You're worried about me, you just want the best for me. I'm sorry for worrying you. "

    a "Thank you for the advice, Mama, Papa. "

    m "Yes, Ana, we want you to be the best you can be."

    a "I know, and I appreciate it. "

    o "Ana, are you sure — "

    a "I have to head out now, I love you all. Have a good night."

    nvl clear

    hide sophia sprite with easeoutbottom

    show ana default with ease:
        xzoom 1.0
        xpos 100
        ypos 30

    show ana with hpunch

    n "Tears released like a flood the moment I hung up the call. "

    n "Fuck!!! "

    n "When am I ever going to be enough for them??"

    n "I know they love me. I know they think they want the best for me. But I can never do anything the way they want me to."

    nvl clear 

    n "I wish they would just be happy for me for once. "

    n "And even when Sophia tries to defend me, she just rubs it in deeper. They never have problems with her. Because she's perfect."

    n "I buried my face into my pillow and tried to block everything out. Stupid stupid stupid."

    n "I wish I could just follow what feels good. Work doesn't feel good. Going on dates doesn't feel good."

    nvl clear

    n "...maybe I do really need help."

    n "I took a deep breath and opened Silvia's instagram. I sent just one message. "

    nvl clear

    hide ana

    cn "I'm ready now."

    stop music fadeout 2


call chapter_ten from _call_chapter_ten