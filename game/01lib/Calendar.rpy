init python:
    import math
        
    class Calendar(object):
        def __init__ (self, Days, Day, Months, Month, Weekdays, Monthdays, Totaldays):
            self.Days = Days
            self.Day = Day
            self.Months = Months
            self.Month = Month
            self.Weekdays = Weekdays
            self. Monthdays = Monthdays
            self.Totaldays = Totaldays
        @property
        def Output(self):
            return self.Weekdays[self.Day] +  " " + self.Months[self.Month] + " " + str(self.Days+1) + " " + " total days:" +str(self.Totaldays)
        def AddDay(self, Days):
            #this code is used for missions that are meant to occur over many days without returning to the main mission select screen.
            self.Day += 1
            self.Totaldays +=1
            self.Days += 1
            self.TimeOfDay = 0
            if self.Day > 6:
                self.Day = 0
            if self.Days > self.Monthdays[self.Month]:
                self.Month += 1
                self.Days = 0
            if self.Month > 11:
                self.Month = 0
                
default calendar = Calendar(0,0,["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"],0,["Monday","Tuesday","Wednsday","Thursday","Friday","Saturday","Sunday"], [31,28,31,30,31,30,31,31,30,31,30,31],0,)    
