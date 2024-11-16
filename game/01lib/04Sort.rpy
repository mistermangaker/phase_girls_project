
default system_taglist = [("nsfw",-1),("ecchi",-0.5),("tutorial",-10)]
default system_blacklist =["Placeholder1","Placeholder2"]
init python:
    class Mission_sort:
        
        def sort_mission_by_metadata(activemissionlist,taglist,blacklist = None):
            temp_activemissionlist = activemissionlist
            temptuple = []
            templist = []
            #this is used to pre filter out unwanted missions via the ai story teller. meant to be a sudo nsfw filter for players who dont want that
            if blacklist:
                for i in temp_activemissionlist:
                    for a in i.metadata:
                        for b in blacklist:
                            if a.lower() == b[0].lower():
                                temp_activemissionlist.remove(i)
                            else:
                                pass

            #step 1 get a mission and look at its metadata
            #step2 assign that metadata to a variable
            #step3 compare that metadata to the taglist and see if its in it
            #if it is add its value to the value variable
            #step4 put the mission and its value in a tuple list

            for i in temp_activemissionlist:
                #print(i.jumplabel)
                value = 0
                for a in i.metadata:
                    #print(a)
                    for b in taglist:
                        #print(a,b[0])
                        if a.lower() == b[0].lower():
                            #print("foundtag"+b[0])
                            value += b[1]
                            break
                temptuple.append((i,value))  
            temptuple.sort(key=lambda tup: tup[1])  
            for i in temptuple:
                templist.append(i[0])
            return templist
            
            

        def assign_actors_to_mission(sortedmissionlist):
            #we copy the active list to a temporary list just for this function
            templist = sortedmissionlist
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


        class Story_teller:
            def __init__(self,taglist,blacklist):
                self.taglist = taglist
                self.blacklist = blacklist
                pass