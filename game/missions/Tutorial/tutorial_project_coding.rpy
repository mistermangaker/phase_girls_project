
default tutorial_Project_coding = Story_Mission.mission_from_xml("tutorial_mission1.xml","tutorial6")



label tutorial_Project_coding:
    play music "Music_Export/Calm/Clouds.mp3"
    scene pippa_room day
    show pippa
    pippa "this section is less of an explanation of mechanics and code and more for core development principles"

    pippa "The main idea behind this project is to be modular, and data driven. "

    pippa "As a general rule of thumb your code should work in a decentralized fashion. and have the ability for a contributor to drag and drop in content or mods into the game directory without having to edit any files and it just works."
    pippa "as a developer for this project you will need to keep in mind that you are not developing code for making a game. you are developing a framework for others to make a game."

    pippa "so you will be required to produce clean, easily readable, well documented, and clearly labeled code complete with intended use cases and copy and pastable example code for the wiki."
    pippa "This is a rule that will be strictly enforced."

    pippa "the people who will using your code are the what we will call the “creative types”"

    pippa "otherwise known as cavemen."

    pippa "They are extremely likely to be amateur programmers and will struggle when working with unfamiliar code."

    pippa "so to make their lives (and by extension your and the main developer's lives) much easier. Thorough documentation along with step by step instructions for using the code should be standard. "

    pippa "creating templates for intended use cases will also be helpful."

    pippa "I say this because the renpy document doesn't do this, and it causes so many headaches trying to figure out what functions do and the correct syntaxes to use them."

    pippa "this means you end up spending twice as long reading documentation and experimenting with code, than you do actually programming your project."


    pippa "as for naming schemes for your code and functions. your first instinct is to be simple and succinct with your function names."

    pippa "don't do this."

    pippa "doing this can make your code ambiguous. especially to someone who isn't a coder, or someone with bad memory."

    pippa "Make your function names descriptive. "

    pippa "It's not 1999 anymore, we have auto complete, we can have longer function names."

    pippa "It saves more time and frustration to be able to read the function name and know what it does, than having to constantly go to the wiki to double check."


    return

