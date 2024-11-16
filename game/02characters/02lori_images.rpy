define lori = Character("lori", image='lori')
default lori_actor = actors("lori")


layeredimage lori:
    zoom 0.5
    group hair auto:
        attribute neutral default
    group outfit auto:
        attribute base default
    group emote auto:
        attribute neutral default
        attribute angry
        attribute sad
        attribute happy
        attribute smug
    group arms auto:
        attribute clasped 
        attribute relaxed default

            

