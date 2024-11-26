# phase_girls_project
 visual novel involoving talents from the phase connect company

 # basic vision  
 normal visual novels have several pitfalls that this project aims to address. 
 this project aims to be modular, and easily expandable. allowing a single contributor to make stories and full routes mostly independent from other contributors with relatively few headaches. hopefully this means that this will allow a large number of contributors to make content for the game without needing direction and coordination from a central dev team. 

# framework
the main point of this framework is to allow a single contributor to make a single story (known internally as a "mission"), then be able to drag and drop the files into the missions directory and the game will handle everything else from there.
the game runs on an internal story director which shuffles and sorts all the currently asctive story missions. from there it decides which missions to present to the player each ingame "day" and from there the player decides which mission they want to play. 

From there the each mission plays out like a regular visual novel. and within these missions contributors and use the frameworks premade functions for activating and deactivating other missions, aswell as various other game logic to create routes and story archs like any other visual novel. 

at the end of each ingame "day" the calender ticks over to the next day and all availible missions are resuffled and sorted by the internal story director. as this project is currently only in alpha 1 this story director is very primative (and currently hardcoded to push all contributor made missions infront of the tutorial)

# gameplay loop
the gameplay loop goes as follows:  
morning  
midday  
night  

the morning and night are currently placeholder and more gameplay functions will be added to them later. 

the midday is where the missions are sorted and displayed for the player to pick from.

the night is a copy of the morning and is currently placeholder. 

then the day ticks over and the proccess repeats

# required tools to contribute to the project
you will need:
git/github/github desktop
the renpy launcher
a text editor (we recommend visual studio code)
and discord




