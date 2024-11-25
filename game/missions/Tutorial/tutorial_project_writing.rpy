default tutorial_Project_writing = Story_Mission.mission_from_xml("tutorial_mission1.xml","tutorial5")
default tutorial_Project_writing_nightspecial = Special_Mission.mission_from_xml("tutorial_mission2.xml","special1")




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
    play music "Music_Export/Calm/Clouds.mp3" 
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
    show shiina crossed
    shiina "it's very easy to do by just appending the name of your label with a period ‘.’ and making sure that the label is below the global label in the story rpy file you write it in."

    shiina "the same with variables. so when writing your stories used one of pythons built in features called “namespace” to add in a prefix to your variables this will allow you have as many variables as you want without bothering other programmers "

    shiina "For story specific displayables, event art and backgrounds, please place them in the same folder as the story.rpy file and not in the images folder (where generic images and characters will be placed) "
    show shiina relaxed 
    shiina "and for the displayable name prefix it with either the name of the story, or your name."
    show shiina happy
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
    show shiina happy
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
    show shiina neutral
    shiina "it's preferred if the missions are set an ambiguous amount of time apart from each other. as they are selected semi randomly so specifying definite amount of time will cause issues"
    #this example code activates the tutorial_Project_writing_nightspecial mission
    example:
        $ tutorial_Project_writing_nightspecial.Priorityactive()
    shiina "Priorityactive()\n takes a single special mission as an argument and inserts it at the front of the special missions queue for whatever time of day it's set."

    shiina "used primarily for special missions that need to be done that day. or immediately the following morning. (special mission queuing only takes place during the mornings to reduce unnecessary sorting. "
    show shiina crossed
    hide example
    # used so these dont show up in the mission pool accidentally
    $ examplemission.SetComplete()
    $ examplemission2.SetComplete()

    return

# to be done later when the proper code is put in place
label .mission_tutorial_question:    
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
    show shiina neutral
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

