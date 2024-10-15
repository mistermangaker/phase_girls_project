init python:
    def saveactornames(missionobject,actorlist):
        #missionobject.actors = [ ]
        newactorlist = []
        actorlist.strip()
        templist = actorlist.split(",")
        for i in templist:
            for b in system_actorslist:
                if i == b.actorname:
                    newactorlist.append(b)
        missionobject.actors= newactorlist
    def saveactorstring(inputmission,inputvalue):
        s=inputvalue
        inputmission.actors=s
        return
    def savemetadata(inputmission,author_value,contributors_value,tags_value,title_value,body_value):
        inputmission.author = author_value.split(",")
        inputmission.contributors = contributors_value.split(",")
        inputmission.tags = tags_value.split(",")
        inputmission.information[0]=title_value
        inputmission.information[1]=body_value
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
        vbox:
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
            hbox:
                if i.type == "story":
                    vbox:
                        text "title"
                        text _("[i.information[0]]")
                    vbox:
                        text "body"
                        viewport:
                            mousewheel True

                            
                            xysize(200,100)
                            
                            text _("[i.information[1]]")
                    vbox:
                        text "location tag"
                        text _("[i.author]")
                    vbox:
                        text "location tag"
                        text _("[i.contributors]")
                    vbox:
                        text "location tag"
                        text _("[i.tags]")
                    
                    


                    

screen missionedits(missiontoedit):
    modal True
    if missiontoedit.type == "story":
        default actorlist = []
        for a in missiontoedit.actors:
            $ actorlist.append(a.actorname)
        default location = FieldInputValue(missiontoedit,"location")
        #default actorslist = str(actorlist)
        default actors = ",".join(actorlist)
        default actors_value = ScreenVariableInputValue("actors")
        default title = (missiontoedit.information[0])
        default title_value = ScreenVariableInputValue("title")
        default body = (missiontoedit.information[1])
        default body_value = ScreenVariableInputValue("body")
        default author = ",".join(missiontoedit.author)
        default author_value = ScreenVariableInputValue("author")
        default contributors = ",".join(missiontoedit.contributors)
        default contributors_value = ScreenVariableInputValue("contributors")
        default tags = ",".join(missiontoedit.tags)
        default tags_value = ScreenVariableInputValue("tags")

        #default actors_value = FieldInputValue(missiontoedit,"actorsstring")
        #default actors = ",".join(actorlist)
        #default actors_value = FieldInputValue(missiontoedit,"actors")
    if missiontoedit.type == "special":
        default time = FieldInputValue(missiontoedit,"activationtag")
    
    default activationdate = str(missiontoedit.activationdate)
    default activationdate_value = ScreenVariableInputValue("activationdate")
    default jumplabel = FieldInputValue(missiontoedit,"jumplabel")
    


    frame:
        vbox:
            hbox:
                spacing 10
                vbox:
                    text "jump label"
                    button:
                        action jumplabel.Toggle()
                        input:
                            value jumplabel
                    textbutton "jump to: [missiontoedit.jumplabel]":
                        action Jump(missiontoedit.jumplabel)
                
                    text "activation date"
                    button:
                        action activationdate_value.Toggle()
                        input:
                            allow "1234567890"
                            value activationdate_value
                    if missiontoedit.type == "story":
                    
                        text "location"
                        button:
                            action location.Toggle()
                            input:
                                value location
                    if missiontoedit.type == "story":
                    
                        text "actors"
                        button:
                            action actors_value.Toggle()
                            input:
                                value actors_value
                    if missiontoedit.type == "special":
                    
                        text "time"
                        button:
                            action time.Toggle()
                            input:
                                value time
                    
                    text "Is Active"
                    textbutton _("[missiontoedit.IsActive]"):
                        action ToggleField(missiontoedit,"IsActive",true_value=True,false_value =False)
            
                
                    text "completed"
                    textbutton _("[missiontoedit.completed]"):
                        action ToggleField(missiontoedit,"completed",true_value=True,false_value =False)

                if missiontoedit.type == "story":  
                    vbox:
                    
                        text"information"
                        vbox:
                            text "title"
                            button:
                                action title_value.Toggle()
                                input:
                                    value title_value
                        vbox:
                            text "body"
                            button:
                                action body_value.Toggle()
                                input:
                                    value body_value
                        text "metadata"
                        vbox:
                            text "authors"
                            button:
                                action author_value.Toggle()
                                input:
                                    value author_value
                        vbox:
                            text "contributors"
                            button:
                                action contributors_value.Toggle()
                                input:
                                    value contributors_value
                        vbox:
                            text "tags"
                            button:
                                action tags_value.Toggle()
                                input:
                                    value tags_value
            textbutton "return":
                if missiontoedit.type == "story":
                    action Function(saveactivationdate,missiontoedit,activationdate),Function(saveactorstring,missiontoedit,actors),Function(savemetadata,missiontoedit,author,contributors,tags,title,body),Hide("missionedits")
                else:
                    action Function(saveactivationdate,missiontoedit,activationdate),Hide("missionedits")



                       