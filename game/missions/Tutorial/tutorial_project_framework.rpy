default tutorial_Project_framework = Story_Mission.mission_from_xml("tutorial_mission1.xml","tutorial3")


label tutorial_Project_framework:
    play music "Music_Export/Calm/Clouds.mp3"
    scene lumi_room day
    show lumi at left

    lumi "the absolute basics of the actor missions framework goes as follows. "

    lumi "each in-game “day” is divided into 3 parts. “morning”, “midday”, and “night” as of alpha 1 morning and night are just the beginning and end of code that runs the gameplay loop. and are trigger points for special missions."

    lumi "but in future they will potentially have further uses."

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
    lumi "then we are all set and you have learned the basics of a mission!"

    lumi "hopefully you found this section informative"
    #call .pre_tutorial_framework_mission_tutorial
    return

label .xmlbasics:
    lumi "this framework uses basic xml integration for more readable and organizable mission code"
    show example xmlmission
    lumi "to define a mission from xml use the following"
    hide example
    show tutorial_image xml_code_example_story at tutorial_right_codebox
    lumi "the xml code looks like this for story missions"
    show tutorial_image xml_code_example_special at tutorial_right_codebox
    lumi "and this is for special missions"
    lumi "note that this framework allows for storing mission data in the \"03data\" folder or you can specify an override location instead"

    lumi "all missions should be placed between the \"def\" tags. multiple missions go inside the main \"def\" tags"
    hide tutorial_image
    lumi "for the raw code look into the \"03data\" folder for a template you can copy and paste from"
    
    #just making double sure they don't show up in the mission pool
    $ example_mission1.SetComplete()
    $ special_mission_1.SetComplete()
    return


#this section is waiting on inbuilt mission creation tools before being finished
label .pre_tutorial_framework_mission_tutorial:
    menu:
        lumi "now that we have covered the basics should we give you a tutorial on making a mission from scratch?"
        "yeah":
            call .tutorial_framework_mission_tutorial
        "nah":
            pass

    return


###this still needs to be finished 
label .tutorial_framework_mission_tutorial:
    "mission creation tutorial"
    return


example xmlmission:
    default example_mission1 = Story_Mission.mission_from_xml("Mission_template.xml","mis1")
    default special_mission_1 = Special_Mission.mission_from_xml("Mission_template.xml","specmis1")

#code to prevent game crashes if example missions ever somehow get activated
label example_mission1:
    "you really shouldn't be here"
    $ example_mission1.SetComplete()
    jump endday

label special_mission_1:
    "you really shouldn't be here"
    $ special_mission_1.SetComplete()
    jump endday
