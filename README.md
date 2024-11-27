# The Phase Connect Streamerhouse
 this is a visual novel involving talents from the phase connect company

# frequently asked questions
Q: What is the goal of this project?  
A: It's a community driven fangame, the goal is to show off our passion for our favorite streamers  

Q: What genre will the game be?  
A: It is planned to be an episodic, slice of life, comedy. see the "project information" section, under "Overview" for more information

Q: What endings are planned?
A: There are no current endings planned, simply by the nature of the games architecture. see the "project information" section, under "Overview" for more information

Q: Will this game cost money?  
A: Never. It's a game made by the community so it is, and always will be, free and open source for anyone to play, download, edit, or redistribute the liscense can he found [here](https://creativecommons.org/licenses/by-nc-sa/4.0/)  

Q: Will a patreon or other means of raising money be implimented?  
A: As of release alpha 1 there is no current plans for a patreon. though if, in the future, funds are required to continue development of this game. Then this may change.  

Q: What if I want to contribute?  
A: Perfect we would love the help. check the "contributing" section further down for more information on that  

Q: What platforms will this game be available on when its done?  
A: ¯\_(ツ)_/¯   

Q: Where can I download it currently?  
A: In the [releases branch](https://github.com/mistermangaker/phase_girls_project/releases)  

Q: Will the game have "xyz" in the story?  
A: Add it yourself. we'd love to see what you can do  

Q: In that case can I add "abc"?  
A: Maybe check the "contributing" section further down  

Q: I'm a streamer, is this safe to play on stream?  
A: The project allows NSFW content to be contributed. In the future, more extensive content filtering and protections will be put into place to make it safe to place on stream. 

Q: Will AI generated content be used in this game?  
A: No. Human made assets only. check the "contributing" section for more information  




# Poject Information
## Overview  
This project is built with the goal of being a large disjointed colection of short stories, funny moments, and various fanfiction from the community in a visual novel format. this format of writting clashes with the more interconnected nature of most visual novels which have long branching paths (known as routes) where all later routes depend on previous work. in a community driven project such as this, that would cause significant issues, as the development can easily be stalled if just one or two people work too slowly compared to the rest of the team. hence why the framework that this game uses was developed.  

This framework allows for easy insertion of whatever content a contributor wants, at any point in the game. then the game will handle presenting the content to the player. The premise that the entire game is set in a single building is primarily to save on the time costs of making vast quanties of backgrounds, sound effects, and assets for the game, allowing us to reuse these assets over and over again without breaking immersion for the player.

It is also for this reason that the primary genre of the game is comedy and slice of life, as that is what best fits how the framework functions. Though it doesn't make it impossible for contributors to adapt this framework to other genres, the planned future mechanic of "chapters" will also make this much easier to achieve since it will allow for contributors to easily segment their work into its own space. 

This project aims to be modular, and easily expandable. allowing a single contributor to make stories and full routes mostly independent from other contributors with relatively few headaches. Hopefully this means that this will allow a large number of contributors to make content for the game without needing direction and coordination from a central dev team.   

## framework
the main point of this framework is to allow a single contributor to make a single story (known internally as a "mission"), then be able to drag and drop the files into the missions directory and the game will handle everything else from there.
the game runs on an internal story director which shuffles and sorts all the currently asctive story missions. from there it decides which missions to present to the player each ingame "day" and from there the player decides which mission they want to play. 

From there the each mission plays out like a regular visual novel. and within these missions contributors and use the frameworks premade functions for activating and deactivating other missions, aswell as various other game logic to create routes and story archs like any other visual novel. 

at the end of each ingame "day" the calender ticks over to the next day and all availible missions are resuffled and sorted by the internal story director. as this project is currently only in alpha 1 this story director is very primative (and currently hardcoded to push all contributor made missions infront of the tutorial)


# Contributing 
---
If you want to contribute to this project you will need all of the required tools (see below). Aswell as follow the contributing guidelines (see further below) for your work to be accepted.

# required tools to contribute to the project
you will need:
[git/github/github desktop](https://desktop.github.com/download/)  
[renpy launcher](https://www.renpy.org/)  
[visual studio code](https://code.visualstudio.com/)  
[discord](https://discord.gg/DkgZnU3GXV)


# contributing guidelines
### Disclaimer:  
These guidelines may change in future. contributions made before the changes may or may not required to change. they will be considered on a case by case basis
### Presumption of good faith contribution
To preface the following rules. we will assume that any content added to this project was done in purely good faith by the contributor and that any violations of these rules (unless we are led to believe otherwise) were entirely non malicious in nature. We will simply ask that the offending content be changed or removed. As such no punishment will be administered based on accidental missteps of these rules (this doesnt mean they won't be enforced tho).

### All assets contributed should either be made by, have the permission of, or be otherwise be allowed by, the original creator
all contributions have to have either been made by the original creator, or be allowed to be contribruted by them, either through direct permission, or by liscense. 

### Contibutions should generally be of a good quality
assets, stories, art, or code may be rejected or modified if its of especially or intentionally poor quality. an example would be contributions with large quanties of mispelled dialogue nonsensical stories, or being overly large, or containing massive amounts of unused files that bloat the game unnecessarily 

### Human made content only
no ai generated assets of any kind. 

### No political content
That being all content so strictly be apolitical in nature. The audience came here to enjoy their favorite streamers and not get lectured by the author. 

### No Twitter or internet drama
Same reason as above. There are other places more appropriate for that.

### Any Talent shown in this game gets veto power over their depiction in this game
Should any of the talents or phase connect management voice issues with any content in this game. It will be changed to a state which they find more acceptable or removed from the game if they so choose. 
(should this happen we ask the talent and the audience at large to assume good faith on behalf of the original contributor and not attempt to seek revenge or otherwise punish them) 

### No disparaging content of the phase connect talents.
This one will require more explanation. In short, banter, memes, or shitposts of the phase connect talents are permitted without moderation or censorship. bad faith interpretations of the talents character, personality, or references to past lives or careers are not. 

### As for other vtubers or streamers:
This game is primarily aimed as a phase connect fan game. Thus should primarily focus on the phase connect talents. streamers and other vtubers that have collaborated with phase connect talents in the past are allowed to be included and make cameos in this story with the same rules as above. 

### All NSFW, suggestive, or ecchi content needs proper disclosure censorship
This project allows for nsfw and suggestive content. however if a player wants to avoid such things, or a streamer wants to play the game on stream, then they should be able to be absolutely certain that there won't be any surprises. it is for this reason that ANY addition of nsfw or ecchi content in any contibution must include a NSFW tag in their contents metadata. likewise the nsfw content follows the same rules as above, depicted talents or streamers get veto power on this 

