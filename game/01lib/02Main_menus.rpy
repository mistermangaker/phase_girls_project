default Main_menus_background = []
init python: 
    class MainMenus_background(object):
        def __init__(self, bgm = "Music_Export/Calm/No.7 Alone With My Thoughts - Esther Abrami.mp3", backgroundimage="mt.png"):
            self.bgm =bgm
            self.backgroundimage = backgroundimage
            Main_menus_background.append(self)


