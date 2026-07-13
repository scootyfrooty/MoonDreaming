# script_chapter5.rpy
#
# Chapter 5. Ana goes to her first group yoga class at Silvia's studio.

label chapter_five:

    play music "pad_low.mp3" volume 0.3
    scene bg studio day with fadehold
    show ana default with easeinleft:
        xpos 30
        ypos 60

    n "The huge windows bathed the yoga studio's wood floor in soft, warm light. There's some other students 
    floating around, they look like they do this all the time. They're sipping tea from cups left on a table at the front of the 
    class. "

    n "I looked around for Silvia. She's the center of all this."

    n "I poured a cup of tea from the kettle on the table, softly nodding my head as a greeting to the other 
    participants. "

    show silvia default with easeinright:
        xpos 500
        ypos 10

    nvl clear

    n "Silvia glided in from one of the side rooms, her long blonde hair tossing in the breeze like a model on a 
    catwalk. "
    
    n "It's ridiculous how perfect she looks, even outside of Instagram. No one looks like their photos in real life — at 
    least, that's what I'd thought. She seemed to glow from within."

    show silvia default at hop
    s "Hellooooooo goddesses!" 

    s "I'm so very glad to have you here. Some returning friends and some new ones, I see."

    s "Why don't you gather on the mats over here and we can get started?"

    nvl clear

    n "I sat on a mat next to a pasty pale ginger woman who looked like she might burn at the slightest touch of sun. 
    She gave me a smile and a nod and I returned it. "
    
    n "Another woman, heavier with tanner skin, sat on my other side.  We exchanged a silent nod as well. "

    s "Don't worry if you haven't done this before, I am sure you will all do beautifully."

    nvl clear 

    n "We stretched and went through some basic yoga. Downward dog, tree pose — the usuals. "

    n "It's not hard, but it makes me realize it's been a while since I've stretched out my back, sooo stiff. 
    It feels nice to loosen up."

    n "Hearing Silvia's voice guide us through the movements is soothing. My brain quiets down a bit. I don't have 
    to worry about what to do next."

    s "Aaaand exhale into downward dog. That's right. Let it all go."

    n "I exhaled and moved my body accordingly. The people around me did the same."

    n "We continued at a leisurely pace through different poses for about half an hour, until Silvia had us return 
    to sukhasana, and sit facing her. "

    nvl clear

    s "For the next part of our morning together, I want to show you all the power of breathwork." 
    
    s "Don't worry if you haven't done it before, I'll show you how." 

    stop music fadeout 0.5

    play music "sleep_forest.mp3" volume 1.5 fadein 1 

    s "Your body has so much natural power inside, just waiting to be tapped into. Breathwork is a way to connect with your 
    inner power, your inner goddess. Let yourself melt into the music here."

    s "Lay down flat on your mats, close your eyes, and rest your hand over your diaphragm. Breathe in for me, aaand 
    breathe out again. "

    nvl clear
    scene cg blank

    s "In, and out, in, and out. Now keep that pace."

    s "In, and out."

    n "I tried my best to relax and breathe slowly. The music was definitely hippie music, but it was pleasant 
    enough. Rhythmic drums kept a steady beat."

    s "Now go a bit quicker. In and out, in and out. That's it."

    n "This was quite a bit quicker than the usual slow breathing of yoga. The drums sped up."

    s "Keep it up, continue breathing in and out with that rhythm. Notice how you feel in the music, 
    in your body."

    n "It was a bit awkward hearing everyone breathing rapidly, so I tried to focus entirely on the music."

    nvl clear

    n "My mind wandered...." 

    n "After a few songs, I started to feel floaty and a bit lightheaded. "

    n "In, and out, in, and out."

    n "A quick drumbeat, like a rabbit's racing heart."

    scene cg trippin with dissolve

    n "It felt like time shifted a little to the left. I could no longer tell how long I'd been breathing that way, 
    and sensations blurred together. "

    n "I became aware of patterns inside my eyelids, growing brighter and more intricate by the moment. They swirled in 
    mesmerising shapes, abstract, impossible. "

    n "I could hear the drumbeat and Silvia's voice, but they sounded far away, like an echo in the very furthest 
    reaches of my head."

    n "Geometric patterns spun in and out of my vision ...  chaotic and absolutely calm at the same time."

    n "The music slowed, and I automatically slowed my breathing along with it. "

    nvl clear

    n "After some amount of time, I heard Silvia say — "

    s "You may now open your eyes and return to the room."

    nvl clear

    scene bg studio sunset with dissolve
   
    show silvia default:
        xpos 500
        ypos 10

    show ana default:
        xpos 30
        ypos 60

    n "Colors were bright and vivid, I could recognize the room around me but it felt transformed. I sat up, a 
    bit dazed, and saw my classmates looking out of it as well. "
    
    n "We had shared this state together...I wonder if they saw the same things as I did? Silvia sat at the front of the room, still in 
    sukhasana with her hands resting lightly on her 
    crossed legs."

    s "Thank you all for trusting me to guide you on that journey. I know it may have awakened new and different feelings 
    in you. Sit with them! Welcome those feelings in. "

    s "If you'd like help processing anything you experienced during our breathwork session, feel free to come speak to me 
    afterwards. "

    s "Otherwise, you are all free to go! Have a week full of love and light. Namaste."

    stop music fadeout 0.5
    nvl clear

    n "Some folks headed towards the front of the room to talk to Silvia, others gathered their things and started heading for the door. 
    A couple friends chatted in low voices with each other. "
    
    n "I got the sense that we had all experienced 
    something profound together, and didn't want to speak too loud for fear of disturbing it."

    n "I thought about speaking with Silvia but I still felt far away. I wasn't sure what I would say to her that 
    could encapsulate my feelings, so I started to roll up my mat."

    n "I couldn't resist a glance back at Silvia as I headed for the door." 
    
    n "She was now deep in conversation with one 
    of the women who had approached her. Their faces were close together, with Silvia gazing into the woman's eyes and nodding her 
    head as she listened to her speak, completely engaged with what she was saying. "

    hide ana default with easeoutleft
    
    n "I felt a pang in my chest, quickly looked away and closed the door behind me."

    nvl clear

    scene bg car sunset with fade

    play music "pad_low.mp3" volume 0.7

    show ana default with easeinleft:
        xpos 30
        ypos 60

    n "I sat for a while in my car in the lot, resting my chin on the dash and staring out at the sunset. 
    The orange-pink sky looked extra vivid."

    n "That's not what I expected from a beginner yoga class, that's for sure. "

    n "At least that class was something different, a break in the monotony."

    n "I felt tipsy, but I hadn't taken anything — somehow, all of that power came from 
    inside my own body. Maybe Silvia was onto something with all that \"goddess\" talk. "
    
    n "If I could alter my own mind that much without a single substance, who knows what else I was capable of, if I just believed?"

    n "I was still too nervous to talk to anyone, but I could see that changing."
    
    n "Maybe with the right mindset, it wouldn't be so hard? Maybe I really could change myself and the world around me."

    stop music

call chapter_six from _call_chapter_six
