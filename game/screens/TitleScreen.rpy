#titles screens go here
## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu
default gui.main_menu_background = "gui/main_menu.png"
#placeholder for any links the game should have either discord, github, twitter ect
screen additionallink():
    hbox:
        #background None
        #xysize(800,150)
        yalign 0.95 
        xalign 0.35
        spacing 10
        frame:
            yalign 1.0
            xysize (100,100)
        frame:
            yalign 1.0
            xysize (100,100)
        frame:
            yalign 1.0
            xysize (100,100)
        frame:
            yalign 1.0
            xysize (100,100)
            

screen main_menu():
    $ t = renpy.random.choice(Main_menus_background)
    on 'show' action Play('music', t.bgm, relative_volume =1, fadein=1.0, if_changed=True)
    on "hide" action Stop("music",fadeout = 1)
    
    
    ## This ensures that any other menu screen is replaced.
    tag menu

    add gui.main_menu_background
    add t.backgroundimage:
        xalign 1.0
        yalign 1.0
    
    #use additionallink
        
    vbox:
        spacing 10
        vbox:
            frame:
                xysize (610,340)
                xoffset 20
                background None
                
                add "gamelogo.png":
                    xalign 0.5
                    yalign 0.5
                    xysize(600,300)

                text "[config.version]":
                    xalign 0.9
                    yalign 1.0
            text "An Unofficial Fan Game":
                xalign 0.5

        vbox:
            xoffset 70
            yoffset 10
            style_prefix "main_menu"
            
            textbutton _("Start") action Start()
            if persistent.debugmode:
                    textbutton _("Quick Start") action ShowMenu("quick_launch")
            textbutton _("Load") action ShowMenu("load")
            textbutton _("Preferences") action ShowMenu("preferences")
            textbutton _("About") action ShowMenu("about")
            textbutton _("Quit") action Quit(confirm=not main_menu)



            


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_button:
    xysize (350, 100)
    background "gui/button/mainmenu_button_idle.png"
    hover_background "gui/button/mainmenu_button_hovered.png"   
style main_menu_button_text:
    xalign 0.5
    yalign 0.5


style main_menu_vbox:
    spacing 10
    xalign 0.2
    yalign 0.65


style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")
    textalign 0.5

style main_menu_version:
    properties gui.text_properties("version")


