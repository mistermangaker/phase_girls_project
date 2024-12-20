default tutorial_Project_basics = Story_Mission.mission_from_xml("tutorial_mission1.xml","tutorial2")




label tutorial_Project_basics:
    play music "Music_Export/Calm/Clouds.mp3" loop
    scene kitchen day
    show sakana
    #sakana Jojo poses
    sakana "welcome to the project basics lesson of the tutorial here we will discuss what you as a creator should expect when working on this project"
    show sakana tutorial jojo pose1
    sakana "before we continue artists, writers, coders"
    show sakana tutorial jojo pose1:
        yalign 1
        zoom 1.5
    sakana "know! your! rights!"
    show sakana tutorial jojo pose2 at default:
        zoom 1
    sakana "all visual assets of this game are licensed under the “creative commons share alike license” which grants the right to all people to use, remix, and redistribute derivative works of these assets under the same license"

    sakana "that means is that by committing art to this project you give others working on this project the right to, reuse, copy, trace, modify, or add to, your art for the purposes of adding more content to this project or any current or future forks of this project so long as it is long as those projects are not for commercial gain."
    show sakana tutorial closeup pointup
    sakana "What that means is that. people can use or modify your shit. so if that doesn't sit right with you it would be advisable not to contribute to this project."
    show sakana tutorial closeup armsdown
    sakana "Given that this project is an unlicensed fan game based on the intellectual property of phase connect llc. we don't necessarily have any copyright to what we are making anyway. "

    sakana "hence why the actor mission framework this game is based on is a wholly separate project licensed under the MIT license."

    sakana "Coders it's recommended that you do the same for whatever unique mechanics you want to develop, or contribute to the actor mission framework directly "

    sakana "we will go over the acceptable content and the forking of this project to form your own version."

    sakana "As the main fork of this project. We as the main development team have an obligation to set a good example and run and moderate this project as well as reasonably possible. "
    show sakana tutorial closeup pointup
    sakana  "It is for that reason we will have these rules set out from the beginning for contributing to the project. "

    sakana  "Naturally this means we will have to be selective about what we accept into the project. "

    sakana "This however does not mean that we will attempt to or even have the ability to stop any forks or overhauls of this project by other 3rd party sources. "
    
    sakana "This is an open source project and as such we encourage any and all who want to make their own fork of this project or update their version with code from this project. "

    sakana "rules for contributing code and other in game assets"

    sakana "If you wish to contribute code, modules, assets, or music which you do not own. you absolutely have to make sure that 1 the asset is under an MIT, creative commons license or equivalent. 2 if not under the previous that the rights holder is aware of its intended use and the fact that it will be redistributed for free. 3 that the original source of the code, asset, or music is placed in the proper credits section. "
    show sakana tutorial closeup handonchest
    sakana "you can not contribute code, assets, or music if they do not fit those criteria. even if the original assets were paid for. "

    sakana "especially if the original assets were paid for. Most commercial licenses do not allow for the redistribution of the paid for intellectual property in an open source format."

    sakana "if the code or assets you provided do not fit those criteria. unfortunately they will not be allowed to be contributed or they will be removed if they had been previously contributed."
    show sakana tutorial jojo pose2_point
    sakana "lastly, no ai generated assets are allowed to be contributed to the project. use the generic assets provided to you if you can't draw. "

    sakana "we don't want to cause drama between the contributors and using AI art offends a lot of artists, so they aren't allowed."

label .questions:
    show sakana tutorial jojo pose2
    menu:

        sakana "now any questions?"
        "Nope":
            jump .end
        "Tell me about the games vision":
            call .game_vision from _call_tutorial_Project_basics_game_vision
        "What tools will we need to develop for the game?":
            call .tools from _call_tutorial_Project_basics_tools
        "Why don't you look like that in real life?" if tutorial.sakana_mainquestions_firstviewing:
            $ tutorial.sakana_mainquestions_firstviewing = False
            call .insult_sakana from _call_tutorial_Project_basics_insult_sakana
    return

label .game_vision:
    show sakana neutral 
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
    call .questions from _call_tutorial_Project_basics_questions 

label .tools:
    show sakana neutral 
    sakana "In order to contribute to this project you are required to have these basic tools."
    if not config.developer:
        sakana "Since you aren't playing on this game through the renpy launcher its safe to assume you will be needing all of these"

    sakana "{a=https://github.com/}a github account{/a}. otherwise known as git, and also {a=https://desktop.github.com/download/}github desktop{/a}. this includes a github account also."

    sakana "A text editor specifically designed for coding. I recommend {a=https://code.visualstudio.com/}visual studio code{/a} with the python and renpy extensions installed "

    sakana "You will need the {a=https://renpy.org}Ren'Py launcher{/a} also."

    sakana "Lastly you will need discord, and be apart of the development discord server, which is where all development of the game will be organized from."

    sakana "Likewise the framework comes built in with a few features that come from enabling \"debug mode\"" 

    if not persistent.debugmode:
        $   renpy.notify("debugmode enabled")
        $ persistent.debugmode = True
        sakana "Speaking of which let's enable that right now" 
    
    sakana "Mainly \"Quick Launch\" in the main menu for quickly launching missions for testing."
    
    sakana "And then there is \"mission information\" that appears in the pause menu when you start a game, it allows you to change all the information about a mission for that particular save session"
    
    sakana "Mildly useful for testing things that depend on other missions being completed or not, but also it's a way for the end user fix softlocks or remove buggy or unwanted missions from the mission pool"
    
    sakana "You know, just simple quality of life things like that"
    
    sakana "That's all for the tools you will need"
    call .questions from _call_tutorial_Project_basics_questions_1

#"<from 5 to 15.5>waves.opus"
label .insult_sakana:
    
    play music "Music_Export/Dramatic/Toreador.mp3"  loop
    show sakana tutorial closeup armsdown with vpunch
    play sound "<from 0.15>Effects/YT_Impacts/Rock_Hits_Metal_Debris.mp3" volume 0.7
        
    sakana "HaHaHa That was hurtful!"
    play sound "Effects/YT_Impacts/Crash_Metal_Plate_Big_Room.mp3" volume 1
    scene tutorial closeup background
    show sakana tutorial closeup armsdown with vpunch:
        xalign 0.5
        zoom 1.5
        yalign 0.8
    sakana "Making fun of how people look is extremely {w=1}funny {w=1}isn't it?"
    play music "Effects/YT_SciFi/Sci_Fi_Vortex.mp3" loop
    show sakana tutorial closeup armsdown with vpunch:
        linear 0.1 zoom 2.5
        linear 0.1 yalign 0.5
    play audio "<from 0.9 to 1.9>Effects/YT_Foley/backpack jump.mp3"
    show sakana tutorial closeup grabandlift with vpunch:
        zoom 1.25
        linear 0.5 zoom 1
    pause 1.0
    #""
    show sakana tutorial closeup grabanddrop
    pause 1.5
    show sakana tutorial leanin_animation
        

    sakana "Listen to me child ..{w=0.5}.{w=0.5}.{w=0.5} One day you will meet someone you truely care about ..{w=0.5}.{w=0.5}.{w=0.5} deeply"
    show sakana turorial leanin_stare
    sakana "You two will grow close together,{w=1} maybe romantically maybe platonically"
    show sakana turorial leanin_shake
    sakana "Then one day, through your careless harshness, you will say something that will hurt them"
    sakana "You never meant anything by it.{w=1} It was just a bit of friendly banter.{w=1} Just some friendly roasting between you two"
    
    
    sakana "You just said it as a joke,{w=1} but what you said truly did hurt them"
    sakana "They will laugh it off and pretend it doesn't bother them"
    sakana "But in truth,{w=1} you hurt them.{w=1} Your words hurt them deeply"
    sakana "You will apologize, and they will tell you that they forgive you.{w=1} Hell they might even tell themseleves that they forgive you"
    show sakana turorial leanin_stare
    sakana "But from that day forth even if its only slightly, they will still see you differently"
    play audio [ "<silence 5>", "<from 0.9 to 1.9>Effects/YT_Foley/backpack jump.mp3" ] 

    show sakana tutorial setdown
    sakana ".{w=0.5}.{w=0.5}.{w=0.5} They don't hate you.{w=2} They don't want you to feel bad about it either.{nw=2} They just wish that you would choose your words more carefully next time"
    stop music fadeout 1
    sakana "... They don't hate you. They don't want you to feel bad about it either. They just wish that you would choose your words more carefully next time"
    show sakana tutorial closeup armsdown at default
    sakana "Likewise I don't hate you either.{w=2} Just be more careful with your words next time okay?"
    show sakana tutorial closeup pointatyou
    sakana "right good talk we had there"
    play music "Music_Export/Calm/Clouds.mp3" loop
    sakana "Back to buisness"
    scene kitchen day
    call .questions from _call_tutorial_Project_basics_questions_2 

###this still needs to be finished 
label .end:
    show sakana neutral 
    sakana "right then that should be just about everything covered then"
    sakana "hopefully this lesson was informative for you"
    sakana "be sure to read through the other lessons from everyone else"
    return


