define lumi = Character("lumi", image='lumi')
default lumi_actor = actors("lumi", "Mission_select_screen_icons/lumi_icon.png")

layeredimage lumi:
    zoom 0.5
    group body auto:
        attribute dress default
    group arms auto:
        attribute held default
        attribute relaxed 
    group emote auto:
        attribute neutral default
        attribute angry
        attribute sad
        attribute happy
        attribute smug
        attribute verysmug


