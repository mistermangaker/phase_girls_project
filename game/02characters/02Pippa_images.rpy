default pippa_actor = actors("pippa")

define pippa  = Character("Pippa", image='pippa')
layeredimage pippa:
    zoom 0.5
    group hair auto:
        attribute back default
    group outfit auto:
        attribute base default
    group emote auto:
        attribute neutral default
        attribute annoyed
        attribute angry
        attribute sad
        attribute happy
        attribute veryhappy
        attribute smug
    group arms auto:
        attribute up 
        attribute down default

            

