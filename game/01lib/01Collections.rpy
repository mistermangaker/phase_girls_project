#a list containing all the stystem actors
default system_actorslist = []

#a list for the current game save holding a conjoined list holding both special and story missions
default alltype_missions_list_repository = []
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
# a list of all chapters
default system_chapters_repository = []
