# script_chapter8.rpy
#
# Chapter 8. Ana has her first one on one session with Silvia in the yoga studio.

label chapter_eight:

    cn "One week later"

    scene bg studio sunset
    play music pt_soundscape fadein 1.5

    show ana default with easeinleft:
        xpos 30
        ypos 60

    n "I felt jittery and excited as I stepped into the yoga studio that afternoon."
    n "The studio, usually full of sun, 
    was dimly lit today. Curtains were drawn over the windows, and an assortment of candles provided most of the light today."
    
    show silvia default with dissolve:
        xpos 500
        ypos 10

    n "Silvia was seated in the center of the studio, facing the door as I walked in. She greeted me warmly."

    show silvia default at hop
    s "Welcome, dear Ana! Would you like some tea?"

    n "There were two cups beside her; she held one out to me. I accepted it. "

    show ana default at hop
    a "Thank you, Silvia."

    s "No, it's my pleasure, truly."

    nvl clear

    n "She sipped from her own cup. "

    s "I'm sure you are wondering about the session today. It will be a lot like what we've done in group sessions, 
    just with you and me. "
    
    s "I will guide you through some breathwork and meditation, and I want you to explore the emotions that arise 
    for you as you do so. "

    s "Even the darker emotions. As in the group session, it's important to bring your shadow to the light." 
    
    s "Do you think you 
    can do that for me?"

    n "The way she described it didn't sound {i}too{/i} scary."

    a "Yes, I think I can do that."
        
    s "Ah ah, not \"I think\", \"I {i}know{/i} I can\""
        
    a "O-oh, sorry."
    
    a "I know I can do that."

    s "Good, good."

    nvl clear 

    n "She smiled at me and put on some music. It was soft and meditative, easily blending into the background."
        
    s "Close your eyes for me."

    scene cg blank with dissolve
    nvl clear
        
    s "Let's walk through some of your memories together. "
    
    s "Think about the sights and sounds of your childhood." 
    
    s "The smells that meant you had come home. Imagine how it felt to be you, in your small body, exploring the world. "

    n "She spoke slowly and methodically, drawing out every word. "
    
    n "I squeezed my eyelids in concentration."

    nvl clear

    s "Tell me about one of these memories. Choose one where you felt safe, and loved."

    n "Different thoughts flitted through my head until I landed on one."

    a "When I was little, me and my Mama and Papa and sister moved a few towns over."

    a " It wasn't that far, but I was really upset. I was convinced the new place would be stupid and bad." 

    a "I cried a lot and threw tantrums, Mama and Papa were really frustrated with me. "

    a "My sister is a bit older than me, so she wasn't making as much of a fuss about it."

    nvl clear 

    a "The first evening I saw the house, it was this warm summer night."
    a "I was pouting all the way there. "
    
    a "But we pulled up to this place, and it looked like a house out of a storybook, with a big yard full of long meadow grass and wild flowers and trees."

    a "And the yard was brimming with fireflies." 

    show cg fireflies with dissolve

    a "I had never seen fireflies before. I thought they were little stars." 

    a "I was immediately distracted from my tantrum and went out to look."

    nvl clear

    a "Papa got out a jar, and showed me and Sophia how to catch the glowing bugs."
    
    a "Once they were inside the jar, I could see their tiny wings  and legs. I didn't like bugs much, usually, but I thought these
     were the prettiest things in the world. "
    
    a "Me and Sophia must have spent at least 
    an hour running around catching them, while Mama and Papa unloaded the car. "

    a "When they were done, they ordered pizza for all of us, and we ate it sitting on the new porch. "
    
    a " That was special too because they  usually never let us order takeout."
    
    a "Between the beautiful star bugs and the pizza, I thought the new house must be magical."

    nvl clear 

    scene bg studio sunset with dissolve

    show silvia default with dissolve:
        xpos 500
        ypos 10

    n "I finished, and hesitated, squinting my eyes open a tiny bit to look at Silvia. She was gazing at me with that soul-searching 
    expression."

    hide silvia default with dissolve
   
    scene cg blank with dissolve

    s "What a beautiful memory."
    
    s "Thank you for blessing me with that, Ana. I see why it is such a positive one for you."

    s "I'm going to ask you to do something that might be challenging for you. But I know you will rise to the challenge. "

    nvl clear

    stop music fadeout 1.0

    s "I want you to explore some negative emotions you may have around the people in that memory."
    
    s "Early childhood memories are often 
    simpler, more pure, but they become complicated as we grow older. "
    
    s "Tell me about the shadows in your light."

    nvl clear
    play music amoebic_sea volume 0.5

    n "Urgh. My stomach dropped."
        
    a "I... yes, it's certainly not as simple as it was back then."

    a "It feels like I'm... tainting the memory, sort of, by describing the bad in it?"

    s "I understand, but there is no need to worry about speaking your truth."

    a "Well — "

    a "I... feel like I'm a disappointment to them. Like when Mama and Papa were frustrated with me for being upset, in the memory? 
    It feels like that most of the time now. "

    nvl clear

    a "Sophia grew up to be the golden child, and I'm always somewhere behind her."

    a "Teachers would always expect me to be just like her. "

    a "Like yes, I have a finance job, but Sophia basically {i}runs{/i} the company she works for. "
    
    a "I just poke around at spreadsheets other people give me."
    
    a "She has a husband and a kid, and I can't even find a guy to go on a second date with. Mama and Papa are sooo proud of her, I know it. "

    a "But whenever Mama or Papa talks to me, it's always to ask me if I've got a promotion yet, if I've found a new job, 
    if I'm seeing anyone, when they're going to get another grandkid. It's never ending."  
    
    a "They just want me to be a copy of her. "

    nvl clear

    a "...Shit, sorry, I'm rambling."

    s "No apologies, this is just the nature of this work. Please, continue exploring these feelings for me."

    a "I... don't know if I want to?"
    
    a "My parents love me and everything. It's not really that bad."
    
    a "I don't want to bitch about them for no reason. They're just parents, that's how it is. "

    s "And yet this is what comes out when you are free to speak? "
    
    s "Sit with that. Consider what it means."

    nvl clear 
        
    a "I think that's on me, really, since I'm the one bringing it up..."
    
    a "I just wish it was easier and I wish they 
    didn't want all this from me and it's my fault and and and — "

    n "Fuck. Even with my eyes closed, tears were streaming down my face."

    s "Ana. I can see you're becoming dysregulated. "

    s "Let me help you center yourself again. Lay down, and place one hand over your diaphragm. 
    Breathe in, and out. "

    nvl clear 

    s "In, and out."

    n "I did as she asked."
    
    n "It was the familiar breathwork breathing pattern."
    
    n "As my breaths became quicker and quicker, I felt like my heart was going to beat out of my chest. "
    
    n "My panic must have showed on my face, because Silvia said — "

    s "Continue breathing just as we practiced. You have the power inside you to conquer this feeling."

    nvl clear 
    stop music fadeout 1

    n "Shakily, I kept breathing, in, and out, in, and out."

    scene cg trippin with dissolve
    play music sleep_forest fadein 1 volume 1
    
    n "Time started to blur a little. That floaty feeling that was 
    so strange just a few weeks ago now felt familiar and welcome. "

    n "I found myself giggling and trembling at the same time, as the patterns under my eyelids grew brighter."

    s "That's it, that's it. Wonderful job, Ana. Continue just like this."

    n "I did it! I did a good job.... Being able to enter an altered state by just changing my breathing felt so powerful. "

    n "I couldn't remember what I was so upset about, although I could feel the salt on my cheeks where the tears had dried. 
    There was just breath and color and light now —"

    nvl clear
    scene cg tripping with dissolve
    play music "<from 146>amoebic_sea.mp3" fadein 0.5

    n "And suddenly, I felt a warm touch on my shoulder."

    a "...wha?"

    s "This will help ground you further. Lean into it, let yourself feel everything fully."

    n "I tried to concentrate on keeping my breathing steady as I felt her hands trace my arms, my shoulders, my back. 
    Geometric patterns exploded out of rhythm."

    n "I felt her hand under my chin, tracing my jaw. Concentrate, in, and out, in, and out.  "

    n "Suddenly I felt her other hand on my breast."

    nvl clear 

    scene cg eyes sunset with hpunch

    cn "My eyes flew open. Silvia filled my entire field of vision, with her vivid, hazel-green eyes looking deep into mine. 
    Our faces were just inches apart. "

    scene cg seduction

    cn "I squirmed backwards. Silvia continued to gaze at me with a calm but focused expression."

    nvl clear 

    s "You got distracted."

    a "W-what? The fuck? Were you doing?"

    s "I was helping you go deeper. Trusting me during this process is vital for working through your shadow."

    s "But it looks like you aren't ready to work through those feelings yet."

    s "I thought you had potential, Ana. But It looks like you're committed to getting in your own way. "

    s "I can't help you if you don't accept that the problem here is you."

    nvl clear 

    n "I sat, staring at her."

    a "I don't... understand."

    s "I know you don't. You are not ready yet."

    s "Come back only when you are ready. For now, you are dismissed."

    scene bg studio sunset2

    a "I'm... I'm really sorry. For everything? I'm sorry. I don't know."

    a "T-thank you for the session."

    nvl clear

    n "Silvia sat stern and calm in the center of the studio."

    n "I scrambled to gather my things and fled out the door. "

    stop music fadeout 1
    nvl clear

call chapter_nine from _call_chapter_nine
