default system_actorslist = []
init python:
    class actors(object):
        def __init__(self, actorname, portrait="mt.png",currentlocation = None, defaultlocation = None):
            self.actorname =actorname
            self.portrait = portrait
            self.currentlocation = currentlocation
            self.defaultlocation = defaultlocation
            if self.portrait == "mt.png" or None:
                find_default_actor_portrait(self)
            
            for i in system_actorslist:
                if self.actorname == i.actorname:
                    raise Exception("actor " + str(self.actorname) + " appears in 'system_actorslist' twice. double check that there are no duplicate names in your code as this will cause errors later")
            
            
            system_actorslist.append(self)
            
    def findactors(mission_actorlist):
        actorportrait = []
        temp_mission_actorlist = []
        for c in mission_actorlist:
            temp_mission_actorlist.append(c.actorname)
        for i in temp_mission_actorlist:
            for b in system_actorslist:
                if i == b.actorname:
                    actorportrait.append(b.portrait)
        return actorportrait
    
    def find_default_actor_portrait(actor):
        """
        if no custom portrait overide is given. this code will search for a portrait in "images/Mission_select_screen_icons/" for an image with the actors name + the suffix _icon.png 
        if none is found it keeps the default of "mt.png" which is a missing texture icon
        """
        filetosearchfor = 'images/Mission_select_screen_icons/'+actor.actorname + '_icon.png'
        if renpy.exists(filetosearchfor): 
            actor.portrait = filetosearchfor
        return


