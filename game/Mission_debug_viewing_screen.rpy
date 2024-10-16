init python:
    def saveactornames(missionobject,actorlist):
        missionobject.actors = [ ]
        newactorlist = []
        actorlist.strip()
        templist = actorlist.split(",")
        for i in templist:
            for b in system_actorslist:
                if i == b.actorname:
                    newactorlist.append(b)
        missionobject.actors = newactorlist
    def saveactivationdate(inputmission,inputvalue):
        s=int(inputvalue)
        inputmission.activationdate=s
        return
    
style mission_label is gui_label
style mission_label_text is gui_label_text
style mission_text is gui_text
style mission_textbutton_text is button 
style mission_textbutton_text:
    size 15
style mission_label_text:
    size 33
style mission_text:
    size 25


screen quick_launch():
    tag menu
    predict False
    use game_menu(_("quick_launch"), scroll="viewport"):
        style_prefix "mission"
        default search = persistent.quicklaunchsearchvariable
        vbox:
            text "this screen is used for quickly going to mission labels to make it easy to test missions"
            use searchbox(search)
            spacing 10
            if search:
                for i in alltype_missions_list_repository:
                    if search in i.jumplabel:
                        hbox:
                            vbox: 
                                text "Jump Label: [i.jumplabel]"
                                text "type: [i.type]"
                                textbutton "play":
                                    action Start(i.jumplabel)
            else:
                for i in alltype_missions_list_repository:
                    hbox:
                        vbox: 
                            text "Jump Label: [i.jumplabel]"
                            text "type: [i.type]"
                            textbutton "play":
                                action Start(i.jumplabel)


screen DevMissionList():
    tag menu
    predict False
    use game_menu(_("DevMissionList"), scroll="viewport"):
        style_prefix "mission"
        default search = persistent.quicklaunchsearchvariable
        text "this screen is used specifically for ingame debugging and setting mission variables for checks"
        use searchbox(search)

        vbox:
            spacing 10     
            if search:
                for i in alltype_missions_list_repository:
                    if search in i.jumplabel:
                        use DevMissionBoxes(i)
            else:
                for i in alltype_missions_list_repository:
                    use DevMissionBoxes(i)

default persistent.quicklaunchsearchvariable = ""                    
screen searchbox(search):
    style_prefix "mission"
    default search = persistent.quicklaunchsearchvariable
    default search_value = ScreenVariableInputValue("search")
    frame:
        xsize 500
        vbox:
            hbox:
                spacing 10
                text "search"
                textbutton "save":
                    style_prefix "check"
                    action ToggleVariable("persistent.quicklaunchsearchvariable", search, "")
            button:
                action search_value.Toggle()
                input:
                    value search_value            
                    

screen  DevMissionBoxes(i):
    frame:
        hbox:
            spacing 10
            textbutton "edit":
                action ShowTransient("missionedits",missiontoedit = i)
            vbox:
                text "type"
                text "[i.type]"
            vbox: 
                text "Jump Label"
                text "[i.jumplabel]"
                textbutton "play":
                    action Jump(i.jumplabel)
            if i.type == "special":
                vbox:
                    text "activation tag"
                    text _("[i.activationtag]")
                
            vbox:
                text "activation date"
                text _("[ i.activationdate]")
            
            if i.type == "story":
                vbox:
                    text "location tag"
                    text _("[i.location]")
                
            if i.type == "story":
                vbox:
                    text "actor list"
                    for a in i.actors:
                        text _("[a.actorname]")
                        
            vbox:
                text "Is Active"
                textbutton _("toggle active"):
                    action ToggleField(i,"IsActive",true_value=True,false_value =False)
                
            vbox:
                text "completed"
                textbutton _("toggle completed"):
                    action ToggleField(i,"completed",true_value=True,false_value =False)

                    

screen missionedits(missiontoedit):
    modal True
    if missiontoedit.type == "story":
        default actorlist = []
        for a in missiontoedit.actors:
            $ actorlist.append(a.actorname)
        default location = FieldInputValue(missiontoedit,"location")
        default actors = ",".join(actorlist)
        default actors_value = ScreenVariableInputValue("actors")
    if missiontoedit.type == "special":
        default time = FieldInputValue(missiontoedit,"activationtag")
    
    default activationdate = str(missiontoedit.activationdate)
    default activationdate_value = ScreenVariableInputValue("activationdate")
    default jumplabel = FieldInputValue(missiontoedit,"jumplabel")
    


    frame:
        vbox:
            spacing 10
            vbox:
                text "jump label"
                button:
                    action jumplabel.Toggle()
                    input:
                        value jumplabel
                textbutton "jump to: [missiontoedit.jumplabel]":
                    action Jump(missiontoedit.jumplabel)
            vbox:
                text "activation date"
                button:
                    action activationdate_value.Toggle()
                    input:
                        allow "1234567890"
                        value activationdate_value
            if missionedit.type == "story":
                vbox:
                    text "location"
                    button:
                        action location.Toggle()
                        input:
                            value location
            if missionedit.type == "story":
                vbox:
                    text "actors"
                    button:
                        action actors_value.Toggle()
                        input:
                            value actors_value
            if missionedit.type == "story":
                vbox:
                    text "time"
                    button:
                        action time.Toggle()
                        input:
                            value time
            vbox:
                text "Is Active"
                textbutton _("[missiontoedit.IsActive]"):
                    action ToggleField(missiontoedit,"IsActive",true_value=True,false_value =False)
            vbox:
                text "completed"
                textbutton _("[missiontoedit.completed]"):
                    action ToggleField(missiontoedit,"completed",true_value=True,false_value =False)
            textbutton "return":
                if missionedit.type == "story":
                    action Function(saveactivationdate,missiontoedit,activationdate),Function(saveactornames,missiontoedit,actors),Hide("missionedits")
                else:
                    action Function(saveactivationdate,missiontoedit,activationdate),Hide("missionedits")





                       