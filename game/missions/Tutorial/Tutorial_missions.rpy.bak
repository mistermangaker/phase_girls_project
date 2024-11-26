default tutorial_introduction = Story_Mission.mission_from_xml("tutorial_mission1.xml","tutorial1")


init python in tutorial:
    tenma_questions_firstviewing = True
    tenma_mainquestions_firstviewing = True
    sakana_mainquestions_firstviewing = True
    menuchoice1 = False
    menuchoice2 = False
    menuchoice3 = False
    menuchoice4 = False
    menuchoice5 = False
    menuchoice6 = True
    menuchoice7 = False
    menuchoiceshowthatsallbutton = True
    testingsakana = 0
    justclicked = False
    justclickedtext = ""


label tutorialintro_start:
    scene entrance day
    play music "Music_Export/Calm/Clouds.mp3"  loop volume 0.8
    show sakana
    if persistent.debugmode:
        call .pre_tutorial_skip
    sakana "Hello there and I am sakana and welcome to the game developer tutorial for “The Phase Connect Streamer House” "
    sakana "Here I will explain everything you need to know about the basics for developing visual novels using this game open source framework, “the actor-missions framework” "
    sakana "Now you maybe wondering as to why I am here"
    menu:
        "Not Really":
            pass
            
    sakana "Well it's because the main artist is overworked and can't justify making more sprites that will only be used during the tuorial"
    sakana "So they will using character sprites that appear in game!"
    play sound "<to 1.8>Effects/YT_Impacts/Dumpster_door.mp3" volume 1.2
    show sakana tutorial jojo pose1 with vpunch
    
    sakana "BUT DON'T WORRY"
    sakana "WITH ENOUGH EFFORT ANYTHING IS POSSIBLE"
    sakana "I PLAN ON WASTING AS MUCH OF THEIR PROFESSIONAL TIME AS POSSIBLE!!"
    show sakana tutorial closeup fist:
        linear 0.5 xalign 0.5
        linear 0.5 xalign 0.51
        repeat
    sakana "now let's make their job difficult"
    show sakana tutorial closeup pointup:
        linear 0.5 xalign 0.5
    sakana "before we begin this tutorial is for “alpha 1” of the game."
    
    
    sakana "So if that is not the current build your are playing then this information may be..."
    play sound "<from 1.8 to 3.2>Effects/YT_Impacts/Dumpster_door.mp3" volume 1.2
    show sakana tutorial jojo pose2 with vpunch 
    
    sakana "OUTDATED!"
    
    show sakana tutorial jojo pose2_point
    sakana "Check the {a=https://github.com/mistermangaker/phase_girls_project/wiki}The github wiki and documentation{/a} on our {a=https://github.com/mistermangaker/phase_girls_project}github repository{/a} for a full rundown of features and code as this tutorial is only the basics"
    show sakana neutral
    sakana "So uh now that is all out of the way. let's get into the lessons"
    
label .tutorial_menu_choice:
    show sakana neutral at right
    menu:
        sakana "What do you want to learn in this course and we will get to it"
        
        "Project basics about contribution and licensing " if not tutorial.menuchoice1:
            $ tutorial_Project_basics.SetActive()
            $ tutorial.menuchoice1 = True
            $ tutorial.menuchoiceshowthatsallbutton = True
            jump .tutorial_menu_choice
            
        "Game framework basics"if not tutorial.menuchoice2:
            $ tutorial_Project_framework.SetActive()
            $ tutorial.menuchoice2 = True
            $ tutorial.menuchoiceshowthatsallbutton = True
            jump .tutorial_menu_choice
            
        "Game Art and working with displayables"if not tutorial.menuchoice3:
            $ tutorial_Project_art.SetActive()
            $ tutorial.menuchoice3 = True
            $ tutorial.menuchoiceshowthatsallbutton = True
            jump .tutorial_menu_choice

        "Writing and working with renpy labels, flags, and flow control "if not tutorial.menuchoice4:
            $ tutorial_Project_writing.SetActive()
            $ tutorial.menuchoice4 = True
            $ tutorial.menuchoiceshowthatsallbutton = True
            jump .tutorial_menu_choice

        "Coding and developing features for the game"if not tutorial.menuchoice5:
            $ tutorial_Project_coding.SetActive()
            $ tutorial.menuchoice5 = True
            $ tutorial.menuchoiceshowthatsallbutton = True
            jump .tutorial_menu_choice

        "Tell me everything" if not tutorial.menuchoice1 or not tutorial.menuchoice2 or not tutorial.menuchoice3 or not tutorial.menuchoice4 or not tutorial.menuchoice5:
            $ tutorial_Project_basics.SetActive()
            $ tutorial_Project_framework.SetActive()
            $ tutorial_Project_art.SetActive()
            $ tutorial_Project_writing.SetActive()
            $ tutorial_Project_coding.SetActive()
            
            $ tutorial.menuchoice7 = True
            pass
        "Continue Without Selecting anything" if not tutorial.menuchoice1 and not tutorial.menuchoice2 and not tutorial.menuchoice3 and not tutorial.menuchoice4 and not tutorial.menuchoice5 and tutorial.menuchoiceshowthatsallbutton:
            pass
        "Thats all I want to learn about" if tutorial.menuchoice1 or tutorial.menuchoice2 or tutorial.menuchoice3 or tutorial.menuchoice4 or tutorial.menuchoice5 and tutorial.menuchoiceshowthatsallbutton:
            pass

label .tutorial_afterscreen:
    show sakana neutral at center

    if tutorial.menuchoice1 and tutorial.menuchoice2 and tutorial.menuchoice3 and tutorial.menuchoice4 and tutorial.menuchoice5 :
        $ tutorial.menuchoice7 = True
    if tutorial.menuchoice7:
        sakana "Wow you want to know everything huh?"
        
        sakana "How eager you are"
    if not tutorial.menuchoice1 and not tutorial.menuchoice2 and not tutorial.menuchoice3 and not tutorial.menuchoice4 and not tutorial.menuchoice5  and not tutorial.menuchoice7:
        
        call .tutorial_afterscreen_noChoice
    
    sakana "Alright then we will load up the lessons for you look at them at your own pleasure"
    
    $ tutorial_introduction.SetComplete()

    jump endday

label .tutorial_afterscreen_noChoice:
    if not tutorial.justclicked:
        sakana "Uh hey. Can't help but notice. You Uh didn't select anything"
        sakana "Sooo uh what gives?"
        sakana "Did you missclick or something or are you just testing my patiences?"
    if tutorial.justclicked:
        if tutorial.testingsakana == 1:
            $ tutorial.justclickedtext = "You didn't select anything again care to explain why?"
        if tutorial.testingsakana == 2:
            $ tutorial.justclickedtext = "You have clicked the button again"

        if tutorial.testingsakana == 3:
            $ tutorial.justclickedtext = "You know this isn't as funny the third time right?"
        if tutorial.testingsakana == 4:
            $ tutorial.justclickedtext = "I'm starting to dislike your enthusiam"
        if tutorial.testingsakana == 5:
            $ tutorial.justclickedtext = "*Sighs*"
    else:
        $ tutorial.justclickedtext = "Care to explain why?"
    show sakana neutral at right
    menu:
        sakana "[tutorial.justclickedtext]"
        
        "I was Just curious what would happen if I didn't choose an option":
            call .testingsakana
            
        "Oh sorry I missclicked":
            $ tutorial.justclicked = False
            call .missclicked
        "I didn't want to choose anything":
            $ tutorial.justclicked = False
            call .didntwanttochoose
    return
label .testingsakana:
    show sakana at center
    $ tutorial.testingsakana +=1
    $ tutorial.justclicked = True
    if tutorial.testingsakana == 1:
        sakana "I see. you were testing me"
        sakana "That's one of the many joys of visual novels isn't it?"
        sakana "Since it's a game you as the player strive to find bugs and portions of the game that are overlooked by the developer"
        sakana "And you can feel some sense of pride in finding something the developer missed"
        sakana "Rest assured that this tutorial is well made"
        sakana "Now lets send you back shall we?"
        jump .tutorial_menu_choice
    if tutorial.testingsakana == 2:
        sakana "I see. You've clicked the button a second time to see if my dialogue would change"
        sakana "Yes I planned for you to do this. It's why this supplimentary dialogue is here"
        sakana "Now allow me to reiterate"
        sakana "*Ahem*"
        play sound "<from 1.8 to 3.2>Effects/YT_Impacts/Dumpster_door.mp3" volume 1.2
        show sakana tutorial jojo pose1 with vpunch
        sakana "Rest assured that this tutorial is well made"
        show sakana tutorial jojo pose2
        sakana "Now lets send you back shall we?"
        jump .tutorial_menu_choice
    if tutorial.testingsakana == 3:
        show sakana angry 
        sakana "It's good to know that you are persisent"
        show sakana neutral
        sakana "A good game developer needs to be that in order to succeed"
        show sakana tutorial jojo pose2_point
        sakana "I like your enthusiam"
        play sound "<to 1.8>Effects/YT_Impacts/Dumpster_door.mp3" volume 1.2
        show sakana tutorial jojo pose2_wink with vpunch:
            zoom 2
            yalign 0.20
        sakana "Now lets stop wasting time and get back to the game"
        show sakana:
            zoom 1
        
        jump .tutorial_menu_choice
    if tutorial.testingsakana == 4:
        sakana "Perhaps we got off on the wrong foot?"
        play sound "<from 3.2 to 4>Effects/YT_Impacts/Dumpster_door.mp3" volume 1.2
        show sakana tutorial closeup armsdown with vpunch:
            zoom 1.5
        sakana "Allow me to explain"
        show sakana tutorial closeup handonchest
        sakana "I am here to get you introduced to the core concepts of this project and you just seem to be just messsing around"
        sakana "Why? What is compelling you to do something like this?"
        sakana "If it is something I'm doing atleast I can understand that"
        sakana "But so far I've only been asking you what you want to know"
        show sakana tutorial closeup pointatyou
        sakana "and it's you who has been messing around"
        menu:
            sakana "care to explain yourself?"
            "No":
                pass
        show sakana tutorial closeup armsdown
        sakana "I should have explected that to be honest"
        show sakana tutorial closeup pointup
        sakana "So I will say this only once more"
        show sakana tutorial closeup armsdown:
            linear 1.5 yalign 0.7
        pause 1.5
        play sound "<from 1.8 to 3.2>Effects/YT_Impacts/Dumpster_door.mp3" volume 1.2
        show sakana tutorial closeup fist with vpunch
        sakana "Knock it off"
        show sakana:
            zoom 1.0
        jump .tutorial_menu_choice
    if tutorial.testingsakana == 5:
        show sakana tutorial closeup armsdown
        sakana "Alright that's enough"
        sakana "You have wasted enough time"
        sakana "Seriously the developer can't make any more of these"
        sakana "So no more messing around"
        menu:
            sakana "Alright?"
            "No":
                pass
        sakana "I should have expected as much"
        sakana "let's see how you handle this then"
        $ tutorial.menuchoiceshowthatsallbutton = False
        jump .tutorial_menu_choice
    return
label .missclicked:
    sakana "Oh you misclicked huh?"
    play sound "<to 1.8>Effects/YT_Impacts/Dumpster_door.mp3" volume 1.2
    show sakana tutorial closeup armsdown with vpunch
    sakana "Hold on I can help with that"
    
    $ tutorial.menuchoiceshowthatsallbutton = False
    sakana "Alright lets try that again"
    jump .tutorial_menu_choice
    return

label .didntwanttochoose:
    sakana "excuse you? what do you mean that you didn't want to choose?"
    play music "<from 10>Music_Export/Dramatic/Dramatic_Swarm.mp3"  loop
    sakana "listen here you ... {nw=2}"
    play sound "<from 3.2 to 4>Effects/YT_Impacts/Dumpster_door.mp3" volume 1.2
    show sakana tutorial closeup armsdown with vpunch:
        xalign 0.5
    sakana "listen here you ... you..."
    
    play sound "Effects/YT_Doors/Wood_Door_Creak_Open.mp3" volume 1
    show sakana tutorial closeup armsdown:
        parallel:
            linear 1.0 zoom 2
        parallel:
            linear 1.0 yalign 0.5
    sakana "youre just trying to waste my time arent you?"
    sakana "yeah that has to be it"
    
    if tutorial.testingsakana >=4:
        jump .didntwanttochoosetwo
        
    sakana "well no matter. I'll just choose for you"
    $ tutorial_Project_basics.SetActive()
    $ tutorial_Project_framework.SetActive()
    $ tutorial_Project_art.SetActive()
    $ tutorial_Project_writing.SetActive()
    $ tutorial_Project_coding.SetActive()
    
    sakana "have fun learning everything"
    return
label .didntwanttochoosetwo:
    #sakana grabs the camera
    play sound "<to 1.8>Effects/YT_Impacts/Dumpster_door.mp3" volume 1.2
    show sakana tutorial closeup armsdown with vpunch
    sakana "Why else would you be messing around so much?"
    sakana "Testing my patience!"
    show sakana tutorial closeup armsdown:
        linear 1.0 zoom 2
    sakana "Going through the beginning menu so much?"
    sakana "You are just messing around!"
    sakana "You know what im going to do to you?"
    sakana "Have fun learning everything chump"
    hide sakana
    show sakana neutral at center
    play music "Music_Export/Calm/Clouds.mp3"  loop volume 0.8
    menu:
        sakana "Select what you want to learn about"
        "Tell me everything oh great master Sakanasan!":
            $ tutorial_Project_basics.SetActive()
            $ tutorial_Project_framework.SetActive()
            $ tutorial_Project_art.SetActive()
            $ tutorial_Project_writing.SetActive()
            $ tutorial_Project_coding.SetActive()
           
            pass
    return

label .pre_tutorial_skip:
    menu:
        "Skip":
            $ tutorial_Project_basics.SetActive()
            $ tutorial_Project_framework.SetActive()
            $ tutorial_Project_art.SetActive()
            $ tutorial_Project_writing.SetActive()
            $ tutorial_Project_coding.SetActive()
            
            $ tutorial_introduction.SetComplete()
            return
        "Continue":
            pass
    return

