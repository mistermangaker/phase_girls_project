
        
screen mission_select_screen_buttons(room_mission,button_positions,button_image,default_info):
    #timer 0.5 action Function(test,"mission_select_screen_buttons",room_mission,button_positions,button_image,default_info)
    
    if room_mission:
        $ trueroombuttonname = button_image
        imagebutton auto trueroombuttonname focus_mask True:
            id "yeet"
            action Return(room_mission.jumplabel)
            #sensitive Return(room_mission.jumplabel)
            hovered SetScreenVariable("showing",True),SetScreenVariable("positions",button_positions),SetScreenVariable("focused",room_mission.information)
            unhovered SetScreenVariable("showing",False),SetScreenVariable("positions",(0,0)),SetScreenVariable("focused",["Room", "this is an ordinary nothing special room", "mt.png"])
    else:
        imagebutton auto button_image focus_mask True:
            id "uwu"
            hovered SetScreenVariable("showing",True),SetScreenVariable("positions",button_positions),SetScreenVariable("focused",default_info)
            unhovered SetScreenVariable("showing",False),SetScreenVariable("positions",(0,0)),SetScreenVariable("focused",["Room", "this is an ordinary nothing special room", "mt.png"])
            #sensitive NullAction()
            action NullAction()


screen mission_select_screen():
    on "show" action Play("sound","audio/mission_select_screen/Wind/Light_Breeze.mp3",fadein = 1 ,fadeout = 1,relative_volume=2)
    on "hide" action Stop("sound",fadeout = 1)
    
    #on 'show' action Play('music', "Music_Export/Calm/No.7 Alone With My Thoughts - Esther Abrami.mp3", relative_volume=1, fadein=1.0, if_changed=True, loop = True)
    default showing = False
    default positions = (0,0)
    default focused = ["Room", "this is an ordinary nothing special room", "mt.png"]
    frame:

        viewport: 
            #area (0, 0, 1920, 1000)
           
            edgescroll (250, 250) 
            
            
            child_size (2400, 1350)
            
            xinitial 0.5
            yinitial 0.5

            fixed:
                add   "Mission_select_screen/mission_select_screen.png" 
                default tenma_room = providemission_info("tenma_room")
                use mission_select_screen_buttons(tenma_room,(1000,200),"Mission_select_screen/bedroom1_%s.png",["Tenma's rooom", "this is an ordinary nothing special room", "mt.png"])

                default pippa_room = providemission_info("pippa_room")
                use mission_select_screen_buttons(pippa_room,(1160,200),"Mission_select_screen/bedroom2_%s.png",["Pippa's rooom", "this is an ordinary nothing special room", "mt.png"])
                        

                default bedroom3 = providemission_info("bedroom3")
                use mission_select_screen_buttons(bedroom3,(1320,200),"Mission_select_screen/bedroom3_%s.png",["empty room", "this is an ordinary nothing special room", "mt.png"])
                

                default bedroom4 = providemission_info("bedroom4")
                use mission_select_screen_buttons(bedroom4,(1440,200),"Mission_select_screen/bedroom4_%s.png",["empty room", "this is an ordinary nothing special room", "mt.png"])
                
                default bedroom5 = providemission_info("bedroom5")
                use mission_select_screen_buttons(bedroom5,(720,520),"Mission_select_screen/bedroom5_%s.png",["empty room", "this is an ordinary nothing special room", "mt.png"])
                
        
                default bedroom6 = providemission_info("bedroom6")
                use mission_select_screen_buttons(bedroom6,(850,520),"Mission_select_screen/bedroom6_%s.png",["empty room", "this is an ordinary nothing special room", "mt.png"])
        
                default bedroom7 = providemission_info("bedroom7")
                use mission_select_screen_buttons(bedroom7,(1240,520),"Mission_select_screen/bedroom7_%s.png",["empty room", "this is an ordinary nothing special room", "mt.png"])
                
                default bedroom8 = providemission_info("bedroom8")
                use mission_select_screen_buttons(bedroom8,(1440,520),"Mission_select_screen/bedroom8_%s.png",["empty room", "this is an ordinary nothing special room", "mt.png"])
                
            
                
                default bathroom = providemission_info("bathroom")
                use mission_select_screen_buttons(bathroom,(820,200),"Mission_select_screen/bathroom_%s.png",["empty room", "this is an ordinary nothing special room", "mt.png"])

                
                default entrance = providemission_info("entrance")
                use mission_select_screen_buttons(entrance,(1080,520),"Mission_select_screen/entrance_%s.png",["empty room", "this is an ordinary nothing special room", "mt.png"])
                
                default laundryroom = providemission_info("laundryroom")
                use mission_select_screen_buttons(laundryroom,(1600,520),"Mission_select_screen/laundryroom_%s.png",["empty room", "this is an ordinary nothing special room", "mt.png"])

                default garage = providemission_info("garage")
                use mission_select_screen_buttons(garage,(2020,820),"Mission_select_screen/garage_%s.png",["empty room", "this is an ordinary nothing special room", "mt.png"])
                
                default storage = providemission_info("storage")
                use mission_select_screen_buttons(storage,(1660,820),"Mission_select_screen/storage_%s.png",["empty room", "this is an ordinary nothing special room", "mt.png"])

                default livingroom = providemission_info("livingroom")
                use mission_select_screen_buttons(livingroom,(1900,500),"Mission_select_screen/livingroom_%s.png",["empty room", "this is an ordinary nothing special room", "mt.png"])

                default kitchen = providemission_info("kitchen")
                use mission_select_screen_buttons(kitchen,(1900,320),"Mission_select_screen/kitchen_%s.png",["empty room", "this is an ordinary nothing special room", "mt.png"])

                if tenma_room:
                    use select_buttonhover(tenma_room,1000,200)
                if pippa_room:
                    use select_buttonhover(pippa_room,1160,200) 
                if bedroom3:
                    use select_buttonhover(bedroom3,1320,200)
                if bedroom4:
                    use select_buttonhover(bedroom4,1440,200)
                if bedroom5:
                    use select_buttonhover(bedroom5,720,520)
                if bedroom6:
                    use select_buttonhover(bedroom6,850,520)
                if bedroom7:
                    use select_buttonhover(bedroom7,1440,520)
                if bedroom8:
                    use select_buttonhover(bedroom8,1440,520)
                if bathroom:
                    use select_buttonhover(bathroom,820,200)
                if entrance:
                    use select_buttonhover(entrance,1080,520)
                if laundryroom:
                    use select_buttonhover(laundryroom,1600,520)
                if kitchen:
                    use select_buttonhover(kitchen,1900,320)
                if livingroom:
                    use select_buttonhover(livingroom,1900,500)
                if storage:
                    use select_buttonhover(storage,1660,820)
                if garage:
                    use select_buttonhover(garage,2020,820)
            if showing:
                frame:
                    at transform:
                        alpha 0.0
                        linear 0.1 alpha 1.0
                    xysize(410,500)
                    pos positions
                    xoffset 100
                    xpadding 10
                    ypadding 10
                    vbox:
                        style_prefix "mission"
                        xalign 0.5
                        
                        #add "[focused[2]]":
                        #    xysize (400,100)
                        #    xalign 0.5
                        text "[focused[0]]":
                            style "mission_label_text"
                        text "[focused[1]]":
                            style "mission_text"
                #timer 0.1 action SetScreenVariable("trueshowing",True)
                #if trueshowing:
                    #use provide_mission_text(i = focused,positions=positions) 
            #else:
                #$ trueshowing = False
                #frame:
                    #xpos 1000 
                    #xysize (400,500)
                    #vbox:
                    #    text i.information[0]
                    #    text i.information[1]
                    #    add i.information[3]

    frame:
        ypos 1000  
        xysize (1920,80)
        has hbox
        spacing 10 
        text "[calendar.Output]" 
        textbutton "return":
            action Return("aborted")

        
image missionavailible_image = Ani_Gif("images/Mission_select_screen_icons/mission_available",pause = 0.1)
transform selectbounce:
    
    easein 0.5 ypos 10
    easeout 0.5 ypos 0

    repeat
transform selectbounce2:
    easein 0.5 ypos 12
    easeout 0.5 ypos -2
    repeat
screen select_buttonhover(mission,x,y):
    fixed:
        xpos x
        ypos y
        hbox:
            at selectbounce
            add "missionavailible_image"
            vbox:
                at selectbounce2
                default roomactors = findactors(mission.actors)
                for b in roomactors:
                    add b:
                        xysize(50,50)


style mission_label_text is gui_label_text
style mission_text is gui_text

style mission_text:
    xalign 0.5
    text_align 0.5
    size 15
style mission_label_text:
    xalign 0.5
    text_align 0.5


screen provide_mission_text_2(i,positions):
    timer 0.5 action Show("provide_mission_text_2",i,positions)


screen provide_mission_text(i,positions):
    
    default local_info = i
        
    modal True
    
    frame:
        
        at transform:
            alpha 0.0
            linear 0.1 alpha 1.0
        xysize(410,500)
        pos positions
        xoffset 100
        xpadding 10
        ypadding 10
        vbox:
            style_prefix "mission"
            xalign 0.5
            
            add "[local_info[2]]":
                xysize (400,100)
                xalign 0.5
            text "[local_info[0]]":
                style "mission_label_text"
            text "[local_info[1]]":
                style "mission_text"
                

                
            
    

            
            
