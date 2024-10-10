import renpy #type: ignore
from renpy import Animation, Solid #type: ignore
"""renpy
init python:
"""

def Ani_Gif(directory, **kwargs):
    from uuid import uuid4 
    pause = float(kwargs["pause"])
    gif_parts = []
    for path in renpy.list_files():
        if path.startswith(directory):
            if path[path.rindex(".")+1:].lower() == "png":
                gif_parts.append(path)
                gif_parts.append(pause)       
    gif_id = str(uuid4())
    renpy.image(gif_id,Animation(*gif_parts))
    return gif_id


