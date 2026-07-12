# script_chapter7.rpy
#
# Chapter 7. Emily and Ana talk about the upcoming one on one session with Silvia.

label chapter_seven:

    scene bg livingroom night with fadehold
    play music raw fadein 0.5

    show ana default with easeinleft:
        xpos 100
        ypos 60

    n "I plopped on the couch and started scrolling mindlessly through videos, but my mind was elsewhere. "

    n "Silvia really thought I had a \"beautiful soul\"? Me, of all people?"

    n "Even after I told her and everyone what I'd done? "

    n "I can't believe she's being so kind to me."

    n "I'm not sure if I'm ready for one-on-one shadow work, if a group setting was already that intense...
    but if Silvia thinks I'm ready, I want to trust her."

    nvl clear

    show emily default with easeinright:
        xpos 500
        ypos 40

    show emily default at hop
    e "Hey girl!!"

    show ana default at hop
    a "Heyyy Emilyy!"

    e "Mannn my clients today were so picky, what a long day. Got dinner with the GF to blow off some steam.
    How're you?"

    a "Oh y'know, the usual same old shit at work. "

    a "I went to another yoga session afterwards, I just got home. "

    e "Oh yeah, same instructor? That new age lady you were talking about from Instagram?"

    a "Yup, that's her."

    nvl clear

    a "The session was honestly kind of a lot this evening. "

    a "But Silvia, the instructor, came up to me afterwards and offered me a free one on one session? "

    a "Just me, no one else. She said I had a \"beautiful soul\"."

    e "Woahhhhh, that's crazy."

    e "It kinda sounds like she's flirting!"

    a "What? No, I think that's just how she talks. Souls and energy and shadow work and shit."

    nvl clear

    e "I dunno girl, it seems like she wants you."

    e "Why else would she give you a one on one for free? Usually coaches want
    all the money they can get from you."

    a "No I reallyyy doubt it's something like that. "

    a "She...looks pretty straight?"

    a "And she'd be way out of my league anyway,
    she's gorgeous and skinny and her hair is always perfect."

    e "If you say so! "

    n "Emily winked very obviously, scrunching her cheeks up to do so."

    e "You seem pretty flattered by her attention."

    nvl clear

    a "Well yeah, she's Ms. Perfect. It's crazy that she'd give someone like me the time of day if I'm not paying her."

    e "You're underselling yourself ma'am, you've got plenty to offer!"

    e "You gotta report back to me on how it goes though. I wanna know the deets!"

    a "Yeah for sure."

    n "It's so much like Emily to read everything in a gay way. It doesn't have to be like that, just because a pretty
    woman gave me attention."

    n "I'll go to the session next week, and I'll see what it's really like."

    nvl clear
    stop music fadeout 2
    scene cg blank with fadehold
