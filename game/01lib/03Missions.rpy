init -10 python:
    import collections
    import math
    
    #this is the game list that the mission objescts are added to automatically when a new missions object is created
    class Mission(object):
        
        def __init__(self, jumplabel: str, activationdate: int, IsActive: bool,author =["None"],contributors= ["None"],tags= ["None"],chapter="one"):
            self.jumplabel = jumplabel
            #jumplabel is the label that the game sends you to when the mission is selected on the mission select screen
            self.IsActive = IsActive
            #isactive refers to whether or not the mission will appear in the availible mission pool for the mission select screen to show
            self.activationdate = activationdate
            self.completed = False
            self.type = "Base"
            self.contributors = contributors 
            self.tags = tags
            self.author = author
            self.chapter = chapter
            alltype_missions_list_repository.append(self)
        
        @property
        def author(self):
            return self._author
            pass
        @author.setter
        def author(self,value):
            if not value:
                self._author = ["None"]
            if isinstance(value,(str)):
                self._author = value.split(',')
            else:
                self._author = value
        @property
        def tags(self):
            return self._tags
            pass
        @tags.setter
        def tags(self,value):
            if not value:
                self._tags = ["None"]

            if isinstance(value,(str)):
                self._tags = value.split(',')
            else:
                self._tags = value
        @property
        def contributors(self):
            return self._contributors
            pass
        @contributors.setter
        def contributors(self,value):
            if not value:
                self._contributors = ["None"]

            if isinstance(value,(str)):
                self._contributors = value.split(',')   
            else:
                self._contributors = value
                
        
        def SetActivationDate(self, Totaldays):
            """
            SetActivationDate(Totaldays)
            #sets the date in total days var "calendar.Totaldays" for this mission to automatically activate
            """
            self.activationdate = Totaldays
        def Delayactive(self, days):
            """
            Delayactive(days)
            #sets the date in total days var "calendar.Totaldays" + inputed number for this mission to automatically activate
            """
            self.activationdate = days + calendar.Totaldays
        def SetInactive(self):
            """
            SetInactive()
            sets the mission as inactive. inactive missions will not be randomly selected in the mission select screen. used in cases where a certian decision or action will remove a
            """
            self.activationdate = None
            self.IsActive = False
        def SetActive(self):
            """
            SetActive()
            sets the mission as active. active missions will be randomly selected in the mission select screen.
            """
            self.activationdate = 0
            self.IsActive =True
        def Complete(self):
            """
            Complete()
            does the same thing as 'SetInactive()' but also sets the mission as complete.
            """
            self.IsActive = False
            self.activationdate = None
            self.completed = True

        def Conditional_activate(self,*missions):
            for i in missions:
                if not i.completed:
                    return False
            self.activationdate = 0
            self.IsActive =True
            return True

        def Conditional_activate_percentage(threshold,self,*missions):
            whole = 0
            notcompleted = 0
            for i in missions:
                whole += 1
                if not i.completed:
                    notcompleted +=1
            ratio = 100*float(notcompleted)/float(whole)
            if ratio >= threshold:
                self.activationdate = 0
                self.IsActive =True
            else:
                return False
            
            

        @staticmethod
        def Check_completed_all(*missions):
            """
            Check_completed_all(*missions)
            takes in the instances of several other missions and checks to see if they are all completed. if all are completed then it returns true. 
            used in cases where you would want to see if several other missions were completed without having to use long "if/else" chains
            """
            for i in missions:
                if not i.completed:
                    return False
            return True
            
    
        @staticmethod
        def Check_completed_percentage(threshold,*missions):
            """
            Check_completed_percentage(100,*missions)
            arguments: threshold float 0 to 100
            missions: mission instances
            takes in number between 1 and 100 and a list of missions as arguments
            checks to see what percentage of those missions are completed and if its higher than the threshold. it returns true
            """
            whole = 0
            notcompleted = 0
            for i in missions:
                whole += 1
                if not i.completed:
                    notcompleted +=1
            ratio = 100*float(notcompleted)/float(whole)
            if ratio >= threshold:
                return True
            else:
                return False

        
    
    class Story_Mission(Mission):
        """
        missions
        these are the main story missions of the game. this is what will show up on the main mission select screen
        ---
        variables:
        ---
        jumplabel
        type: string
        jumplabel is the label that the game sends the player to when the mission is selected on the mission select screen
        it is also treated like a unique id by the game. 
        ---
        location
        type: string
        this is the location tag that the game will use to determine what mission select area can use this mission
        activationdate
        type: integer or 'None'
        the activation date is the date in "calendar.Totaldays" that the mission will activate on. so a value of 7 will mean that after 7 days have passed ingame the mission will activate the next time the "check mission" code fires
        ---
        actors
        type: list of objects
        note: not a list os strings, its a list of other variables
        a list of actor objects to be used in sorting and displaying who is prsent at the start of the mission. used to prevent the same people from appearing in sveral places at once on the start screen
        ---
        IsActive
        type: boolean
        isactive refers to whether or not the mission will appear in the availible mission pool for the mission select screen to show
        ---
        """
        def __init__(self, jumplabel: str, activationdate: int, location: str, actors, IsActive: bool,author =["None"],contributors= ["None"],tags= ["None"],chapter="one",information = ["title","information about the mission","mt.png"]):
            super().__init__(jumplabel,activationdate,IsActive,author,contributors,tags,chapter)
            self.location = location
            self.actors = actors
            self.type = "story"
            self.information = information
            
            missionslist_repository.append(self)
            
        def __str__(self):
            
            return f"(jumplabel={self.jumplabel!r})"
        
        """
        functions
        usuage: missionname.functionname()
        """
                
        @property
        def actors(self):
            return self._actors
           
        @actors.setter
        def actors(self,value):
            if isinstance(value,(list)):
                self._actors = value
            newactorlist = []
            templist = value.split(',')
            for i in templist:
                for b in system_actorslist:
                    #print("checking"+b.actorname)
                    if i == str(b.actorname):
                        #print("appending to list")
                        newactorlist.append(b)
            self._actors = newactorlist

                
        @property
        def actors2(self):
            #print("starting actors")
            newactorlist = []
            templist = self.actorsstring.split(",")
            #print(templist)
            for i in templist:
                for b in system_actorslist:
                    #print("checking"+b.actorname)
                    if i == str(b.actorname):
                        #print("appending to list")
                        newactorlist.append(b)
            #print(newactorlist)
            return newactorlist
        @classmethod
        def mission_from_xml(cls,xml_path):
            import os
            from xml.etree import ElementTree
            
            if renpy.loadable('03data/'+xml_path):
                code_path = '03data/'+xml_path
            elif renpy.loadable(xml_path):
                code_path = xml_path
            else:
                raise Exception("can not find file: "+xml_path)
            
            f_name=(renpy.open_file(code_path))
            dom=ElementTree.parse(f_name)
            root = dom.getroot()
            

            
            jumplabel = dom.find('jumplabel').text
            activationdate = int(dom.find('activationdate').text)
            location = dom.find('location').text
            actors = ""
            for i in dom.findall("actors/li"):
                actors += str(i.text)+','
            dom.find('actors').text
            IsActive = bool(dom.find('IsActive').text)
            information = []
            information.append(dom.find('information/title').text)
            information.append(dom.find('information/body').text)
            information.append(dom.find('information/image').text)
            
            chapter = []
            for i in dom.findall("metadata/chapter/li"):
                chapter.append(i.text)
            
            authors = []
            for i in dom.findall("metadata/authors/li"):
                authors.append(i.text)
            
            contributors = []
            for i in dom.findall("metadata/contributors/li"):
                contributors.append(i.text)
        
            tags = []
            for i in dom.findall("metadata/tags/li"):
                tags.append(i.text)
            
            print(actors)
            print(authors)
            print (contributors)
            print (tags)
            print (chapter)

            

            
            return cls(jumplabel,activationdate,location,actors,IsActive,authors,contributors,tags,chapter,information,)
        
        
        
        pass

        def Appened_story_information(self,new_information):
            """
            pass in a list of two strings and an image
            """
            self.information = new_information
        
        
        


    


    class Special_Mission(Mission):
        """
        special missions
        ---
        variables:
        ---
        activationtag
        type: string
        either "day" or "night" chooses what time of the day the mission spawns at
        ---
        jumplabel
        type: string
        jumplabel is the label that the game sends the player to when the mission is selected on the mission select screen
        it is also treated like a unique id by the game. 
        ---
        activationdate
        type: integer or 'None'
        the activation date is the date in "calendar.Totaldays" that the mission will activate on. so a value of 7 will mean that after 7 days have passed ingame the mission will activate the next time the "check mission" code fires
        ---
        IsActive
        type: boolean
        isactive refers to whether or not the mission will appear in the availible mission pool for the mission select screen to show
        ---
        """
        def __init__(self, activationtag: str, jumplabel: str, activationdate: int, IsActive: bool):
            super().__init__(jumplabel,activationdate,IsActive,author,contributors,tags,chapter)
            self.activationtag = activationtag
            self.inserted = False
            specialmissionslist_repository.append(self)
            self.type = "special"
            
        """
        functions
        usuage: missionname.functionname()
        """
        def Priorityactive(self):
            """
            Priorityactive()
            immediately adds this mission to the start of the secial queue.
            used for special missions that have to be done next
            """
            self.activationdate = 0
            self.IsActive =True
            self.inserted = True
            if self.activationtag == "day":
                specialsqueueday.appendleft(self.jumplabel)
            if self.activationtag == "night":
                specialsqueuenight.appendleft(self.jumplabel)
    
    


    def activate_mission_by_date():
        """
        looks through the mission list and checks if a missions activation date has passed and the mission is not active.
        it also checks if the mission is diabled if the activation date is '-1' 
        """
        for i in missionslist_repository:
            if i.activationdate != None and not i.IsActive:
                if i.activationdate <= calendar.Totaldays:
                    i.SetActive


    def sort_missions_to_activelist():
        """
        clears the currently_active_missions_list and then refills it from all the missions in 
        missionslist_repository based on if they have been activated or if their activation date 
        has been reached.
        """
        activate_mission_by_date()
        currently_active_missions_list.clear()
        for i in missionslist_repository:  
            if i.activationdate != None and i.IsActive and not i.completed:
                currently_active_missions_list.append(i) 
        return 

    def assign_actors_to_mission():
        #we copy the active list to a temporary list just for this function
        templist = currently_active_missions_list
        #this filter list stores the names of all actors + all locations they take place in 
        #defaults to empty so the first mission selected is guaranteed to be allowed in
        filterlist = []
        for i in templist:
            #for each item in the temporary list we go through and combine the locations and actors from the mission object into
            #a single list called "combinedlist" for ease of evaluation
            discard = False
            combinedlist = []
            combinedlist.append(i.location)
            for b in i.actors:
                combinedlist.append(b)
            #combinedlist.extend(i.actors)
            #we then check to see if the any of the values from combinedlist and filterlist to see if any of the values match
            result = set(combinedlist) & set(filterlist)
            if result:
                # if a match is found the resulting entry is removed from the list
                templist.remove(i)
            elif not result:
                #if no match is found its combinedlist (its loction and actors) is added the the filterlist
                filterlist.extend(combinedlist)
        #the process is iterated over the entire active list until at the end we have narrored it down
        #to a handful of semi random missions which is then stored in the "todays_selected_missions"
        renpy.store.todays_selected_missions = templist
        return 

    def providemission_info(tag):
        """
        checks to see if a mission with the provided tag is in the curated list of missions
        """
        hasmission = False
        #thisbuttonmission = "ERROR_LABEL"
        for i in todays_selected_missions:
            if i.location == tag:
                hasmission = True
                thisbuttonmission =  i 
                break
        if hasmission:   
            return thisbuttonmission
        else:
            pass     


        return 
             
    def instantiatespecialsqueue():
        """
        looks through the mission list and checks if a missions activation date has passed and the mission is not active.
        it also checks if the mission is diabled if the activation date is '-1' 
        """
        for i in specialmissionslist_repository:
            if i.activationdate != None and i.IsActive:
                if not i.inserted and not i.completed:
                    i.inserted = True
                    if i.activationtag == "day":
                        specialsqueueday.append(i.jumplabel)
                    if i.activationtag == "night":
                        specialsqueuenight.append(i.jumplabel)
    

    
    def launchspecials(queue):
        """
        checks to see if the provided queue is empty. if it is it returns and does nothing
        if the queue is populated it takes the first item from that list and returns it
        """
        if not queue:
            return
        temp = queue[0]
        queue.popleft()
        renpy.call(temp)

    def provide_all_currently_active_missions_labels():
        currently_active_missions_list_labels.clear()
        for i in currently_active_missions_list:
            currently_active_missions_list_labels.append(i.jumplabel)
        return currently_active_missions_list_labels

    def provide_todays_selected_missions_labels():
        todays_selected_missions_labels.clear()
        for i in todays_selected_missions:
            todays_selected_missions_labels.append(i.jumplabel)
        return todays_selected_missions_labels



        
       


            

