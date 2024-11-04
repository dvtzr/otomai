# The script of the game goes in this file.

# Change text direction to rtl:
init python:
    renpy.config.rtl = True

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define ao = Character("אאוי", color="#5e9cff")
define sh = Character("שירו", color="#ffffff")
define ak = Character("אקאי", color="#ff0000")
define p = Character("אתם", color= "#80ff75")
default ending_progress = 0
default secret_ending = False
default persistent.aoi_ending = False
default persistent.shiro_ending = False
default persistent.akai_ending = False
# The game starts here.


label start:
    
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg_train_station

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show spr_aoi_test
    with dissolve
    play music bgm_normal

    # These display lines of dialogue.

    ao "וואה וואה מה זה פה"

    ao "מה קורה פה"

    ao "איך אני אוהבת {color=#f00}לבדוק אם סופים עובדים{/color}"

    p "מה באמת?"

    p "ואם אני רוצה לבחור עם מי אני רוצה להיות?"

    menu:
        "אאוי":
            jump aoi_route
        
        "שירו":
            jump shiro_route

        "אקאי":
            jump akai_route

        "אופציה רביעית סודית" if persistent.aoi_ending and persistent.shiro_ending and persistent.akai_ending:
            jump secret_route


    label aoi_route:
        stop music fadeout 1.0
        hide spr_aoi_test
        show spr_aoi_happy

        ao "שלום זאת אני אאוי"
        ao "וזה הראוט המרגש שלי"
        ao "בוא נעשה בחירות"
        p "מה כמו כל ארבע ארבע שנים?"
        
        hide spr_aoi_happy
        show spr_aoi_angry

        ao "לא יא טמבל"
        ao "טוב בוא נראה"
        ao "תבחר"

        menu:
            "בחירה טובה 1":
                $ ending_progress += 1
                ao "נכון"
                
            "בחירה רעה 1":
                ao "לא נכון"
        
        ao "ועוד פעם"

        menu:
            "בחירה טובה 2":
                $ ending_progress += 1
                ao "נכון"
                
            "בחירה רעה 2":
                ao "לא נכון"

        ao "ואחרון חביב לט מי שואו יו תל אביב"

        menu:
            "בחירה טובה 3":
                $ ending_progress += 1
                ao "נכון"
                
            "בחירה רעה 3":
                ao "לא נכון"      

        if ending_progress >= 2:
            hide bg_train_station
            "סיום טוב"
            $ persistent.aoi_ending = True
            return
        else:
            hide bg_train_station
            "סיום רע"
            return 

    label shiro_route:
        stop music fadeout 1.0
        hide spr_aoi_test
        show spr_aoi_happy

        sh "שלום זה אני שירו"
        sh "וזה הראוט המרגש שלי"
        sh "בוא נעשה בחירות"
        p "אבל למה אתה נראה כמו אאוי בדיוק"
        
        hide spr_aoi_happy
        show spr_aoi_angry

        sh "שתוק שתוק עדיין הספרייטים לא מוכנים"
        sh "טוב בוא נראה"
        sh "תבחר"

        menu:
            "בחירה טובה 1":
                $ ending_progress += 1
                sh "נכון"
                
            "בחירה רעה 1":
                sh "לא נכון"
        
        sh "ועוד פעם"

        menu:
            "בחירה טובה 2":
                $ ending_progress += 1
                sh "נכון"
                
            "בחירה רעה 2":
                sh "לא נכון"

        sh "ואחרון חביב לט מי שואו יו תל אביב"

        menu:
            "בחירה טובה 3":
                $ ending_progress += 1
                sh "נכון"
                
            "בחירה רעה 3":
                sh "לא נכון"      


        if ending_progress >= 2:
            hide bg_train_station
            "סיום טוב"
            $ persistent.shiro_ending = True
            return
        else:
            hide bg_train_station
            "סיום רע"
            return 

    label akai_route:
        stop music fadeout 1.0
        hide spr_aoi_test
        show spr_aoi_happy

        ak "שלום זה אני אקאי"
        ak "וזה הראוט המרגש שלי"
        ak "בוא נעשה בחירות"
        p "אבל למה אתה נראה כמו אאוי בדיוק"
        
        hide spr_aoi_happy
        show spr_aoi_angry

        ak "שתוק שתוק עדיין הספרייטים לא מוכנים"
        ak "טוב בוא נראה"
        ak "תבחר"

        menu:
            "בחירה טובה 1":
                $ ending_progress += 1
                ak "נכון"
                
            "בחירה רעה 1":
                ak "לא נכון"
        
        ak "ועוד פעם"

        menu:
            "בחירה טובה 2":
                $ ending_progress += 1
                ak "נכון"
                
            "בחירה רעה 2":
                ak "לא נכון"

        ak "ואחרון חביב לט מי שואו יו תל אביב"

        menu:
            "בחירה טובה 3":
                $ ending_progress += 1
                ak "נכון"
                
            "בחירה רעה 3":
                ak "לא נכון"      


        if ending_progress >= 2:
            hide bg_train_station
            "סיום טוב"
            $ persistent.akai_ending = True
            return
        else:
            hide bg_train_station
            "סיום רע"
            return 


    label secret_route:
        hide spr_aoi_test
        show spr_aoi_happy

        ao "יאיייייי"

        stop music fadeout 1.0
        hide spr_aoi_happy
        hide bg_train_station

        "סיום סודי"
       
        return


    # This ends the game.

    return
