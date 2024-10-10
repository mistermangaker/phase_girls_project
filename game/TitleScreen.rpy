#titles screens go here
## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

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

    ## This empty frame darkens the main menu.
    frame:
        style "main_menu_frame"

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation

    if gui.show_name:

        vbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 0.9
    xoffset -30
    xmaximum 1200
    yalign 0.1
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")
    textalign 0.5

style main_menu_version:
    properties gui.text_properties("version")


