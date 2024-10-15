define uruka = Character("Uruka", image='uruka')
default uruka_actor = actors("uruka", "Mission_select_screen_icons/uruka_icon.png")

layeredimage uruka:
    zoom 0.5
    group backhair auto:
        attribute down default
    group fararm auto:
        attribute relaxed default
    group body auto:
        attribute normal default
    group neararm auto:
        attribute onhip default
    group emote auto:
        attribute neutral default
