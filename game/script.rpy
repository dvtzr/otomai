# The script of the game goes in this file.

# Change text direction to rtl:
init python:
    renpy.config.rtl = True

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("אאוי", color="#5e9cff")
define p = Character("אתם", color= "#ffffff")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg_train_station

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show spr_aoi_normal
    with dissolve
    play music bgm_normal

    # These display lines of dialogue.

    e "וואה וואה מה זה פה"

    e "מה קורה פה"

    e "איך אני אוהבת {color=#f00}פפסי{/color}"

    p "מה זה פפסי בכלל?"

    p "טוב פה תהיה החלטה משמעותית"

    menu:
        "אני גם אוהב פפסי":
            jump yes
        
        "אני לא אוהב פפסי":
            jump no

    label yes:
        stop music fadeout 1.0
        hide spr_aoi_normal
        show spr_aoi_happy

        e "יאייייי איזה יופי"
        
        hide spr_aoi_happy
        hide bg_train_station
        "סיום טוב"

        return

    label no:
        stop music fadeout 1.0
        hide spr_aoi_normal
        show spr_aoi_angry

        e "בונא יא מניאק"

        hide spr_aoi_angry
        hide bg_train_station
        "סיום רע"

        return

    # This ends the game.

    return
