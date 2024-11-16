define michiru = Character("michiru", image='michiru')
default michiru_actor = actors("michiru")

layeredimage michiru:
    zoom 0.5
    group backhat auto:
        attribute neutral default if_all['hat']
    group backhair auto:
        attribute down default
    group body auto:
        attribute base default
    group arms auto:
        attribute relaxed default
    group emote auto:
        attribute neutral default
        attribute pout
        attribute angry
        attribute sad
        attribute happy
        attribute smug
    group fronthat auto:
        attribute hat 

