init python:
    
    def get_sounds(directory):
        sounds_list = []
        for path in renpy.list_files():
            if path.startswith(directory):
                if path[path.rindex(".")+1:].lower() == "mp3" or path[path.rindex(".")+1:].lower() == "wav" or path[path.rindex(".")+1:].lower() == "ogg":
                    sounds_list.append(str(path))
        return sounds_list
    
    renpy.music.register_channel("sound1", mixer="sound", loop=False, stop_on_mute=True, tight=True, file_prefix='', file_suffix='', buffer_queue=True) 
    renpy.music.register_channel("sound2", mixer="sound", loop=False, stop_on_mute=True, tight=True, file_prefix='', file_suffix='', buffer_queue=True) 

    def start_mission_select_screen_audio():
        renpy.music.set_pause(False, channel='sound1')
        renpy.music.set_pause(False, channel='sound2')
    def stop_mission_select_screen_audio():
        renpy.music.stop(channel='sound1', fadeout=None)
        renpy.music.stop(channel='sound2', fadeout=None)
        renpy.music.set_pause(True, channel='sound1')
        renpy.music.set_pause(True, channel='sound2')
        
        return
    def mission_select_screen_ambience_ambience():
        print ("starting new ambience sound")
        sound_list1 = get_sounds("audio/mission_select_screen/Ambience/")
        chance2 = renpy.random.randint(1,10)
        sound_file1 = renpy.random.choice(sound_list1)
        print (sound_list1)
        if chance2>=7:
            renpy.music.queue(sound_file1,'sound1',relative_volume=1,fadein =0.5)
        else:
            renpy.music.queue(["<silence 30>",sound_file1],'sound1',relative_volume=1,fadein =0.5)
        print (renpy.music.get_playing(channel='sound1'))
        if renpy.music.get_pause('sound1'):
            print (renpy.music.get_pause('sound1'))
            renpy.music.set_queue_empty_callback(mission_select_screen_ambience_ambience)
        else:
            renpy.music.stop(channel='sound1', fadeout=None)

    def mission_select_screen_ambience_wind():
        print ("starting new wind sound")
        sound_list = get_sounds("audio/mission_select_screen/Wind/")
        chance = renpy.random.randint(1,10)
        sound_file = renpy.random.choice(sound_list)
        print (sound_file)
        if chance>=3:
            renpy.music.queue(sound_file,'sound2',relative_volume=1,fadein =0.5)
        else:
            renpy.music.queue(["<silence 15>",sound_file],'sound2',relative_volume=1,fadein =0.5)
        print (renpy.music.get_playing(channel='sound2'))
        if renpy.music.get_pause('sound2'):
            print (renpy.music.get_pause('sound2'))
            renpy.music.set_queue_empty_callback(mission_select_screen_ambience_wind)
        else:
            renpy.music.set_pause(True, channel='sound2')


