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
    #sakana Jojo poses
    "before we continue artists, writers, coders"

    "know! your! rights!"

    "all visual assets of this game are licensed under the “creative commons share alike license” which grants the right to all people to use, remix, and redistribute derivative works of these assets under the same license"

    "that means is that by committing art to this project you give others working on this project the right to, reuse, copy, trace, modify, or add to, your art for the purposes of adding more content to this project or any current or future forks of this project so long as it is long as those projects are not for commercial gain."

    "What that means is that. people can use or modify your shit. so if that doesn't sit right with you it would be advisable not to contribute to this project."

    "Given that this project is an unlicensed fan game based on the intellectual property of  phase connect llc. we don't necessarily have any copyright to what we are making anyway. "

    "hence why the actor mission framework this game is based on is a wholly separate project licensed under the MIT license."

    "Coders it's recommended that you do the same for whatever unique mechanics you want to develop, or contribute to the actor mission framework directly "

    "we will go over the acceptable content and the forking of this project to form your own version."

    "As the main fork of this project. We as the main development team have an obligation to set a good example and run and moderate this project as well as reasonably possible. It is for that reason we will have these rules set out from the beginning for contributing to the project. "

    "Naturally this means we will have to be selective about what we accept into the project. This however does not mean that we will attempt to or even have the ability to stop any forks or overhauls of this project by other 3rd party sources. This is an open source project and as such we encourage any and all who want to make their own fork of this project or update their version with code from this project. "

    "rules for contributing code and other in game assets"

    "If you wish to contribute code, modules, assets, or music which you do not own. you absolutely have to make sure that 1 the asset is under an MIT, creative commons license or equivalent. 2 if not under the previous that the rights holder is aware of its intended use and the fact that it will be redistributed for free. 3 that the original source of the code, asset, or music is placed in the proper credits section. "

    "you can not contribute code, assets, or music if they do not fit those criteria. even if the original assets were paid for. "

    "especially if the original assets were paid for. Most commercial licenses do not allow for the redistribution of the paid for intellectual property in an open source format."

    "if the code or assets you provided do not fit those criteria. unfortunately they will not be allowed to be contributed or they will be removed if they had been previously contributed."



    return




label tutorial_Project_framework:
    #option 2 actor framework basics
    "the absolute basics of the actor missions framework goes as follows. "

    "each in-game “day” is divided into 3 parts. “morning”, “midday”, and “night” as of alpha 1 morning and night are just the beginning and end of code that runs the gameplay loop. and are trigger points for special missions."

    "but in future they will potentially have further uses."

    #show code here
    "you declare a mission object like so:"


    "there are two types of missions story and special "

    "special missions are directly triggered by code while story missions are sorted and displayed on the mission select screen"
    "The story mission object has many attributes the most important structurally are."

    "jump label. location, activation date, actor list, display information. along with the less important attributes of author, credits, tags, and chapter." 

    "along with the attributes completed and type which just let's the game know if it's completed or not and which type of mission it is."

    "These will be the beginning where the game will jump to begin the mission. note each one of these has to be unique. these are internal references only and won't be seen. it should be at the very start of the mission. "

    "treat them like a mission ID and only have one global label per mission and have all other labels be local labels. "

    "For more information about that will be provided in the “about writing” mission"

    "location is very simple. is a tag that let's the game know which where the start of the mission should take place. "

    "the actor mission framework only allows for one mission to take place in one location per day. with other missions being sorted so only missions that take place in other locations can be shown."

    "activation date is the day in total game days that the mission will get activated and be added to the pool of available missions. "

    "it can be used to have missions become available after certain number of days have passed in game or happen on a particular day. "

    "But usually it's used to with the function “delay_activation_date” to make a mission only become available a set number of days after whatever triggered it "

    "a more in depth explanation of all the functions will be provided in the “about writing” mission"

    "next up is actor list which is written as either a string of actors separated by commas like so “actor1,actor2,actor3” or as a python list \[“actor1”,”actor2”,”actor3”\] "

    "the actor list is a list of actors who will be present at the start of the mission. an actor can only be in one place at a time and sorted so missions with other actors will be displayed. "

    "will be used in conjunction with the location Tag ensures that only missions with unique actors and in unique locations are present at any given time."

    "this is to make sure less popular talents can also get screen time and missions aren't biased toward the most popular talents"

    "finally display information which has two attributes, title and body. this is the information that holds the title and the preamble that is displayed in the mission select screen."

    "Finally we are onto the mission metadata. which is used in sorting and organizing missions "

    ###this needs review###


    "author(s): a string or python list of one or more main authors of the mission. used for sorting and assigning credit."

    "format for strings “author1,author2,author3” format for python lists \[“author1”,“author2”,“author3”\]"

    "credits: a string or list of one or more contributors. used for sorting and assigning credit. "

    "format for strings separate the credits from the contributors with a ‘,’ and the credit + contributors with a comma"

    "an example would be:“music:bob,music:lia,art:john,background art:mike”"

    "format for python list separate the credit and the contributor with a ‘:’ "


    "an example would be:\[“music:bob”,”music:lia”,”art:john”,”background art:mike”\]"

    "The credits can be for whatever you like. "

    "next up are mission tags, which is a string or a python list of content tags that tell the game what the content of your mission will have. used for sorting and content classification purposes "

    "Finally there is the chapter which tells the game which groupings of missions should be made available for viewing used for Grouping missions by theme, special event or otherwise. "

    "Now that you've written your mission you might be noticing that it's kind of cluttered. there is a neater organization method for creating missions using XML files."
    menu:

        "Would you like an advanced tutorial about using xml files?"
        "yes":
            pass
        "no":
            pass

    #go to somewhere else for xml

    "next up and less exciting is declaring the special missions these special missions are declared as follows"

    "and have these attributes. jump label, activation day, chapter and activation tag. along with the attributes completed and type."

    "The only attribute which hasn't Been covered already is activation tag, which just tells the game whether it takes place in the morning or at night and they happen automatically based on a queue system."

    "future planned additions to the framework will contain: a system to assign actors to other places besides the starting location. add in unique ambient noises to the map and stories based on what other missions were happening that day and where the player currently is. additions to the over world map to display images on the world map holiday missions/chapters that display on certain in-game or real life days"


    return




label tutorial_Project_art:
    return




label tutorial_Project_writing:
#about writing 
    "in this section we will discuss labels, flow control, and using the actor missions framework to help direct the flow of these stories."

    "to start off with. the renpy game engine uses special names to use as the start of blocks of dialog called labels. "

    "a label contains all the dialogue, art, screens, and various code that the game will use for the story."

    "All labels and ingame variables have to be unique. with a single dev team this is decently easy to achieve. but with a large open source project like this. it will quickly get out of hand if everyone used generic labels and names for their stories and variables "

    "this is why we ask that all writes use renpy's “local label” feature to write all of their stories and only have a single global label that their mission points to in the code. "

    "it's very easy to do by just appending the name of your label with a period ‘.’ and making sure that the label is below the global label in the story rpy file you write it in."

    "the same with variables. so when writing your stories used one of pythons built in features called “namespace” to add in a prefix to your variables this will allow you have as many variables as you want without bothering other programmers "


    "For story specific displayables, event art and backgrounds, please place them in the same folder as the story.rpy file and not in the images folder (where generic images and characters will be placed) "

    "and for the displayable name prefix it with either the name of the story, or your name."

    "next we will talk about the custom functions that the actor mission framework provides."

    "SetActive(mission) and SetInactive(mission) \n activates or deactivates the provided mission. as you can imagine this is helpful for actually progressing the story along."
    
    "SetCompleted(mission)\n sets a mission as completed. just remeber that missions DO NOT automatically get set as completed when they are played. this is done for various reasons but primarily its for missions that are meant to be replayed"

    "Check_completed_all(*args) \n takes one or multiple missions as arguments and returns true if they are all completed"

    "Check_completed_percentage(threshold,*args) \n takes a number between 0 and 100 as the threshold and one or multiple missions as arguments and returns true if the percentage of the missions completed is above the specified percentage. "

    "used primarily for additional dialogue or choices in stories. or to conditionally enable other missions."

    "Conditional_activate(mission,*args) \n takes a mission and a list of other missions to check against as arguments. activates the specified mission if all provided missions are completed"

    "Conditional_activate_percentage(threshold,mission,*args) \n takes a number between 0 and 100 as the threshold. a mission to activate and a list of other missions to check against as arguments. activates the specified mission if all provided missions are completed"

    "SetActivationDate(mission,totaldays) Delayactive(mission,days) \n takes a single mission instance as an argument either sets the date in total days from the start of the game or activate it after a specified number of days. "

    "it's preferred if the missions are set an ambiguous amount of time apart from each other. as they are selected semi randomly so specifying definite amount of time will cause issues"

    "Priorityactive(specialmission)\n takes a single special mission as an argument and inserts it at the front of the special missions queue for whatever time of day it's set."

    "used primarily for special missions that need to be done that day. or immediately the following morning. (special mission queuing only takes place during the mornings to reduce unnecessary sorting. "


    return




label tutorial_Project_coding:
    return




label tutorial_Renpy_basics:
    return

