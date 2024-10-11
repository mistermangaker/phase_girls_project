default pippa_actor = actors("pippa")

define pippa  = Character("Pippa", image='pippa')
layeredimage pippa:
    zoom 0.5
    group hair auto:
        attribute back default
    group body auto:
        attribute bare default
        attribute jacket
    group bangs auto:
        attribute down default
    group emote auto:
        attribute content default
    group arms:
        attribute jacket_up if_all['jacket']:
            "pippa_arms_jacket_up"
            
image pippa_jacket:
    "pippa jacket jacket_up" 

