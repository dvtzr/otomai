# The script of the game goes in this file.

# Change text direction to rtl:
init python:
    renpy.config.rtl = True

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define ao = Character("אאוי", color="#5e9cff", image = "aoi")
define sh = Character("שירו", color="#ffffff", image = "shiro")
define ak = Character("אקאי", color="#ff0000", image = "akai")
define p = Character("אתם", color= "#80ff75")
default ending_progress = 0
default secret_ending = False
default persistent.aoi_ending = False
default persistent.shiro_ending = False
default persistent.akai_ending = False

# tranforms: 
transform left_to_right:
    yalign 1.0
    easein_bounce 3 xalign 1.0
    pause 0.5
    ease 3 xalign .1
    pause 0.5
    repeat

# The game starts here.
label start:

    ## Disclaimers

    "היי, כאן צוות הווי ובידור אמא''י!"

    "תודה רבה לכם שהחלטתם לשחקן במשחק שלנו ואנחנו מקווים שתהנו ממנו כמו שאנחנו נהננו להכין אותו."

    "לתשומת ליבכם והבנתכם: דמות השחקן במשחק מיוצגת כדמות בן על מנת להקל על יצירת המשחק."
    
    jump intro_scene

    ## Introduction
    label intro_scene:
        
        # show train brackground
        scene bg_train_station

        "בוקר טוב שחקן!"

        "ואיזה בוקר זה באמת, בוקר הכנס! הכנס הראשון שלך!"

        # get player name input (irrelevant)
        python:
            renpy.input("מי אתה שחקן יקר ומה השם שלך?",length = 32)
        
        "תודה רבה! לא נשתמש בזה, אבל טוב לדעת שאתה מוכן לשיתוף פעולה!"

        "ההתרגשות באוויר והפרפרים בבטן כבר משתוללים. "

        "הדרך המהירה ביותר לכנס היא הרכבת, זה למה אתה כאן. בתחנת הרכבת." 

        p "סוף סוף הגיע הזמן שלי ללכת לאירוע הכי מדהים, כנס האנימה!"

        p "הרכבת שלי פה עוד 5 דקות, כל מה שאני צריך לעשות זה לשבת בשקט, לשמוע מוזיקה, ולרדת מהרכבת."

        # (note : train sound here)
        play sound sfx_train_arrive volume 0.25

        p "מקווה שיהיה לי מקום ישיבה, מרגיש שכל עם ישראל כאן..!"

        "הרכבת נכנסת לתחנה ונראה שצדקת, בקושי יש מקום."

        "הצלחת למצוא את דרכך לקרון ריק יחסית לשאר הרכבת."

        # (note : train sound here)
        play sound sfx_train_door_open volume 0.5
        play music bgm_normal

        scene bg_inside_train

        "התיישבת והתחלת להתמקם, סך הכל מקום די סבבה."

        "לפתע עולים לקרון בו אתה נמצא שלושה אנשים עם שיער בצבע מוזר."

        "וואי! כנראה שהם גם באים לכנס! יש להם חזות של אוהבי אנימה, אולי זה השיער בצבעים?"
        



        show aoi at left_to_right
        with dissolve
        

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

    ## Aoi Route
    label aoi_route:
        stop music fadeout 1.0

        ao happy "שלום זאת אני אאוי"
        ao "וזה הראוט המרגש שלי"
        ao "בוא נעשה בחירות"
        p "מה כמו כל ארבע ארבע שנים?"
        

        ao angry "לא יא טמבל"
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

    ## Shiro Route
    label shiro_route:
        stop music fadeout 1.0
        hide aoi test
        show aoi happy

        sh "שלום זה אני שירו"
        sh "וזה הראוט המרגש שלי"
        sh "בוא נעשה בחירות"
        p "אבל למה אתה נראה כמו אאוי בדיוק"
        
        hide aoi happy
        show aoi angry

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

    ## Akai Route
    label akai_route:
        stop music fadeout 1.0
        hide aoi test
        show aoi happy

        ak "שלום זה אני אקאי"
        ak "וזה הראוט המרגש שלי"
        ak "בוא נעשה בחירות"
        p "אבל למה אתה נראה כמו אאוי בדיוק"
        
        hide aoi happy
        show aoi angry

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
        hide aoi test
        show aoi happy

        ao "יאיייייי"

        stop music fadeout 1.0
        hide aoi happy
        hide bg_train_station

        "סיום סודי"
       
        return


    # This ends the game.

    return
