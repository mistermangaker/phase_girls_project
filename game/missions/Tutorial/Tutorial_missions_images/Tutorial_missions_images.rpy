image sakana tutorial jojo pose1:
    zoom 0.5
    "missions/Tutorial/Tutorial_missions_images/sakanapose1.png"

image sakana tutorial jojo pose2:
    zoom 0.5
    "missions/Tutorial/Tutorial_missions_images/sakanapose2.png"

image sakana tutorial jojo pose2_wink:
    zoom 0.5
    "missions/Tutorial/Tutorial_missions_images/sakanapose2_1.png"
    pause 2.0
    "missions/Tutorial/Tutorial_missions_images/sakanapose2_1_1.png"
    pause 0.5
    "missions/Tutorial/Tutorial_missions_images/sakanapose2_1.png"

image sakana tutorial jojo pose2_point:
    zoom 0.5
    "missions/Tutorial/Tutorial_missions_images/sakanapose2_1.png"

image sakana tutorial jojo pose3:
    zoom 0.5
    "missions/Tutorial/Tutorial_missions_images/sakanapose3.png"

#sakana close up

image sakana tutorial closeup armsdown:
    zoom 0.5
    "missions/Tutorial/Tutorial_missions_images/sakanapose4.png"

image sakana tutorial closeup pointup:
    zoom 0.5
    "missions/Tutorial/Tutorial_missions_images/sakanapose4_1.png"

image sakana tutorial closeup pointatyou:
    zoom 0.5
    "missions/Tutorial/Tutorial_missions_images/sakanapose4_4.png"


image sakana tutorial closeup fist:
    zoom 0.5
    "missions/Tutorial/Tutorial_missions_images/sakanapose4_3.png"

image sakana tutorial closeup handonchest:
    zoom 0.5
    "missions/Tutorial/Tutorial_missions_images/sakanapose4_2.png"


image sakana tutorial setdown:
    "missions/Tutorial/Tutorial_missions_images/sakana_setdown1.png"
    pause 5
    "missions/Tutorial/Tutorial_missions_images/sakana_setdown2.png"


image tutorial closeup background = Solid('#000000')

image sakana tutorial closeup grabandlift:
    "missions/Tutorial/Tutorial_missions_images/sakana_lift.png"

image sakana tutorial closeup grabanddrop:
    
    contains:
        "missions/Tutorial/Tutorial_missions_images/sakana_closeup/longsakana.png"
        ypos 1000
        easeout 1.5 ypos -120

    contains:
        "missions/Tutorial/Tutorial_missions_images/sakana_closeup/sakana_closeupscruff.png"
        





image sakana tutorial leanin_animation:
    
    "missions/Tutorial/Tutorial_missions_images/sakana_closeup/frame1.png"
    pause 0.1
    "missions/Tutorial/Tutorial_missions_images/sakana_closeup/frame2.png"
    pause 0.1
    "missions/Tutorial/Tutorial_missions_images/sakana_closeup/frame3.png"
    pause 0.1
    "missions/Tutorial/Tutorial_missions_images/sakana_closeup/frame4.png"
    pause 0.1
    "missions/Tutorial/Tutorial_missions_images/sakana_closeup/frame5.png"

image sakana turorial leanin_stare:
    "missions/Tutorial/Tutorial_missions_images/sakana_closeup/frame5.png"

image sakana turorial leanin_shake:
    xanchor 0.0
    "missions/Tutorial/Tutorial_missions_images/sakana_closeup/frame5.png"
    linear 0.1 xpos 5
    linear 0.1 xpos 0
    repeat
    
    






image tutorial_image layered_image_example:
    "missions/Tutorial/Tutorial_missions_images/game_image_folder.png"

image tutorial_image layered_image_example tenma_code:
    "missions/Tutorial/Tutorial_missions_images/layered_image.png"
image tutorial_image layered_image_example tenma_images:
    "missions/Tutorial/Tutorial_missions_images/layered_image2.png"

transform tutorial_right_codebox:
    xalign 0.9
    yalign 0.5

transform tutorial_left_codebox:
    xalign 0.1
    yalign 0.5



image tutorial_image xml_code_example_story:
    "missions/Tutorial/Tutorial_missions_images/mission_code_xml.png"

image tutorial_image xml_code_example_special:
    "missions/Tutorial/Tutorial_missions_images/mission_code_xml2.png"

example tenma_full_image:
    image tutorial_image tenma_full_image:
        zoom 0.5
        "missions/Tutorial/Tutorial_missions_images/tenma_totorial_full_image.png"
    


image tenma tutorial fullimage:
    "tenma"

image tutorial_image tenma yourownstyle:
    zoom 0.5
    "missions/Tutorial/Tutorial_missions_images/tenma_uniquestyle.png"

layeredimage tenmaupclose:
    yanchor 1.0
    zoom 0.8
    group tail:
        attribute wag default:
            "tutorial_tenma_tail_wag"
        attribute aggitated default:
            "tutorial_tenma_tail_agitated"
    always "missions/Tutorial/Tutorial_missions_images/tenma_closeup/backhair.png"
    always "missions/Tutorial/Tutorial_missions_images/tenma_closeup/bodybase.png"
    group emote:
        attribute annoyed:
            "missions/Tutorial/Tutorial_missions_images/tenma_closeup/emote_annoyed.png"
        attribute blindrage:
            "missions/Tutorial/Tutorial_missions_images/tenma_closeup/emote_blindrage.png"
        attribute confused:
            "missions/Tutorial/Tutorial_missions_images/tenma_closeup/emote_confused.png"
        attribute rage:
            "missions/Tutorial/Tutorial_missions_images/tenma_closeup/emote_rage.png"
        attribute grouchy:
            "missions/Tutorial/Tutorial_missions_images/tenma_closeup/emote_grouchy.png"
        attribute scary:
            "missions/Tutorial/Tutorial_missions_images/tenma_closeup/emote_scary.png"
        attribute distraught1:
            "missions/Tutorial/Tutorial_missions_images/tenma_closeup/emote_distraught1.png"
        attribute distraught2:
            "missions/Tutorial/Tutorial_missions_images/tenma_closeup/emote_distraught2.png"
        attribute distraught3:
            "missions/Tutorial/Tutorial_missions_images/tenma_closeup/emote_distraught3.png"
        attribute distraught4:
            "missions/Tutorial/Tutorial_missions_images/tenma_closeup/emote_distraught4.png"
        attribute distraught5:
            "missions/Tutorial/Tutorial_missions_images/tenma_closeup/emote_distraught5.png"
        attribute distraught6:
            "missions/Tutorial/Tutorial_missions_images/tenma_closeup/emote_distraught6.png"
        attribute distraught7:
            "missions/Tutorial/Tutorial_missions_images/tenma_closeup/emote_distraught7.png"
        attribute distraught8:
            "missions/Tutorial/Tutorial_missions_images/tenma_closeup/emote_distraught8.png"
        
    group arms:
        if_not ["highpoint","lowpoint","highgrab","lowgrab"]
        attribute crossed:
            "missions/Tutorial/Tutorial_missions_images/tenma_closeup/arms_crossed.png"
    
    group rightarm:
        attribute highpoint:
            "missions/Tutorial/Tutorial_missions_images/tenma_closeup/right_arm_upwardpoint.png"
        attribute lowpoint:
            "missions/Tutorial/Tutorial_missions_images/tenma_closeup/right_arm_droopypoint.png"

    group leftarm:
        attribute highgrab:
            "missions/Tutorial/Tutorial_missions_images/tenma_closeup/left_arm_highgrab.png"
        attribute lowgrab:
            "missions/Tutorial/Tutorial_missions_images/tenma_closeup/left_arm_lowgrab.png"
    
    group ears:
        attribute ears_neutral default:
            "missions/Tutorial/Tutorial_missions_images/tenma_closeup/ears_neutral.png"
        attribute ears_angry:
            "missions/Tutorial/Tutorial_missions_images/tenma_closeup/ears_angry.png"
        attribute ears_droop1:
            "missions/Tutorial/Tutorial_missions_images/tenma_closeup/ears_droop1.png"
        attribute ears_droop2:
            "missions/Tutorial/Tutorial_missions_images/tenma_closeup/ears_droop2.png"
      
image tutorial_tenma_tail_wag:
    "missions/Tutorial/Tutorial_missions_images/tenma_closeup/tail1.png"
    pause 1.0
    "missions/Tutorial/Tutorial_missions_images/tenma_closeup/tail2.png"
    pause 1.0
    "missions/Tutorial/Tutorial_missions_images/tenma_closeup/tail3.png"
    pause 1.0

image tutorial_tenma_tail_agitated:
    "missions/Tutorial/Tutorial_missions_images/tenma_closeup/tail1.png"
    pause 1.0
    "missions/Tutorial/Tutorial_missions_images/tenma_closeup/tail2.png"
    pause 1.0
    "missions/Tutorial/Tutorial_missions_images/tenma_closeup/tail3.png"
    pause 1.0
   

image tenmaupclose look_surprised1:
    "tenmaupclose distraught1 highpoint highgrab"
    pause 0.5
    "tenmaupclose distraught3 ears_droop2 highpoint highgrab" with dissolve
    pause 0.5
    "tenmaupclose distraught3 ears_droop1 lowpoint highgrab" 
    
image tenmaupclose look_surprised2:
    "tenmaupclose distraught4 ears_droop1 highpoint highgrab" 
    pause 0.4
    "tenmaupclose distraught3 ears_droop2 highpoint highgrab" 
    pause 0.1
    "tenmaupclose distraught4 ears_droop1 highpoint highgrab" 
    pause 0.3
    "tenmaupclose distraught3 ears_droop2 highpoint highgrab" 
   
image tenmaupclose look_surprised3:
    "tenmaupclose distraught5 lowpoint highgrab" with dissolve
    pause 0.2 
    "tenmaupclose distraught6 ears_angry lowpoint highgrab"
    pause 0.3
    "tenmaupclose distraught7 ears_droop1 lowpoint highgrab"
    pause 0.4
    "tenmaupclose distraught6 ears_angry lowpoint highgrab"
    pause 0.3
    "tenmaupclose distraught7 ears_droop1 lowpoint highgrab"

image tenmaupclose look_surprised4:
    "tenmaupclose distraught8 ears_droop2 lowpoint lowgrab"  with dissolve
    pause 0.4
    "tenmaupclose distraught2 ears_droop2 lowpoint lowgrab"
    pause 0.5
    "tenmaupclose distraught5 ears_droop2 lowpoint lowgrab" with dissolve
    pause 0.6
    "tenmaupclose annoyed ears_droop2 lowpoint lowgrab"
    pause 2.0
    "tenmaupclose grouchy ears_droop2 lowpoint lowgrab"
    
image tenmaupclose look_rage:
    "tenmaupclose distraught6 ears_angry highpoint highgrab"
    pause 0.2
    "tenmaupclose rage ears_angry highpoint highgrab"
    pause 0.2
    "tenmaupclose blindrage lowgrab ears_angry highpoint"
    pause 0.2
    "tenmaupclose rage lowgrab ears_angry highpoint"
    pause 0.2
    "tenmaupclose blindrage ears_angry highpoint highgrab"
