default tutorial_introduction = Story_Mission.mission_from_xml("tutorial_mission1.xml","tutorial1")
default tutorial_Project_basics = Story_Mission.mission_from_xml("tutorial_mission1.xml","tutorial2")
default tutorial_Project_framework = Story_Mission.mission_from_xml("tutorial_mission1.xml","tutorial3")
default tutorial_Project_art = Story_Mission.mission_from_xml("tutorial_mission1.xml","tutorial4")
default tutorial_Project_writing = Story_Mission.mission_from_xml("tutorial_mission1.xml","tutorial5")
default tutorial_Project_coding = Story_Mission.mission_from_xml("tutorial_mission1.xml","tutorial6")
default tutorial_Renpy_basics = Story_Mission.mission_from_xml("tutorial_mission1.xml","tutorial7")


init python in tutorial:
    menuchoice1 = False
    menuchoice2 = False
    menuchoice3 = False
    menuchoice4 = False
    menuchoice5 = False
    menuchoice6 = False
    menuchoice7 = False
    menuchoiceshowthatsallbutton = True
    testingsakana = 0
    justclicked = False
    justclickedtext = ""

define maindev = Character("Main Developer")
label tutorialintro_start:
    scene entrance day
    show sakana
    sakana "hello there and I am sakana and welcome to the game developer tutorial for “The Phase Connect Streamer House” "
    sakana "here I will explain everything you need to know about the basics for developing visual novels using this game open source framework, “the actor-missions framework” "
    sakana "Now you maybe wondering as to why I am here"
    menu:
        "Not Really":
            pass
            
    sakana "Well it's because the main artist is overworked and can't justify making more sprites that will only be used during the tuorial"
    sakana "So they will using character sprites that appear in game!"
    #show sakana is a jojo pose
    sakana "BUT DON'T WORRY"
    sakana "WITH ENOUGH EFFORT ANYTHING IS POSSIBLE"
    sakana "I PLAN ON WASTING AS MUCH OF THEIR PROFESSIONAL TIME AS POSSIBLE!!"
    sakana "now let's make their job difficult"
    sakana "before we begin this tutorial is for “alpha 1” of the game."
    #*sakana Jojo poses*
    sakana "So if that is not the current build your are playing then this information may be..."
    #*sakana Jojo poses again* 
    sakana "OUTDATED!"
    #*sakana points to a link on screen*
    sakana "check the “wiki and documentation” for a full rundown of features and code as this tutorial is only the basics"
label .tutorial_menu_choice:
    menu:
        sakana "So tell me. what do you want to learn in this course and we will get to it"
        #option 1
        
        "project basics aka licensing and legal jargon" if not tutorial.menuchoice1:
            $ tutorial_Project_basics.SetActive()
            $ tutorial.menuchoice1 = True
            $ tutorial.menuchoiceshowthatsallbutton = True
            jump .tutorial_menu_choice
            
        #option 2
        "actor framework basics"if not tutorial.menuchoice2:
            $ tutorial_Project_framework.SetActive()
            $ tutorial.menuchoice2 = True
            $ tutorial.menuchoiceshowthatsallbutton = True
            jump .tutorial_menu_choice
            
        #option 3
        "art aka working with displayables"if not tutorial.menuchoice3:
            $ tutorial_Project_art.SetActive()
            $ tutorial.menuchoice3 = True
            $ tutorial.menuchoiceshowthatsallbutton = True
            jump .tutorial_menu_choice
        #option 4
        "writing aka working with labels flags and flow control "if not tutorial.menuchoice4:
            $ tutorial_Project_writing.SetActive()
            $ tutorial.menuchoice4 = True
            $ tutorial.menuchoiceshowthatsallbutton = True
            jump .tutorial_menu_choice
        #option 5
        "coding aka developing features for the game"if not tutorial.menuchoice5:
            $ tutorial_Project_coding.SetActive()
            $ tutorial.menuchoice5 = True
            $ tutorial.menuchoiceshowthatsallbutton = True
            jump .tutorial_menu_choice
        #option 6
        "renpy basics aka why are you playing this tutorial instead of the built in tutorial" if not tutorial.menuchoice6:
            $ tutorial_Renpy_basics.SetActive()
            $ tutorial.menuchoice6 = True
            $ tutorial.menuchoiceshowthatsallbutton = True
            jump .tutorial_menu_choice
        #option 7
        "all" if not tutorial.menuchoice1 or not tutorial.menuchoice2 or not tutorial.menuchoice3 or not tutorial.menuchoice4 or not tutorial.menuchoice5 or not tutorial.menuchoice6:
            $ tutorial_Project_basics.SetActive()
            $ tutorial_Project_framework.SetActive()
            $ tutorial_Project_art.SetActive()
            $ tutorial_Project_writing.SetActive()
            $ tutorial_Project_coding.SetActive()
            $ tutorial_Renpy_basics.SetActive()
            $ tutorial.menuchoice7 = True
            pass
        "thats all" if tutorial.menuchoiceshowthatsallbutton:
            pass

label .tutorial_afterscreen:

    if tutorial.menuchoice1 and tutorial.menuchoice2 and tutorial.menuchoice3 and tutorial.menuchoice4 and tutorial.menuchoice5 and tutorial.menuchoice6:
        $ tutorial.menuchoice7 = True
    #"[tutorial.menuchoice1] [tutorial.menuchoice2]  [tutorial.menuchoice3] [tutorial.menuchoice4] [tutorial.menuchoice5] [tutorial.menuchoice6]"
    if tutorial.menuchoice7:
        sakana "Wow you want to know everything huh?"
        
        sakana "How eager you are"
    if not tutorial.menuchoice1 and not tutorial.menuchoice2 and not tutorial.menuchoice3 and not tutorial.menuchoice4 and not tutorial.menuchoice5 and not tutorial.menuchoice6 and not tutorial.menuchoice7:
        #if tutorial.testingsakana > 1
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
            $ tutorial.justclickedtext = "care to explain why?"
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
        sakana "*Ahem* Rest assured that this tutorial is well made"
        sakana "Now lets send you back shall we?"
        jump .tutorial_menu_choice
    if tutorial.testingsakana == 3:
        sakana "It's good to know that you are persisent"
        sakana "A good game developer needs to be that in order to succeed"
        sakana "I like your enthusiam"
        jump .tutorial_menu_choice
    if tutorial.testingsakana == 4:
        sakana "Perhaps we got off on the wrong foot?"
        sakana "Allow me to explain"
        sakana "I am here to get you introduced to the core concepts of this framework and you just seem to be messsing around"
        sakana "why? whats compelling you to do something like this?"
        menu:
            sakana "care to explain yourself?"
            "No":
                pass
        sakana "I should have explected that to be honest"
        sakana "So I will say this only once more"
        sakana "knock it off"
        jump .tutorial_menu_choice
    if tutorial.testingsakana == 5:
        sakana "Alright that's enough"
        sakana "You have wasted enough time"
        sakana "Seriously the developer can't make any more of these"
        sakana "so no more messing around"
        $ tutorial.menuchoiceshowthatsallbutton = False
        jump .tutorial_menu_choice
    return
label .missclicked:
    sakana "Oh you misclicked huh?"
    sakana "Hold on I can help with that"
    $ tutorial.menuchoiceshowthatsallbutton = False
    sakana "Alright lets try that again"
    jump .tutorial_menu_choice
    return

label .didntwanttochoose:
    sakana "excuse you? what do you mean that you didn't want to choose?"
    sakana "listen here you ... you..."
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
    $ tutorial_Renpy_basics.SetActive()
    sakana "have fun learning everything"
    return
label .didntwanttochoosetwo:
    #sakana grabs the camera
    sakana "Why else would you be messing around so much?"
    sakana "Testing my patience!"
    sakana "Going through the beginning menu so much?"
    sakana "You are just messing around!"
    sakana "You know what im going to do to you?"
    sakana "Have fun learning everything chump"
    menu:
        sakana "Select what you want to learn about"
        "Tell me everything oh great master Sakanasan!":
            $ tutorial_Project_basics.SetActive()
            $ tutorial_Project_framework.SetActive()
            $ tutorial_Project_art.SetActive()
            $ tutorial_Project_writing.SetActive()
            $ tutorial_Project_coding.SetActive()
            $ tutorial_Renpy_basics.SetActive()
            pass
    return







label tutorial_Project_basics:
    return




label tutorial_Project_framework:
    return




label tutorial_Project_art:
    return




label tutorial_Project_writing:
    return




label tutorial_Project_coding:
    return




label tutorial_Renpy_basics:
    return

