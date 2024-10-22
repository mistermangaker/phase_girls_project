define nasa = Character("Nasa", image='nasa')
default nasa_actor = actors("nasa")

layeredimage nasa:
    zoom 0.5
    group tail auto:
        attribute relaxed default
    group fararm auto:
        attribute relaxed default
    group body auto:
        attribute normal default
    group neararm auto:
        attribute relaxed default
    group emote auto:
        attribute neutral default


