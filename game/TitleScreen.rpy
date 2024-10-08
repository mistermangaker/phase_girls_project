screen Quick_story_title(author = None,title = None,subtext = None,credit = None,displayimage = "gui/quick_title_background.png", music= "Music_Export/Calm/No.7 Alone With My Thoughts - Esther Abrami.mp3" , music_volume = 1,looped =True,time =10.0):
    if music:
        on 'show' action Play('music', music, relative_volume=music_volume, fadein=1.0, if_changed=True, loop = looped)
    timer time action Return()
    frame:
        if displayimage:
            add displayimage:
                xalign 0.5
        
        xysize (1920,1080)
        vbox:
            xalign 0.5
            yalign 0.5
           
            if title:
                text "{size=+20}[title]":
                    xalign 0.5
            if subtext:
                text "{size=+10}[subtext]":
                    xalign 0.5
            if author:
                text "written by: [author]":
                    xalign 0.5
            if credit:
                text "[credit]":
                    xalign 0.5
                