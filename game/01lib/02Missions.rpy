init -10 python:
    import collections
    import math
    #this is the game list that the mission objescts are added to automatically when a new missions object is created
    class Mission(object):
        def __init__(self, jumplabel: str, activationdate: int, IsActive: bool):
            self.jumplabel = jumplabel
            #jumplabel is the label that the game sends you to when the mission is selected on the mission select screen
            self.IsActive = IsActive
            #isactive refers to whether or not the mission will appear in the availible mission pool for the mission select screen to show
            self.activationdate = activationdate
            self.completed = False
            self.type = "Base"
            alltype_missions_list_repository.append(self)

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
            SetActive()
            

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
        def __init__(self, jumplabel: str, activationdate: int, location: str, actorsstring, IsActive: bool,information = ["title","information about the mission","mt.png"]):
            super().__init__(jumplabel,activationdate,IsActive)
            self.location = location
            self.actorsstring = actorsstring
            self.type = "story"
            self.information = information
            missionslist_repository.append(self)
         
        
        """
        functions
        usuage: missionname.functionname()
        """
        @property
        def actors(self):
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
            super().__init__(jumplabel,activationdate,IsActive)
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

#a list for the current game save holding a conjoined list holding both special and story missions
default alltype_missions_list_repository = [ ]

#a list for the current game save holding all story missions
default missionslist_repository = [ ]      
#a list for the current game save holding only the currentl active story missions
default currently_active_missions_list = [ ]  
#a list for the current game save holding only missions that are selected for the current day
default todays_selected_missions = [] 

#a list for the current game save holding all special missions
default specialmissionslist_repository = [ ] 

#a deque for the current save that holds a the special missions queued to be triggered in the morning before the main mission select screen
default specialsqueueday = collections.deque([])
#a deque for the current save that holds a the special missions queued to be triggered at night after the day has ended
default specialsqueuenight = collections.deque([])

        
       


            

