# The script of the game goes in this file.

# Change text direction to rtl:
init python:
    renpy.config.rtl = True

# Declare characters used by this game. The color argument colorizes the
# name of the character.

##  Characters

#   main characters
define ao = Character("אאוי", color="#5e9cff", image = "aoi")
define sh = Character("שירו", color="#ffffff", image = "shiro")
define ak = Character("אקאי", color="#ff0000", image = "akai")
define e = Character("כולם", color= "#ffd000")
define p = Character("אתם", color= "#80ff75")

#   secondary characters / npcs 
define m = Character("מתנדב", color= "#00704f")
define st = Character("אדם זר", color= "#00704f")
define am = Character("עמית נדבת", color= "#00704f")
define shp = Character("מוכר", color= "#00704f")
define mtt = Character("המנחה", color= "#00704f")
define jdg = Character("שופטת", color= "#00704f")
define emi = Character("אמה ועידו", color= "#00704f")

##   Variables
# Progress on endings
default ending_progress = 0

default secret_ending = False
# endings gotten

#   good 
default persistent.aoi_ending = False
default persistent.shiro_ending = False
default persistent.akai_ending = False
#   bad
default persistent.aoi_ending_bad = False
default persistent.shiro_ending_bad = False
default persistent.akai_ending_bad = False

## styles:

style excited is text:
    size 20


## special images:


## tranforms: 

# bounce left to right
transform left_to_right:
    yalign 1.0
    easein_bounce 3 xalign 1.0
    pause 0.5
    ease 3 xalign .1
    pause 0.5
    repeat

## darken image

transform sprite_darken:
    matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)
    linear 1.0 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(-0.7)

## lighten image

transform sprite_lighten:
    matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(-0.7)
    linear 1.0 matrixcolor TintMatrix("#ffffff") * BrightnessMatrix(0.0)

## sprite expressions:
# aoi
# shiro
# akai 

# The game starts here.
label start:

    ## Disclaimers

    "היי, כאן צוות הווי ובידור אמא''י!"

    "תודה רבה לכם שהחלטתם לשחקן במשחק שלנו ואנחנו מקווים שתהנו ממנו כמו שאנחנו נהננו להכין אותו."

    "לתשומת ליבכם והבנתכם: דמות השחקן במשחק מיוצגת כדמות בן על מנת להקל על יצירת המשחק."
    
    jump intro_scene

    ## Scene 1: Introduction

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

        p "הרכבת שלי מגיעה עוד 5 דקות. כל מה שאני צריך לעשות זה לשבת בשקט, לשמוע מוזיקה, ואז לרדת בתחנה."

        # change the train bg to the train arriving
        scene bg_train_arrive
        with dissolve

        # (note : train sound here)
        play sound sfx_train_arrive volume 0.25

        p "מקווה שיהיה לי מקום ישיבה, מרגיש שכל עם ישראל כאן..!"

        "הרכבת נכנסת לתחנה ונראה שצדקת, בקושי יש מקום."

        # change the train bg to the train arriving
        scene bg_inside_train_2
        with dissolve

        "הצלחת למצוא את דרכך לקרון ריק יחסית לשאר הרכבת."

        # (note : train sound here)
        play sound sfx_train_door_open volume 0.5
        play music bgm_normal

        scene bg_inside_train
        with dissolve

        "התיישבת והתחלת להתמקם, סה\"כ מקום די סבבה"

        "לפתע עולים לקרון בו אתה נמצא שלושה אנשים עם שיער בצבע מוזר."

        "וואי! כנראה שגם הם באים לכנס! יש להם חזות של אוהבי אנימה, אולי זה בגלל השיער הצבעוני?"

        show aoi
        show shiro at left
        show akai at right
        with dissolve
        
        "רגע, אתה מזהה אותם בתור המאסקוטים הראשיים של אמא\"י."

        ao happy "היי, תגיד, אתה במקרה מגיע לכנס האנימה בירושלים?"

        menu :
            "כן, איך ידעת?":
                pass
            "לא, למה חשבת?":
                pass  
        
        ao "לא בטוחה, יש לך חזות של אוהב אנימה."

        sh stress "אאוי, לא יפה להגיד חזות!"

        ao "בכל מקרה! אכפת לך אם נשב פה?"

        "היא מתיישבת למרות ששאלה ולא קיבלה תשובה, שירו ואקאי אחריה."
        
        # highlight aoi

        hide aoi
        hide shiro
        hide akai
        show aoi
        show shiro at left:
            sprite_darken
        show akai at right:
            sprite_darken

        "אאוי, נערה עם שיער בצבע כחול וקוקיות ארוכות, יושבת מולך. בדרך כלל היא מלאת שמחת חיים, במיוחד לצד אחיה התאום שירו וחבריהם אקאי. אולי קרה משהו?"

        # highlight shiro
        hide aoi
        hide shiro
        show aoi at center:
            sprite_darken
        show shiro at left:
            sprite_lighten

        "שירו, אחיה התאום של אאוי. אני לא יודע מה הגיע קודם, השיער הלבן או הדאגה שלו מהשטויות של אחותו וחברו. בכל מקרה, הוא נראה די עסוק במחשבות."

        # highlight akai
        hide shiro
        hide akai
        show shiro at left:
            sprite_darken
        show akai at right:
            sprite_lighten
        
        "אקאי, הצעיר מבין השלושה (אני יודע, מפתיע). למרות גילו הצעיר הוא נראה כמו בחור עם ראש על הכתפיים, מעניין מה מציק לו."

        # re highlight everyone
        hide shiro
        hide aoi
        show shiro at left:
            sprite_lighten
        show aoi at center:
            sprite_lighten

        "הם נראים מאוד טרודים במשהו."

        p "הכל בסדר? מה קרה?"

        e "טוב… דווקא יש משהו שמטריד אותי."
        
        ## split to explanations
        label intro_choices :
            
            hide aoi
            hide shiro
            hide akai
            show aoi
            show shiro at left
            show akai at right

            menu:
                "מה הבעיה, אאוי?":
                    jump aoi_exp
                
                "למה אתה עצוב, שירו?":
                    jump shiro_exp

                "מה מלחיץ אותך, אקאי?":
                    jump akai_exp

                "נראה לי שהבנתי" if ending_progress >= 2:
                    jump end_exp

    ## Aoi Route - explanation
    label aoi_exp:

        ## remove shiro and akai
        hide akai
        hide shiro

        ao happy "אני משתתפת בתחרות הקוספליי בפעם הראשונה השנה, ואני רוצה שזה יהיה מושלם!"

        ao sad "אבל האמת… לקח לי כל כך הרבה זמן להכין את הקוספליי עצמו ששכחתי להכין את כל השאר."

        ao "ועכשיו אני מפחדת שאעלה לבמה ואפול על הפרצוף. וזה לא יהיה חלק מהסקיט!"
        
        ao angry "ושירו לא יכול לעזור לי עם זה! יש לו קול של ברבור, אבל לתפור? ממש לא!"
        
        ao sad "אם רק היה מי שיעזור לי... אני ממש רוצה לנצח!"
        
        p "אני יכול לעזור לך."
        
        p "אף פעם לא השתתפתי, אבל יש לך כל כך הרבה כריזמה, את תצליחי אם רק תאמיני בעצמך!"
        
        ao surprised "וואי, קצת גיבור שונאן מצידך הנאום הזה."
        
        ao happy "אאוי: אבל נשמע טוב! אני סומכת עליך. ביחד נעשה את תחרות הקוספליי הזו בלתי נשכחת!"
        
        p "דרך אגב, לאיזו דמות עשית קוספליי?"
        
        ao surprised "מה? זה לא ברור? לא רואים ישר לאיזו דמות יהיה הכי מתאים לי לעשות קוספליי?"

        "לשבריר שנייה, עולה לך שם. אבל אתה מרגיש שזה לא נכון, אז אתה שותק."

        ao angry "נו באמת. זה קוספליי לנסיכה הקסומה שהיא גם בת ים, גם נינג'ה וכנראה גם בת אלמוות! הנסיכה נטלישיקו!"

        "מי?"

        menu:
            "אה. היא באמת מתאימה לך!":
                pass
                
            "לא מכיר, נשמע מגניב!":
                pass
        
        ao happy "תודה! אני מקווה שגם השופטים והקהל יאהבו את זה…"
        $ ending_progress += 1
        jump intro_choices

    ## Shiro Route
    label shiro_exp:
        hide akai
        hide aoi
        hide shiro
        show shiro at center

        sh stress "האמת… חשבתי שהכנס הזה יהיה כמו כל כנס. אאוי ואני עולים על הבמה, קורעים את התחרות ומנצחים."
        
        sh "רק שהפעם.. אאוי החליטה שהיא חייבת להשתתף בתחרות הקוספליי, אבל אני מאוד רוצה להשתתף בתחרות האיידול!"
        
        sh "אאוי ואני תמיד שרים בדואט. זה כמו מלח ופלפל.כמו תות ובננה. כמו…"
        
        p "כמו אש ופיקאצ'ו?"
        
        ## note: maybe an animation here?
        sh "?"

        sh laugh "אהה… כן, אבל לפני הפנסיה!"

        p "ניסית לשאול את אקאי? אולי הוא יכול לעזור."

        sh angry "לא אחרי אירוע הקראוקה של 2014."

        menu:
            "אוי לא, מרגיש שיש פה סיפור רקע":
                pass
                
            "מה קרה ב-2014?":
                pass

            "היה אז אירוע קראוקה?":
                pass
        
        sh mortified "אקאי שר כל כך גרוע שהוא בטעות מחק את הזיכרון של כל באי האירוע. רק מעטים מאיתנו זוכרים את היום הנוראי ההוא."

        sh "זוכרים… ולא שוכחים."

        p "אה. אבל גם אני לא יודע לשיר. איך אוכל לעזור?"

        sh stress "אם היה לי עוד זמן להתכונן, אולי הייתי מצליח לשנות את הדואט הזה לסולו מצליח."

        p "אם ככה, אוכל לעזור לך בשמחה!"

        sh surprised "באמת? וואו זה ממש נחמד מצידך!"

        sh "כשהרכבת תעצור נוכל ללכת ולהגיע בדיוק בזמן לחזרה! אני רק מקווה שלא נאחר לחזרה הזו…"

        $ ending_progress += 1
        jump intro_choices

    ## Akai Route
    label akai_exp:
        hide akai
        hide aoi
        hide shiro
        show akai at center

        ak stress "וואי, רואים עליי, אה? קשה לשמור התרגשות כזו בלב!"
        
        ak "האמת… שהכנס הזה מיוחד מאוד! אחד מסוגו!"
        
        ak @ happy "אחרי הרבה שנים… היום זו ההתנדבות שתקבע אם העתיד שלי בסגל!"
        
        p "סגל? מה זה אומר?"

        ak "שום דבר מיוחד. זה רק אומר שאני נכנס חינם…"
        
        ak excited "ואעזור להפוך את הכנס הזה לכנס הכי טוב בעולם!"
        
        ak focus "זו ההתנדבות שתקבע את גורל הכנס… עליו הוא יקום וייפול!"

        p "מה? איזה תפקיד בכנס יכול להיות כל כך חשוב? ספר לי!"

        ak "אני לא יודע אם אני יכול… האם אתה מוכן אליו?"

        menu:
            "רגע, אמיתי? זה סוד?":
                pass
                
            "ברור שאני מוכן!":
                pass

            "א-אני לא יודע!?":
                pass
    
        ak "אולי… יש לך את מה שצריך בשבילו."
        
        ak "האם תרצה להצטרף אליי למסע הביזארי הזה?"

        menu:
            "אני רוצה לדבר קודם עם אאוי":
                pass
                
            "אני רוצה לדבר קודם עם שירו":
                pass

            "יש לי פיפי":
                pass

        ak happyclosed "אוקיי, אם כן תרצה לעזור, אחכה לך בכניסה לכנס."
        $ ending_progress += 1
        jump intro_choices


    ## End explanations
    label end_exp:
        
        $ ending_progress = 0
        hide aoi
        hide shiro
        hide akai
        with dissolve

        "לאחר שהקשבת לבעיותיהם הרבות של המאסקוטים של אמא\"י, החלטתם להמשיך לדבר על דברים אחרים."

        "איזה אנימה ראית בשנה האחרונה, מצב החסה בשטחים... ולפני ששמת לב, הגעת כבר לירושלים."
          
        stop music fadeout 2.0
        jump con_intro

    ## Scene 2: Coming to the convention
    label con_intro:

        scene bg_con_entrance
        with fade

        "הגעת לכנס האנימה. בכניסה יש כמה תורים. מעולם לא ראית כל כך הרבה אנשים מחופשים!"

        "וואו, יש קבוצות שלמות של אנשים מחופשים ביחד. רגע, קוראים לזה קוספליי, נכון."
        
        "אתה מזהה כמה פיראטים שונים, יש גם אנשים עם בגדי לחימה בצבע כתום ואפילו שחקני כדורעף!"

        "לפני כל אלו יש איזשהו קוספליי עם כנפיים ענקיות ושמלה בצבע זהב, משהו משנות ה-80' שאתה לא מכיר."

        p "מזל שקניתי מראש כרטיס באתר, ככה אדלג על התור הזה."

        "אתה מוציא את קוד ה-QR שהדפסת מראש ומציג אותו למתנדב בקופה."

        m "ברוך הבא לכנס האנימה הגדול של אמא\"י!"

        "תודה רבה, האמת שזה הכנס הראשון שלי!"
        
        window hide
        # show the game's logo
        show game logo at truecenter
        with dissolve
        
        pause 3.0

        hide game logo
        with dissolve

        window show
        scene bg_con_booths
        with fade
        play music bgm_convention

        ## main branching paths
        label con_post_intro :
            p "מה הדבר הראשון שאעשה? אלך לדוכנים? אקנה מנגה? אולי אלך להרצאה? אפשר כבר לשמור מקום בקהל התחרות?"

            "חכה רגע, הבטחת שתעזור לחבריך החדשים! החלטת למי מהם תעזור?"

            menu:
                
                "כן, אעזור לאאוי עם הקוספליי":
                    jump aoi_route
                
                "כן, אעזור לשירו בתחרות האיידול":
                    jump shiro_route

                "כן, אעזור לאקאי עם ההתנדבות":
                    jump akai_route

                "רגע, על אמת? אבל אנחנו כבר חברים!" if persistent.aoi_ending == True and persistent.shiro_ending == True and persistent.akai_ending == True:
                    jump true_ending

                "האמת... אין לי כוח אליהם." if persistent.aoi_ending_bad == True and persistent.shiro_ending_bad == True and persistent.akai_ending_bad == True:
                    jump true_bad_ending

            return
    
    #####################################
    # Main Branches start here!         #
    # Hoo boy let's go                  #
    #####################################


    ## Akai Route
    label akai_route:
        return

    ## True (Good) Ending
    label true_ending:
        return

    ## True (Bad) Ending
    label true_bad_ending:
        return
