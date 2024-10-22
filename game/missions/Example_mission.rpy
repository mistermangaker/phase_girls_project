#default examplemission = Story_Mission("examplemission",0, "tenma_room","tenma,pippa",True,information=["The First Example Mission", "meant to show you how the code works","mt.png"],)
#default examplemission2 = Story_Mission("examplemission2",0, "pippa_room","shiina",True)
default examplespecialmission1 = Special_Mission("night", "examplespecialmission1", None, True,["mistermangaker"])
    
#default examplemission3 = Story_Mission.mission_from_xml_testing("example_mission3.xml",'mis1')
#default examplemission4 = Story_Mission.mission_from_xml_testing("example_mission3.xml",'mis2')
#default examplemission5 = Story_Mission.mission_from_xml("example_mission5.xml")
#default examplemission6 = Story_Mission.mission_from_xml("example_mission6.xml")
#default examplemission7 = Story_Mission.mission_from_xml("example_mission7.xml")



label example_mission3:
    $ examplemission4.SetActive()
    "yeah3"
    $ examplemission3.SetComplete()
    return
label example_mission4:
    #$ examplemission7.SetActive()
    "yeah4"
    $ examplemission4.SetComplete()
    return
label example_mission5:
    "yeah5"
    $ examplemission5.Complete()
    return
label example_mission6:
    "yeah6"
    $ examplemission6.Complete()
    return
label example_mission7:
    "yeah7"
    $ examplemission7.Complete()
    return






init python in mistermanagker_examplemissions:
    flag1 = 1
    flag2 = 2
    flag3 = 3


label examplemission:
    call screen Quick_story_title(title= "example mission", subtext = "part one", author = "mistermangaker",music_volume = 0.2) 
    scene pippa_room day
    show pippa jacket jacket_up at left
    show tenma at right 
    

    "[mistermanagker_examplemissions.flag1]"
    "[mistermanagker_examplemissions.flag2]"
    "[mistermanagker_examplemissions.flag3]"
    $ mistermanagker_examplemissions.flag3 =4
    ""
    menu:
        "greet":
            call .greetlabel from _call_examplemission_greetlabel
        "insult":
            call .insultlabel from _call_examplemission_insultlabel

    "this is a normal interaction between you two"
    $ examplemission.Complete()
    jump endday
label .greetlabel:
    tenma "hey"
    pippa "hey"
    return
label .insultlabel:
    tenma "fuck you"
    pippa "fuck you too"
    $ examplespecialmission1.Priorityactive()
    return

label examplemission2:
    call screen Quick_story_title(title= "example mission", subtext = "part two", author = "mistermangaker") 
    scene living_room day
    show pippa jacket jacket_up at left
    show tenma at right 
    "living room"
    $ examplemission2.Complete()
    jump endday

label examplespecialmission1:
    scene pippa_room night
    "this is the special mission"
    show tenma angry
    tenma "fuck you"
    $ examplespecialmission1.Complete()
    jump endday