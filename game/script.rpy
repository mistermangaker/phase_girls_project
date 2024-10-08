#placeholder room to be used for placeholder scene transitions
image bg room = Solid('#606060')

label start:
    #call screen test()
    ""
    
    if not persistent.debugmode:
        jump introduction
    
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


