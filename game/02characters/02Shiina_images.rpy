default shiina_actor = actors("shiina", "Mission_select_screen_icons/shiina_icon.png")
define shiina = Character("Shiina", image='shiina')

layeredimage shiina:
    zoom 0.5
    group backhair auto:
        attribute out default
    group body auto:
        attribute outfit1 default
    group arms auto:
        attribute relaxed default
        attribute crossed
    group emote auto:
        attribute neutral default
        attribute sad
        attribute angry
        attribute happy
        attribute smug
        attribute verysmug
        attribute pout