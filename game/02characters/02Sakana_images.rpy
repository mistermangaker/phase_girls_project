define sakana = Character("Sakana", image='sakana')
default sakana_actor = actors("sakana", "Mission_select_screen_icons/sakana_icon.png")

layeredimage sakana:
    zoom 0.5
    group fararm auto:
        attribute relaxed default
    group emote auto:
        attribute neutral default
        attribute angry
        attribute embarassed
        attribute sad
    group neararm auto:
        attribute relaxed default
    

