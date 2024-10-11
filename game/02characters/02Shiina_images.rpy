default shiina_actor = actors("shiina", "Mission_select_screen_icons/shiina_icon.png")
define shiina = Character("Shiina", image='shiina')

layeredimage shiina:
    zoom 0.5
    group backhair auto:
        attribute out default
    group backarm auto:
        attribute relaxed default
    group body auto:
        attribute outfit1 default
    group frontarm auto:
        attribute relaxed default
    group emote auto:
        attribute neutral default