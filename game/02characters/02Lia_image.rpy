define lia = Character("Lia", image='lia')
default lia_actor = actors("lia")

layeredimage lia:
    zoom 0.5
    group backhair auto:
        attribute down default
    group outfit auto:
        attribute normal default
    group emote auto:
        attribute neutral default
        attribute happy
        attribute sad
        attribute angry
        attribute smug
    group leftarm auto:
        attribute relaxed default
        attribute up
    group rightarm auto:
        attribute relaxed default
        attribute up
    

