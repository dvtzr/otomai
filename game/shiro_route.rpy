## Shiro Route
label shiro_route:
    ## first event: late to practice
    label shiro_route_1:

        show shiro stress with dissolve
        
        play music bgm_convention

        sh "אוקיי. הגענו. אני לא מאמין שאני עושה את זה."
        
        "שירו נראה כאילו הוא לחוץ מאוד ולא מצליח להירגע."
        
        p "אוקיי, בוא נעשה את זה צעד-צעד. אמרת שיש חימום, נכון? אתה יודע איפה זה מתקיים?"
        
        sh "כן, זה באיזור שמאחורי הבמה, אנחנו תמיד מתאספים שם כדי לחמם את מיתרי הקול ולתת כמה מילות עידוד. אאוי בדרך כלל מובילה את המעגל."
        
        p "אני בטוח שגם אתה יכול. זה קטן עלייך, רק חימום קצר ותרגיש הרבה יותר טוב!"

        show shiro -stress

        sh "צודק, זה לא משהו שלא עשיתי בעבר."

        "שירו מתחיל לחפש בתיק שלו את המילים לשיר שהדפיס מראש, הוא נותן לך את הפלאפון שלו לרגע."

        sh "תוכל לבדוק בשבילי מתי מתחיל החימום? אני חושב שיש לנו עוד זמן, אבל אני לא בטוח…"

        menu:
            "לפי התוכנייה האירוע מתחיל ב-10:30, אז אולי ב-09:45?":
                jump shiro_route_1_bad
            "יש לך הודעה שאומרת \" נתראה ב-09:10 \", זה זה?":
                jump shiro_route_1_good

        # bad choice
        label shiro_route_1_bad:
            
            sh sus "אתה בטוח? זה נשמע לי יחסית מאוחר."

            p "זה מה שכתוב, אין לי סיבה להמציא סתם."

            sh "טוב, אז בינתיים אעשה חזרה קצרה במסדרון. הייתי רוצה להסתובב בכנס, אבל אני לא בטוח שאצליח להרגע."

            p "מה? אז תבזבז את השעה הראשונה של הכנס במסדרון?"

            sh "כן? אתה חושב שזה בזבוז זמן?"

            menu:
                "אולי לטייל קצת בכנס יעזור לך להתנתק.":
                    pass
                "אני לא בטוח שזה מה שאני רוצה לעשות…":
                    pass
            
            show shiro -sus

            sh "צודק, ממילא אצטרך להגיע לחימום. אין סיבה לעשות את זה פעמיים. חוץ מזה, אולי חימום יתר יהרוס לי את מיתרי הקול. עדיף לנסות להפיג מתח בדוכנים."

            scene bg_con_booths with fade
            
            show shiro with dissolve

            "שירו ואתה מסתובבים בכנס ומסתכלים יחד בדוכנים. נדמה שזה עוזר להפיג את המתח, אבל שירו פספס את החימום שלו."
            
            sh @ happy "וואו, אני לא מאמין שיש אנשים כל כך מוכשרים בכנס! זו הפעם הראשונה שיש לי זמן להגיע לסחורה לפני שהכל נמכר!"

            p "כן, ואפילו הספקתי לקנות סטיק-לייט לקראת התחרות, עכשיו אוכל לעודד אותך במלוא הכוח!"

            sh "יופי, אבל עכשיו באמת כדאי לנו להזדרז, אני לא רוצה לאחר."

            stop music fadeout 1.0

            scene bg_stage_back with fade

            emi "שירו? הגעת לכנס? היינו בטוחים שהחלטת לא לבוא!"

            show shiro surprised with dissolve

            sh "למה שלא אגיע? הגעתי בדיוק בזמן לחימום!"

            emi "החימום נגמר כבר מזמן… לא הגעת אז חשבנו שלא תשתתף בתחרות. מזל שלא מחקנו את השם שלך מהרשימה של המשתתפים!"

            play music bgm_crisis

            sh shock "מה?! ה-החימום כבר קרה?! איך?! חשבתי שיש לי עוד הרבה זמן!"

            menu:
                "אני כל כך מצטער! יש משהו שנוכל לעשות?":
                    pass
                "אמרתם שלא הורדתם אותו מהרשימה, זה אומר שעדיין לא מאוחר מידי!":
                    pass

            stop music fadeout 1.0
            
            emi " שירו, הכל בסדר, זה רק החימום. אתה עדיין ברשימה. בואו רק נוודא שאנחנו מסונכרנים על השיר."

            sh stress "או-אוקיי… השיר שבחרתי הוא \"השונאן שבליבי פועם\" מהסדרה \"הפעם ההיא שהפכתי לסליים, אבל בצפון תל אביב\"."

            jump shiro_route_2

        # good choice

        label shiro_route_1_good:

            sh stress "ומה השעה עכשיו?"

            p "09:05… אולי כדאי שנרוץ?"

            sh "………"

            sh "כן."

            "שירו ואתה רצים ועוקפים את כל הדוכנים, אבל מספיקים להגיע לתחילת החימום בזמן."

            stop music fadeout 1.0

            scene bg_stage_back with fade

            show shiro mortified with dissolve

            sh "הגעתי... הגעתי, אני כאן… אני פה...!"

            "נראה שהחימום לא התחיל, אבל רוב המשתתפים כבר כאן, כולל אמה יידול ועידו וולפסט - המנהלים של התחרות."

            emi "שירו, הכל בסדר, עדיין לא התחלנו. תנשום עמוק, יהיה בסדר."

            p "רואה? הכל לפי התוכנית."

            show shiro -mortified

            play music bgm_normal

            sh "כן, אה? ממש על הקשקש. לא נורא, העיקר שהגענו."

            "שירו מסתכל סביבו ורואה את כל הזמרים המוכשרים שעומדים מולו. ההתרגשות ממש מורגשת באוויר."

            show shiro stress

            p "מה קרה?"

            sh "כולם כל כך מוצלחים… מה אם לא אהיה טוב בלי אאוי? מה אם לא אצליח לעמוד לבד על הבמה ולהדהים את הקהל? מה אם-"

            menu:
                "שירו, הכל יהיה בסדר! תן לעצמך יותר קרדיט.":
                    pass
                "Ganbare ganbare Shiro!":
                    pass
                "שירו, תאמין בי שמאמין בך!":
                    pass

            sh happy "תודה לך, באמת."

            sh "כן, אני אצליח ואהיה הכי טוב בכוחות עצמי. צעד-צעד, נכון?"

            scene black with fade

            "החימום מתחיל וכולם שרים ביחד, השירה של כולם נעימה מאוד ונראה שעומדת בפני שירו תחרות קשה. אבל למרות הכל, נראה שהשירה מרגיעה אותו."

            scene bg_stage_back with fade

            emi "כל הכבוד לכולם, שמחים לראות ולשמוע אתכם מוכנים לתחרות! אנחנו רק רוצים לוודא שהכל מוכן מאחורי הקלעים, בואו אלינו לבדוק את הקבצים כשתהיו מוכנים!"

            show shiro happy with dissolve

            sh "פיו… זה מרגיש טוב לחמם קצת את מיתרי הקול לפני התחרות."

            p "יופי, רואה? אמרתי לך שהכל יהיה בסדר!"

            sh "כן, טוב, בוא נראה שהקבצים שלי תקינים. הכל צריך להיות מושלם כדי שאעלה  עם ביטחון."

            "שירו ואתה מתקדמים לכיוון אמה ועידו, שרואים אתכם וכבר מכינים את התיקייה של שירו."

            stop music fadeout 1.0

            emi "יופי, אנחנו רואים שאאוי שלחה את כל הקבצים והם כאן, בואו רק נוודא שאנחנו על אותו קו. איזה שיר בחרת?"

            sh "השיר שבחרתי הוא \"השונאן שבליבי פועם\", מהסדרה \"הפעם ההיא שהפכתי לסליים, אבל בצפון תל אביב\"."

            $ ending_progress += 1

            jump shiro_route_2

        






        



    return