



default tenma_actor = actors("tenma", "Mission_select_screen_icons/tenma_icon.png")
define tenma = Character("Tenma", image='tenma')
define tenma_pov= Character("Tenma",image="tenma_pov")
#image side tenma_pov content = "Characters/Tenma/Side_images/content.png"

#image tenma_talking_content = Movie("Characters/Tenma/Side_images/talking.mp4")
#image tenma_idle_content = Movie("Characters/Tenma/Side_images/idle.mp4")
layeredimage tenma:
    zoom 0.5
    group tail auto:
        attribute wag default
        attribute excited 
        attribute agitated 
        
    group emote auto:
        attribute content default
        attribute happy
        attribute sad 
        attribute annoyed
        attribute angry
    group ears auto:
        attribute up default
        attribute down 
        attribute surprised
    group body auto:
        attribute sweater default
    group arms auto:
        attribute side default
    #group hoodie auto:
    #    attribute base default:

#image tenma_emote_content:

image tenma_tail_wag:
    "Characters/Tenma/tenma_tail1.png"
    pause 0.25
    "Characters/Tenma/tenma_tail2.png"
    pause 0.25
    "Characters/Tenma/tenma_tail3.png"
    pause 5 
    repeat

image tenma_tail_excited:
    "Characters/Tenma/tenma_tail_excited_1.png"
    pause 0.05
    "Characters/Tenma/tenma_tail_excited_2.png"
    pause 0.05
    "Characters/Tenma/tenma_tail_excited_3.png"
    pause 0.05
    "Characters/Tenma/tenma_tail_excited_4.png"
    pause 0.05
    "Characters/Tenma/tenma_tail_excited_5.png"
    pause 0.05
    "Characters/Tenma/tenma_tail_excited_6.png"
    pause 0.05
    repeat

image side tenma_pov content = ConditionSwitch(
    "povyapping == True", "tenma_neutral_talking" , "povyapping == False", "tenma_neutral_idle", 
)
image tenma_neutral_talking= Ani_Gif("images/Characters/Tenma/Side_images/tenma_neutral_talking",pause = 0.1)
image tenma_neutral_idle = Ani_Gif("images/Characters/Tenma/Side_images/tenma_neutral_idle",pause = 0.1)

image side tenma_pov angry = ConditionSwitch(
    "povyapping == True", "tenma_angry_talking" , "povyapping == False", "tenma_angry_idle", 
)
image tenma_angry_talking= Ani_Gif("images/Characters/Tenma/Side_images/tenma_angry_talk",pause = 0.1)
image tenma_angry_idle = Ani_Gif("images/Characters/Tenma/Side_images/tenma_angry_idle",pause = 0.1)

