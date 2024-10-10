default shiina_actor = actors("shiina", "Mission_select_screen_icons/shiina_icon.png")
define shiina = Character("Shiina", image='shiina')

layeredimage shiina outfit1:
    group backhair auto:
        attribute out default
    group backarm auto:
        attribute backrelaxed default
    group body auto:
        attribute outfit1 default
    group frontarm auto:
        attribute frontrelaxed default
    group emote auto:
        attribute neutral default