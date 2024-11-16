default tutorial_introduction = Story_Mission.mission_from_xml("tutorial_mission1.xml","tutorial1")
default tutorial_Project_basics = Story_Mission.mission_from_xml("tutorial_mission1.xml","tutorial2")
default tutorial_Project_framework = Story_Mission.mission_from_xml("tutorial_mission1.xml","tutorial3")
default tutorial_Project_art = Story_Mission.mission_from_xml("tutorial_mission1.xml","tutorial4")
default tutorial_Project_writing = Story_Mission.mission_from_xml("tutorial_mission1.xml","tutorial5")
default tutorial_Project_coding = Story_Mission.mission_from_xml("tutorial_mission1.xml","tutorial6")
default tutorial_Project_writing_nightspecial = Special_Mission.mission_from_xml("tutorial_mission2.xml")



init python in tutorial:
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
    show sakana
    menu:
        "skip":
            $ tutorial_Project_basics.SetActive()
            $ tutorial_Project_framework.SetActive()
            $ tutorial_Project_art.SetActive()
            $ tutorial_Project_writing.SetActive()
            $ tutorial_Project_coding.SetActive()
            
            $ tutorial_introduction.SetComplete()
            return
        "continue":
            pass

    sakana "hello there and I am sakana and welcome to the game developer tutorial for “The Phase Connect Streamer House” "
    sakana "here I will explain everything you need to know about the basics for developing visual novels using this game open source framework, “the actor-missions framework” "
    sakana "Now you maybe wondering as to why I am here"
    menu:
        "Not Really":
            pass
            
    sakana "Well it's because the main artist is overworked and can't justify making more sprites that will only be used during the tuorial"
    sakana "So they will using character sprites that appear in game!"
    show sakana tutorial jojo pose1
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
    #*sakana Jojo poses*
    
    sakana "So if that is not the current build your are playing then this information may be..."
    #*sakana Jojo poses again* 
    show sakana tutorial jojo pose2 with vpunch 
       
    sakana "OUTDATED!"
    #*sakana points to a link on screen*
    show sakana tutorial jojo pose2_point
    sakana "Check the “wiki and documentation” for a full rundown of features and code as this tutorial is only the basics"
    show sakana neutral
    sakana "So uh now that is all out of the way. let's get into the lessons"
    
label .tutorial_menu_choice:
    show sakana neutral at right
    menu:
        sakana "What do you want to learn in this course and we will get to it"
        #option 1
        
        "Project basics about contribution and licensing " if not tutorial.menuchoice1:
            $ tutorial_Project_basics.SetActive()
            $ tutorial.menuchoice1 = True
            $ tutorial.menuchoiceshowthatsallbutton = True
            jump .tutorial_menu_choice
            
        #option 2
        "Game framework basics"if not tutorial.menuchoice2:
            $ tutorial_Project_framework.SetActive()
            $ tutorial.menuchoice2 = True
            $ tutorial.menuchoiceshowthatsallbutton = True
            jump .tutorial_menu_choice
            
        #option 3
        "Game Art and working with displayables"if not tutorial.menuchoice3:
            $ tutorial_Project_art.SetActive()
            $ tutorial.menuchoice3 = True
            $ tutorial.menuchoiceshowthatsallbutton = True
            jump .tutorial_menu_choice
        #option 4
        "Writing and working with renpy labels, flags, and flow control "if not tutorial.menuchoice4:
            $ tutorial_Project_writing.SetActive()
            $ tutorial.menuchoice4 = True
            $ tutorial.menuchoiceshowthatsallbutton = True
            jump .tutorial_menu_choice
        #option 5
        "Coding and developing features for the game"if not tutorial.menuchoice5:
            $ tutorial_Project_coding.SetActive()
            $ tutorial.menuchoice5 = True
            $ tutorial.menuchoiceshowthatsallbutton = True
            jump .tutorial_menu_choice
        #option 6
        
        #option 7
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
        $ tutorial.menuchoice7 = True#"[tutorial.menuchoice1] [tutorial.menuchoice2]  [tutorial.menuchoice3] [tutorial.menuchoice4] [tutorial.menuchoice5] [tutorial.menuchoice6]"
    if tutorial.menuchoice7:
        sakana "Wow you want to know everything huh?"
        
        sakana "How eager you are"
    if not tutorial.menuchoice1 and not tutorial.menuchoice2 and not tutorial.menuchoice3 and not tutorial.menuchoice4 and not tutorial.menuchoice5  and not tutorial.menuchoice7:
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
        show sakana tutorial jojo pose1
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
        show sakana tutorial jojo pose2_wink with vpunch:
            zoom 2
            yalign 0.20
        sakana "Now lets stop wasting time and get back to the game"
        show sakana:
            zoom 1
        
        jump .tutorial_menu_choice
    if tutorial.testingsakana == 4:
        sakana "Perhaps we got off on the wrong foot?"
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
        show sakana tutorial closeup fist with vpunch
        sakana "Knock it off"
        show sakana:
            zoom 1.0
        jump .tutorial_menu_choice
    if tutorial.testingsakana == 5:
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
           
            pass
    return







label tutorial_Project_basics:
    scene kitchen day
    show sakana
    #sakana Jojo poses
    sakana "before we continue artists, writers, coders"

    sakana "know! your! rights!"

    sakana "all visual assets of this game are licensed under the “creative commons share alike license” which grants the right to all people to use, remix, and redistribute derivative works of these assets under the same license"

    sakana "that means is that by committing art to this project you give others working on this project the right to, reuse, copy, trace, modify, or add to, your art for the purposes of adding more content to this project or any current or future forks of this project so long as it is long as those projects are not for commercial gain."

    sakana "What that means is that. people can use or modify your shit. so if that doesn't sit right with you it would be advisable not to contribute to this project."

    sakana "Given that this project is an unlicensed fan game based on the intellectual property of phase connect llc. we don't necessarily have any copyright to what we are making anyway. "

    sakana "hence why the actor mission framework this game is based on is a wholly separate project licensed under the MIT license."

    sakana "Coders it's recommended that you do the same for whatever unique mechanics you want to develop, or contribute to the actor mission framework directly "

    sakana "we will go over the acceptable content and the forking of this project to form your own version."

    sakana "As the main fork of this project. We as the main development team have an obligation to set a good example and run and moderate this project as well as reasonably possible. "
    sakana  "It is for that reason we will have these rules set out from the beginning for contributing to the project. "

    sakana  "Naturally this means we will have to be selective about what we accept into the project. "
    sakana "This however does not mean that we will attempt to or even have the ability to stop any forks or overhauls of this project by other 3rd party sources. "
    sakana "This is an open source project and as such we encourage any and all who want to make their own fork of this project or update their version with code from this project. "

    sakana "rules for contributing code and other in game assets"

    sakana "If you wish to contribute code, modules, assets, or music which you do not own. you absolutely have to make sure that 1 the asset is under an MIT, creative commons license or equivalent. 2 if not under the previous that the rights holder is aware of its intended use and the fact that it will be redistributed for free. 3 that the original source of the code, asset, or music is placed in the proper credits section. "

    sakana "you can not contribute code, assets, or music if they do not fit those criteria. even if the original assets were paid for. "

    sakana "especially if the original assets were paid for. Most commercial licenses do not allow for the redistribution of the paid for intellectual property in an open source format."

    sakana "if the code or assets you provided do not fit those criteria. unfortunately they will not be allowed to be contributed or they will be removed if they had been previously contributed."

    sakana "lastly, no ai generated assets are allowed to be contributed to the project. use the generic assets provided to you if you can't draw. "

    sakana "we don't want to cause drama between the contributors and using AI art offends a lot of artists, so they aren't allowed."

label .questions:
    menu:

        sakana "now any questions?"
        "Nope":
            jump .end
        "Tell me about the games vision":
            call .game_vision
        "What tools will we need to develop for the game?":
            call .tools
        "Why don't you look like that in real life?":
            call .insult_sakana
    return

label .game_vision:
    
    sakana "The current vision of the game is primarily for it to be a large collection of various short, semi unrelated stories that all take place in a fictional dormitory, or “streamer house” "

    sakana "The premise of this setting is primarily inspired by the consensus in the community that having all the girls in one location like this would cause chaos. "

    sakana "The goal of this project is to make the code as lightweight and modular as possible so that almost anyone can add content to the game without having to worry about others "

    sakana "This approach will hopefully side step the largest issue that shuts down community developed visual novels. which is having further development of the story grind to a halt because 1 or 2 people on the dev team aren't keeping up with the rest."

    sakana "With this approach anyone can add content to the game, disconnected from the rest of development. and are shown to the player via the games inbuilt story director."

    sakana "So you can work at your own pace, and then commit your work to the github repository once your mission is fully complete."

    sakana "Or if you decide you aren't a fan of making visual novels and don't want to finish developing whatever it is you are working on, you aren't slowing anyone else down or halting development in any way."

    sakana "The game is currently planned to focus on the streamer house, and what is going on inside it. This is primarily done to minimize the amount of assets needed to be created."

    sakana "If you want to potentially expand the amount of starting areas the game has then you are welcome to."

    sakana "Currently the streamer house has a dozen or so starting areas all inside of the house. primarily bedrooms and common areas."

    sakana "In the future, more floors are planned along with more areas outside of the house such as pools, and hotsprings on the property."

    sakana "These haven't been added yet due to them requiring the creation of additional area specific characters sprites, which would already triple the workload."
    call .questions 

label .tools:
    
    sakana "In order to contribute to this project you are required to have these basic tools."

    sakana "Github. otherwise known as git, and also github desktop. this includes a github account also."

    sakana "A text editor specifically designed for coding. I recommend visual studio code with the python and renpy extensions installed "

    sakana "You will need the renpy launcher also."

    sakana "Lastly you will need discord, and be apart of the development discord server, which is where all development of the game will be organized from."

    call .questions

###this still needs to be finished 
label .insult_sakana:
    "insult_sakana"
    return

###this still needs to be finished 
label .end:
    "That's all for now"
    "end"
    return



label tutorial_Project_framework:
    scene lumi_room day
    show lumi at left
    #option 2 actor framework basics
    lumi "the absolute basics of the actor missions framework goes as follows. "

    lumi "each in-game “day” is divided into 3 parts. “morning”, “midday”, and “night” as of alpha 1 morning and night are just the beginning and end of code that runs the gameplay loop. and are trigger points for special missions."

    lumi "but in future they will potentially have further uses."

    #show code here
    show example example_mission example_special
    lumi "you declare a mission object like so:"


    lumi "there are two types of missions story and special "

    lumi "special missions are directly triggered by code while story missions are sorted and displayed on the mission select screen"
    show example example_mission

    lumi "The story mission object has many attributes the most important structurally are."

    lumi "jump label. location, activation date, IsActive actor list, display information. along with the less important attributes of author, credits, tags, and chapter." 

    lumi "along with the attributes completed and type which just let's the game know if it's completed or not and which type of mission it is."

    lumi "These will be the beginning where the game will jump to begin the mission. note each one of these has to be unique. these are internal references only and won't be seen. it should be at the very start of the mission. "

    lumi "treat them like a mission ID and only have one global label per mission and have all other labels be local labels. "

    lumi "For more information about that will be provided in the “about writing” mission"

    lumi "location is very simple. is a tag that let's the game know where the start of the mission should take place. "

    lumi "the actor mission framework only allows for one mission to take place in one location per day. with other missions being sorted so only missions that take place in other locations can be shown."

    lumi "next up is actor list which is written a string of actors separated by commas like so “actor1,actor2,actor3”"

    lumi "the actor list is a list of actors who will be present at the start of the mission. an actor can only be in one place at a time and sorted so missions with other actors will be displayed. "

    lumi "will be used in conjunction with the location Tag ensures that only missions with unique actors and in unique locations are present at any given time."

    lumi "this is to make sure less popular talents can also get screen time and missions aren't biased toward the most popular talents"
    
    lumi "activation date is the day in total game days that the mission will get activated and be added to the pool of available missions. "

    lumi "it can be used to have missions become available after certain number of days have passed in game or happen on a particular day. "

    lumi "But usually it's used to with the function “delay_activation_date” to make a mission only become available a set number of days after whatever triggered it "
    
    lumi "a more in depth explanation of all the functions will be provided in the “about writing” mission"

    lumi "IsActive is used to detirmine if a mssion should be added to the mission pool. having it default to True means its active right away."
    
    lumi "this isnt recomennded. you should instead have your mission activate after a certain amount of days into the game"

    lumi "Then there is display information which has three attributes, title, body, and image. this is the information that holds the title and the preamble that is displayed in the mission select screen."

    lumi "Finally we are onto the mission metadata. which is used in sorting and organizing missions"

    
    lumi "author(s) declared with a list of strings. used for sorting and assigning credit to the writers of the mission."

    lumi "contributors are used for additional assistance like artists, musicians, proof readers, programmers etc"
    lumi "they are declared by a list of strings"

    lumi "next up are mission tags"

    lumi "these are for telling the ingame AI director what kind of content is in the mission, used for sorting and content classification purposes"

    lumi "it's declared also with a list of strings"

    lumi "Finally there is the chapter which tells the game which groupings of missions should be made available for viewing used for Grouping missions by theme, special event or otherwise."

    lumi "Now that you've written your mission you might be noticing that it's kind of cluttered. there is a neater organization method for creating missions using XML files."
    hide example 
    menu:

        lumi "Would you like an advanced tutorial about using xml files?"
        "yes":
            call .xmlbasics
        "no":
            pass

    #go to somewhere else for xml
    show example example_special
    lumi "next up and less exciting is declaring the special missions these special missions are declared as follows"

    lumi "and have these attributes. jump label, activation tag, activation date, chapter and along with the attributes completed and type."

    lumi "The only attribute which hasn't Been covered already is activation tag, which just tells the game whether it takes place in the morning or at night and they happen automatically based on a queue system."

    lumi "future planned additions to the framework will contain: a system to assign actors to other places besides the starting location"
    lumi "additions to the over world map to display images on the world map holiday missions/chapters that display on certain in-game or real life days"
    lumi "and hopefully many more!"
    hide example 
    menu:
        lumi "now that we have covered the basics should we give you a tutorial on making a mission from scratch?"
        "yeah":
            call .tutorial_framework_mission_tutorial
        "nah":
            pass
    lumi "then we are all set and you have learned the basics of a mission!"

    lumi "hopefully you found this section informative"

    return


###this still needs to be finished 
label .xmlbasics:
    lumi "this framework uses basic xml integration for more readable and organizable mission code"
    #show mission xml code here
    lumi "to define a mission from xml use the following"
    lumi "all missions should be placed between the \"def\" tags. multiple missions go inside the main \"def\" tags"
    "xml basics"
    return

###this still needs to be finished 
label .tutorial_framework_mission_tutorial:
    "mission tutorial"
    return



label tutorial_Project_art:
    scene tenma_room day
    show tenma
    tenma "Assets in this project are divided between core assets and mission specific assets. "

    tenma "There isn't any actual objective distinction between them, just that core assets are meant to be generic and meant to be used by all contributors. "

    tenma "Core image assets are found in the “images” folder of the game directory and the code repository for core assets is in the “characters” and “displayables” folders. "

    tenma "Core assets should have a short, generic name, and follow a consistent naming scheme similar to the rest of them"

    tenma "Whereas mission or contributor specific displayables should be in their own folder together."

    tenma "And they can have whatever naming scheme the contributor wants."

    tenma "If you want to make core assets to the game, they should be placed along with the other core assets."

    tenma "Do note that non core assets should be made unique to avoid conflicts with other code."

    tenma "So add either prefixes or suffixes of either your name, the mission they appear in, or both to the names of your displayables. "

    tenma "For example: tenma, tenma happy, or tenma sad are all generic displayables. "

    tenma "Making a new displayable and naming it tenma happy would cause code conflicts. "

    tenma "But naming it “tenma contributornamehere missionthree superduper happy” would not cause issues as it's unique in a way that it's very unlikely that anyone else would ever randomly pick that name"

    tenma "The more unique and descriptive your naming is, the easier it will be in the long run."

    tenma "This is done to keep things easily separated and modular."

    tenma "Like with the “tutorial” missions (that you are currently playing through) they have their own separate folder with code, assets, displayables, etc in the “missions” directory folder. "

    tenma "It contains images that should only will appear in this tutorial (though there is nothing that actually prevents them from appearing elsewhere) "

    tenma "For creating generic character assets the main format you should use is renpy's “layered image” displayables."

    tenma "We will assume that you are already familiar with the concept of them. they are just many different images stacked on top of eachother to make different combinations of poses."

    tenma "The layered images for characters can be found in the “characters” or “displayables” folders. "

    tenma "As for the artsyle of the game. The artstyle is loosely a flat semi cellshaded artstyle"

    tenma "When making generic assets, please attempt to keep the art style similar to the current art style the generic assets currently have"

    tenma "As for mission specific assets like character art, or event art. any style is perfectly fine. "

    tenma "In fact , we encourage you to make your work visually and stylistically unique. this includes even making your own versions of already made generic assets to better fit the art style you are going for."

    return

example example_mission hide:
    default examplemission = Story_Mission(jumplabel = "examplemission",location = "tenma_room", actors = "tenma,pippa",activationdate = None,IsActive=False,author=["mistermangaker"],contributors=["None"],tags=["tutorial"],chapter = "one", information=["The First Example Mission", "meant to show you how the code works","mt.png"])
example example_special hide:
    default example_specialmission = Special_Mission(jumplabel ="example_specialmission", activationtag = "day", activationdate = None , IsActive = False ,author =["mistermangaker"],contributors= ["None"],tags= ["None"],chapter="one")

default examplemission2 = Story_Mission(jumplabel = "examplemission2",location = "pippa_room", actors = "tenma,pippa",activationdate = None,IsActive=False,author=["mistermangaker"],contributors=["None"],tags=["tutorial"],chapter = "one", information=["The First Example Mission", "meant to show you how the code works","mt.png"])
#code to prevent game crashes if example missions ever somehow get activated
label examplemission:
    "you really shouldn't be here"
    $ examplemission.SetComplete()
    jump endday
label examplemission2:
    "you really shouldn't be here"
    $ examplemission2.SetComplete()
    jump endday
label example_specialmission:
    "you really shouldn't be here"
    $ example_specialmission.SetComplete()
    jump endday

label tutorial_Project_writing:
#about writing 
    scene shiina_room day
    show shiina at right
    $ reset_example()
    shiina "in this section we will discuss labels, flow control, and using the actor missions framework to help direct the flow of these stories."
    show example label_1    
    example:
        label example_label: 
    shiina "to start off with. the renpy game engine uses special names to use as the start of blocks of dialog called labels. shown as so:"
    
    shiina "a label contains all the dialogue, art, screens, and various code that the game will use for the story."
    example: 
        label another_example_label:
            shiina "hi there"
    hide example 
    shiina "All labels and ingame variables have to be unique. with a single dev team this is decently easy to achieve. but with a large open source project like this. it will quickly get out of hand if everyone used generic labels and names for their stories and variables "

    shiina "this is why we ask that all writes use renpy's “local label” feature to write all of their stories and only have a single global label that their mission points to in the code. "

    shiina "it's very easy to do by just appending the name of your label with a period ‘.’ and making sure that the label is below the global label in the story rpy file you write it in."

    shiina "the same with variables. so when writing your stories used one of pythons built in features called “namespace” to add in a prefix to your variables this will allow you have as many variables as you want without bothering other programmers "

    shiina "For story specific displayables, event art and backgrounds, please place them in the same folder as the story.rpy file and not in the images folder (where generic images and characters will be placed) "

    shiina "and for the displayable name prefix it with either the name of the story, or your name."

    shiina "next we will talk about the custom functions that the actor mission framework provides."
    show example missions
    example:
        $ examplemission.SetActive()
        $ examplemission.SetInactive()
    shiina "SetActive() and SetInactive() \n activates or deactivates the provided mission. as you can imagine this is helpful for actually progressing the story along."
    example:
        $ examplemission.SetComplete()
    shiina "SetComplete()\n sets a mission as completed. just remeber that missions DO NOT automatically get set as completed when they are played. this is done for various reasons but primarily its for missions that are meant to be replayed"
    example:
        if Mission.Check_completed_all(examplemission2,tutorial_introduction):
            pass

    shiina "Check_completed_all(*args) \n takes one or multiple missions as arguments and returns true if they are all completed"
    example:
        if Mission.Check_completed_percentage(100,examplemission,tutorial_introduction):
            pass
            
    shiina "Check_completed_percentage(threshold,*args) \n takes a number between 0 and 100 as the threshold and one or multiple missions as arguments and returns true if the percentage of the missions completed is above the specified threshold. "

    shiina "used primarily for additional dialogue or choices in stories. or to conditionally enable other missions."

    example: 
        $ examplemission.Conditional_activate(tutorial_introduction,examplemission2)
    shiina "Conditional_activate(*args) \n takes a mission and a list of other missions to check against as arguments. activates the specified mission if all provided missions are completed"
    example: 
        $ examplemission.Conditional_activate_percentage( 100,tutorial_introduction, examplemission2)
    shiina "Conditional_activate_percentage(threshold,*args) \n takes a number between 0 and 100 as the threshold. a mission to activate and a list of other missions to check against as arguments. activates the specified mission if all provided missions are completed"
    example:
        $ examplemission.SetActivationDate(99)
        $ examplemission.Delayactive(99)
    shiina "SetActivationDate(totaldays) Delayactive(days) \n takes a single mission instance as an argument either sets the date in total days from the start of the game or activate it after a specified number of days. "

    shiina "it's preferred if the missions are set an ambiguous amount of time apart from each other. as they are selected semi randomly so specifying definite amount of time will cause issues"
    #this example code activates the tutorial_Project_writing_nightspecial mission
    example:
        $ tutorial_Project_writing_nightspecial.Priorityactive()
    shiina "Priorityactive()\n takes a single special mission as an argument and inserts it at the front of the special missions queue for whatever time of day it's set."

    shiina "used primarily for special missions that need to be done that day. or immediately the following morning. (special mission queuing only takes place during the mornings to reduce unnecessary sorting. "
    
    hide example
    # used so these dont show up in the mission pool accidentally
    $ examplemission.SetComplete()
    $ examplemission2.SetComplete()
    menu: 
        shiina "now that we have gone over the basics. Would you like to set up your first mission?"
        "yeah":
            call .mission_tutorial
        "nah":
            pass
    shiina "Then you are all set!"
    shiina "Thank you for listening to me yap!"
    return
label .mission_tutorial:
    "mission creation tutorial"
    return

label tutorial_Project_writing_nightspecial:
    scene shiina_room night
    show shiina
    shiina "Rawr!"
    shiina "Ha! scared you didn't I?"
    shiina "this here is a special mission"
    shiina "special missions occur either in the mornins or at night and cant be selected by the player"
    shiina "their intended use cases are for situations just like this"
    shiina "randomly have the player get sent to a new mission"
    shiina "im sure you can think of a few ideas of how to use this."
    shiina "they use all the same code as regular missions also"

    shiina "pretty cool huh?"
    shiina "that's all there is to learn about special missions currently"
    $ tutorial_Project_writing_nightspecial.SetComplete()

    return


label tutorial_Project_coding:
    scene pippa_room day
    show pippa
    pippa "this section is less of an explanation of mechanics and code and more for core development principles"

    pippa "The main idea behind this project is to be modular, and data driven. "

    pippa "As a general rule of thumb your code should work in a decentralized fashion. and have the ability for a contributor to drag and drop in content or mods into the game directory without having to edit any files and it just works."
    pippa "as a developer for this project you will need to keep in mind that you are not developing code for making a game. you are developing a framework for others to make a game."

    pippa "so you will be required to produce clean, easily readable, well documented, and clearly labeled code complete with intended use cases and copy and pastable example code for the wiki."
    pippa "This is a rule that will be strictly enforced."

    pippa "the people who will using your code are the what we will call the “creative types”"

    pippa "otherwise known as cavemen."

    pippa "They are extremely likely to be amateur programmers and will struggle when working with unfamiliar code."

    pippa "so to make their lives (and by extension your and the main developer's lives) much easier. Thorough documentation along with step by step instructions for using the code should be standard. "

    pippa "creating templates for intended use cases will also be helpful."

    pippa "I say this because the renpy document doesn't do this, and it causes so many headaches trying to figure out what functions do and the correct syntaxes to use them."

    pippa "this means you end up spending twice as long reading documentation and experimenting with code, than you do actually programming your project."


    pippa "as for naming schemes for your code and functions. your first instinct is to be simple and succinct with your function names."

    pippa "don't do this."

    pippa "doing this can make your code ambiguous. especially to someone who isn't a coder, or someone with bad memory."

    pippa "Make your function names descriptive. "

    pippa "It's not 1999 anymore, we have auto complete, we can have longer function names."

    pippa "It saves more time and frustration to be able to read the function name and know what it does, than having to constantly go to the wiki to double check."


    return





