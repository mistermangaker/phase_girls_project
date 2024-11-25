default tutorial_Project_art = Story_Mission.mission_from_xml("tutorial_mission1.xml","tutorial4")
default tutorial_Project_art_nightspecial = Special_Mission.mission_from_xml("tutorial_mission2.xml","special2")

label tutorial_Project_art_nightspecial:
    "night special"
    return

label tutorial_Project_art:
    play music "Music_Export/Calm/Clouds.mp3"
    scene tenma_room day
    show tenma
    "welcome. This section will be about contributing art and other visual assets for the project."
    "Specificially we will be discussing the difference between core and mission specific assets, naming conventions, and the basics of how renpy displays images with it's \"displayables\" format"
label .questions:
    if not tutorial.tenma_mainquestions_firstviewing:
        tenma "Now let's continue with the tutorial"

    menu:
        tenma "what would you like to learn about?" 
        "the basics of renpy's displayables":
            $ tutorial.tenma_mainquestions_firstviewing = False
            jump .displayables
        "making assets for the game":
            $ tutorial.tenma_mainquestions_firstviewing = False
            jump .assets
        "art style guide":
            $ tutorial.tenma_mainquestions_firstviewing = False
            jump .artstyleguide
        "content guidelines":
            $ tutorial.tenma_mainquestions_firstviewing = False
            jump .guidelines
        "that's all":
            jump .end


label .displayables:
    tenma "we will only be going over the absolute very basics of renpy's displayables in this section, the renpy launcher has its own tutorial on this section, and you can read renpy's documentation on their website for further information."

    tenma "the very basics of displayables goes as follows"

    tenma "a “displayable” is something like an image which renpy can show, hide, and move around. "

    tenma "a “displayable” is just the name for what you want to display, so you can have images, videos, layered images, or text be displayables."

    tenma "displayables use an “attribute” or “tag” based system, meaning that it uses a collection of strings to name the object it wants to display."
    
    tenma "This makes programming very easy because renpy automatically switches out the previous image with the new one if they have the same root tag."
    show example characters
    example:
        show tenma
    tenma "to go more indepth we will use the example “tenma” and “tenma happy”"

    tenma "the root tag is “tenma” which when shown is this:"
    example: 
        show tenma happy
    tenma "and the tag “happy” tells renpy to use the “happy” face instead."
    hide example
    show tutorial_image layered_image_example tenma_code at tutorial_left_codebox
    show tenma at right
    tenma "this is because the “tenma” character displayable is a “layered image”"

    tenma "the string “tenma happy” tells renpy to use the “tenma” displayable which is a layered image"
    show tutorial_image layered_image_example tenma_images at tutorial_left_codebox
    hide tutorial_image
    tenma "and the attribute “happy” which tells renpy to use the image \"tenma_emote_happy.png\""

    show example tenma_full_image 
    
    show tenma tutorial fullimage

    tenma "but we can also do it like this and say “tenma tutorial fullimage” and renpy shows a whole .png image that isn't in the layered image but still swaps out the previous \"tenma\" displayable anyway"
    
    hide example
    tenma "this allows for much more seamless programming on your end."
    show tenma neutral at center

    tenma "pretty cool huh?"

    jump .questions
    
label .assets:
    tenma "Assets in this project are divided between core assets and mission specific assets. "

    tenma "There isn't any actual objective distinction between them, just that core assets are meant to be generic and meant to be used by all contributors. "

    tenma "Core image assets are found in the “images” folder of the game directory and the code repository for core assets is in the “characters” and “displayables” folders. "

    tenma "Core assets should have a short, generic name, and follow a consistent naming scheme similar to the rest of them"
    
    tenma "Whereas mission or contributor specific displayables should be in their own folder together."

    tenma "And they can have whatever naming scheme the contributor wants."

    tenma "If you want to make core assets to the game, they should be placed along with the other core assets."

    tenma "Do note that non core assets should be made unique to avoid conflicts with other code."
    
    tenma "So add either prefixes or suffixes of either your name, the mission they appear in, or both to the names of your displayables. "

    tenma "For example: tenma, tenma happy, or tenma sad are all generic displayables. "

    tenma "Making a new displayable and naming it tenma happy would cause code conflicts. "
    
    tenma "But naming it “tenma contributornamehere missionthree superduper happy” would not cause issues as it's unique in a way that it's very unlikely that anyone else would ever randomly pick that name"

    tenma "The more unique and descriptive your naming is, the easier it will be in the long run."

    tenma "This is done to keep things easily separated and modular."

    tenma "Like with the “tutorial” missions (that you are currently playing through) they have their own separate folder with code, assets, displayables, etc in the “missions” directory folder. "

    tenma "It contains images that should only will appear in this tutorial (though there is nothing that actually prevents them from appearing elsewhere) "

    tenma "For creating generic character assets the main format you should use is renpy's “layered image” displayables."

    show tutorial_image layered_image_example at left
    show tenma:
        linear 1.0 xalign 1.0 
    tenma "We will assume that you are already familiar with the concept of them. they are just many different images stacked on top of eachother to make different combinations of poses."

    hide tutorial_image
    show tenma:
        linear 1.0 xalign 0.5

    tenma "The layered images for characters can be found in the “characters” or “displayables” folders."


    jump .questions

label .artstyleguide:
    tenma "that depends on what assets you want to make. if you are making and contributing core assets to the game, it would be preferable to make your assets match the current art style as much as possible."

    tenma "so that means using solid black, clean lineart, with mostly flat cel shaded colors, and using gradients sparingly."

    tenma "this is done primarily to make it easier to color match between various artists, and because it's the artstyle the main developer uses the most "

    menu:
        tenma "you are about to say “but what if i want to draw in my own artstyle?”"
        "you read my mind":
            tenma "heh I knew it"
            pass
        "I wasn't thinking that at all actually":
            tenma "well I'm going to tell you about it anyway "
            pass

    tenma "anyway, you aren't required to use the core assets for your missions, infact we would love to see you make your own assets for your own missions."


    show tutorial_image tenma yourownstyle at left
    show tenma at right
    
    tenma "even making duplicate assets to the main core assets, like this"
    tenma "its perfectly acceptable to make whatever you want in your own style for your own missions"
label .morequestions:
    play music "Music_Export/Calm/Clouds.mp3" if_changed
    show tenma at right
    menu:
        tenma "any more questions?"
        "what are the best practices for making our own assets?":
            $ tutorial.tenma_questions_firstviewing = False
            jump .bestpractices
        "does this mean we can make nsfw art?":
            $ tutorial.tenma_questions_firstviewing = False
            jump .nsfwart
        "that's all":
            $ tutorial.tenma_questions_firstviewing = False
            jump .endofassets
        "why is the tenma on the left more attractive?" if tutorial.tenma_questions_firstviewing:
            $ tutorial.tenma_questions_firstviewing = False
            jump .moreattractive


label .movetenma_tocenter:
    hide tutorial_image tenma yourownstyle
    show tenma at center
    return

label .bestpractices:
    call .movetenma_tocenter
    tenma "for making your own assets, we would recommend the “layeredimage” format, it gives you the most versatility for making many standard poses"

    tenma "and for unique poses we recommend making dedicated images for them rather than trying to fit them into a layered image which is a headache to try and do."

    tenma "you can also have multiple layered images for different poses with the same root tag."

    jump .morequestions



label .nsfwart:
    call .movetenma_tocenter
    tenma "yes you can contribute nsfw art"

    tenma "just make sure that whatever mission it's in is tagged with the “nsfw” tag in your mission metadata "

    tenma "if nsfw content appears anywhere in your mission it has to be tagged nsfw. no exceptions."

   
    tenma "if you want more information see the “content guidelines” section "
    jump .morequestions


label .endofassets:
    call .movetenma_tocenter
    tenma "so that's all there is about making and contributing assets to the game"

    tenma "it's decently complex but overall not too complicated"

    tenma "thank you for listening to me"
    tenma "I will send you back to the prvious menu now"

    jump .questions


label .moreattractive:
    show tenma annoyed agitated surprised tochest
    play sound "Effects/YT_Impacts/Crash_Metal_Plate_Big_Room.mp3" volume 1
    play music "Music_Export/Dramatic/It_s_Coming.mp3"
    tenma "what's that supposed to mean exactly?"
    show tenma angry
    tenma "got a problem with small chests huh?!"

    hide tenma
    hide tutorial_image tenma yourownstyle
    show tenmaupclose crossed annoyed with vpunch
    play sound "<from 0.15>Effects/YT_Impacts/Rock_Hits_Metal_Debris.mp3" volume 0.7
    tenma "I bet you think youre sooo funny with the \"ha! tenma is flat\" don't you?"
    menu:
        "a bit":
            play sound "Effects/YT_Doors/Wood_Door_Creak_Open.mp3" volume 1
            show tenmaupclose crossed distraught6:
                parallel:
                    linear 2 zoom 1.2
                parallel:
                    easein 2.0 yalign 0.5
            tenma "oh we have a funny man over here huh?"
            show tenmaupclose crossed annoyed ears_droop1
            tenma "well I know something that's a bit funny too"
            pass
        "its hilarious":
            play sound "Effects/YT_Impacts/Crash_Metal_Plate_Big_Room.mp3" volume 1
            show tenmaupclose crossed blindrage:
                zoom 1.2
                yalign 0.5
                parallel:
                    linear 0.09 yalign 0.52
                    linear 0.13 yalign 0.5
                    repeat
                parallel:
                    linear 0.11 xalign 0.51
                    linear 0.13 xalign 0.5
                    repeat
                    
            "hilarious huh?{w=1.0} you think it's funny to make fun of me huh? {nw=6}"
            pass
    play music "Music_Export/Dramatic/Dramatic_Swarm.mp3"
    play sound "Effects/YT_Impacts/Metal_Trash_Can_Filled (1).mp3" volume 1
    show tenmaupclose annoyed lowgrab ears_angry highpoint with vpunch
    tenma "see I can be funny too"
    play sound "<to 2.2>Effects/YT_Impacts/Metal_Scrap_Kicking.mp3" volume 1
    show tenmaupclose annoyed ears_neutral highgrab  with vpunch
    tenma "now that you can't get away"

    tenma "we can talk more ..."

    show tenmaupclose scary
    tenma "...Intimately"

    show tenmaupclose ears_angry 
    tenma "now ill have you know that i think i look very cute with a modest chest"

    tenma "my modest chest, which im NOT insecure about, gives me an innocent cuteness that having massive bazonga's would ruin!"

    show tenmaupclose confused
    tenma "and all men absolutely love inocent cute girls don't they?"

    show tenmaupclose distraught6
    tenma "but you are mocking me for having a modest chest so maybe you don't agree"

    show tenmaupclose distraught6:
        zoom 1
    hide tenmaupclose

    show tenmaupclose distraught6 lowgrab ears_angry highpoint:
        zoom 1.2
        yalign 0.5
        xalign 0.5
        
    menu:
        tenma "So let me ask again. Do you think its funny that I have a flat chest?"
        "Yes":
            call .moreattractive_yes
        "N-No":
            call .moreattractive_no
        "You aren't cute either":
            call .moreattractive_hurt

    #narration:
    "perhaps it would be best if we moved along"
    jump .morequestions


label .moreattractive_yes:
    play music "<from 50>Music_Export/Dramatic/Dramatic_Swarm.mp3"
    show tenmaupclose look_rage:
        linear 0.1 yalign 0.52
        linear 0.1 xalign 0.53
        linear 0.1 yalign 0.5
        linear 0.1 xalign 0.5
        linear 0.1 yalign 0.54
        linear 0.1 xalign 0.51
        linear 0.1 xalign 0.5
        linear 0.1 yalign 0.5
    tenma "Excuse you?"
    show tenmaupclose rage lowgrab ears_angry highpoint
    tenma "you are very brave I'll give you that"
    show tenmaupclose blindrage
    tenma "But now you will regret saying that"
    show tenmaupclose distraught6
    tenma "Mark my word's you will regret this"

    #to be done later
    #$ tutorial_Project_art_nightspecial.Delayactive(3)
    hide tenmaupclose
    return


label .moreattractive_no:
    show tenmaupclose distraught6
    tenma "That's what I thought "
    show tenmaupclose scary

    tenma "Atleast you arent a complete idiot"
    tenma "Now let's get back on topic.{w=2} shall we?"
    hide tenmaupclose
    return


label .moreattractive_hurt:
    stop music fadeout 5
    show tenmaupclose look_surprised1
    tenma "Huh?! {w=1.0} -uh {nw=1}"
    show tenmaupclose look_surprised2
    tenma "You.... {w=1.0} -well.. {nw=2}"
    show tenmaupclose look_surprised3
    tenma "Well I...{w=1.0} you know{nw=2}"
    show tenmaupclose look_surprised4:
        parallel:
            linear 0.4 yalign 1.0
        easeout 0.4 zoom 1.1
    tenma "You know what.{w=1.0} Fuck you.{w=1.0} Whatever man.{w=1.0} I don't care. {w=1.0}"
    "Perhaps it would be best if we moved along{w=1.5} before anything else happens"
    hide tenmaupclose
    show tenma annoyed tochest surprised 
    jump .morequestions



label .guidelines:

    tenma "for contributing generic assets, yes there is there is, low effort, poorly made, or ugly art will not be allowed to be contributed to the generic asset"

    tenma "for your own mission specific assets, there is no restrictions, if it's what you feel is good enough quality to show others then go ahead"

    tenma "In the end its your name will be attached to it in the code and in the credits."

    tenma "there are a few exceptions to this rule, such as all the assets you contribute have to be used in your mission, unused assets have to be removed, this is to prevent bloating the game files."

    tenma "likewise, the files you commit, can't be overly large for the same reason."

    tenma "because I know that there will be at least one jackass who will attempt to commit a random 2 terabyte super high resolution picture of a train or something"

    tenma "and then will get upset when we deny their merge request on github."

    tenma "for reference, all the color character models use a texture size of 2000 by 2000 pixels, and are zoomed in so they fit on the screen"

    tenma "you should do something similar to that"

    tenma "as for nsfw content"

    jump .questions


label .end:
    "so that's all there is to tell you about working with displayables and contributing art to this project"
    "hopefully you learned a lot"
    "that's all for now"
    jump endday


    

