default Main_menus_background = []
init python: 
    class MainMenus_background(object):
        def __init__(self,identifier,label = "label", icon ="mt.png", backgroundimage="mt.png"):
            self.identifier = identifier
            self.backgroundimage = backgroundimage
            self.label = label
            self.icon = icon
            Main_menus_background.append(self)

        @classmethod
        def returnitembyid(cls,identifier):
            for i in Main_menus_background:
                if i.identifier == identifier:
                    return i

default default_background = MainMenus_background(identifier="defaultbackground1",label= "Sakana's phone call",icon ="Mission_select_screen_icons/sakana_icon.png" ,backgroundimage="Backgrounds/MainMenu/sakana_background.png")
default persistent.mainmenu_object = "defaultbackground1"

