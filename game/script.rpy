#placeholder room to be used for placeholder scene transitions
image bg room = Solid('#606060')

#default placeholder main menu background
default default_background = MainMenus_background(bgm = "Music_Export/Calm/No.7 Alone With My Thoughts - Esther Abrami.mp3", backgroundimage="Backgrounds/MainMenu/sakana_background.png")

label start:
    
    if not persistent.debugmode:
        call introduction from _call_introduction
    
label daystart:
    scene bg room
    $ calendar.AddDay(1)
    $ instantiatespecialsqueue()
    $ launchspecials(specialsqueueday)
    #"lets see what is happening today in the phase connect household"
label activate:
    $ sort_missions_to_activelist()
    $ assign_actors_to_mission()
    #call screen mission_select_screen_2()
    call screen mission_select_screen()
    if _return != "aborted":
        $ renpy.call(_return)
label endday:
    scene bg room
    menu:
        "Today is [calendar.Output]"
        "Go to bed":
            pass
    $ launchspecials(specialsqueuenight)
    ""
    jump daystart

    return


