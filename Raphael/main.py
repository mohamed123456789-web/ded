from Software_Install import Software_Text_Search,Software_Install
from Anime_Search import Anime_Text_Search,Anime_Voice_Search,Anime_List,Anime_Add_List,Anime_Edit_List
from Battery_Status import Battery
from Greet_Me import GreetMe
from Listen import Listen
from Speak import Speak
from Webrowser import YoutubeSearch


def MainExecution():
    GreetMe()
    Speak("I'm Rapheal, I'm Ready To Assist You .")

    Data = Listen()
    Data = str(Data).replace(".", "")

    ValueReturn = Data
    if ValueReturn == True:
        pass

    if len(Data) < 3:
        pass

    if "battery" in Data:
        Battery()

    if "anime search" in Data  or  "search anime" in Data:
        Speak("Sir Would You Like To Type The Name of The Anime")
        reply = Listen().lower()
        if "yes" in reply:
            Anime_Text_Search()

        else:
            Speak("Sir What is The Name of The Anime")
            Anime_Voices_Search = Listen().lower()
            Anime_Voice_Search(Anime_Voices_Search)

    if "software download" in Data or "install software" in Data or "software install" in Data or "download software" in Data:
        Speak("Sir Would You Like To Type The Name of The Software")
        software_reply = Listen().lower()
        if "yes" in software_reply:
            Software_Text_Search()

        else:
            Speak("What is the name of the software")
            Software_Install(software_reply)

    if "anime list" in Data:
        Speak("as you wish sir, opening your anime watch list")
        Anime_List()

    if "watch list" in Data:
        if "change to watch list" in Data or "change to watchlist" in Data or "add anime to watchlist":
            Anime_Edit_List("watching")
        else:
            Anime_Add_List("watching")

    if "plan to watch" in Data :
        if "change to plan to watch" in Data:
            Anime_Edit_List("plan to watch")

        else:
            Anime_Add_List("plan to watch")


    if "remove from watchlist" in Data or "remove anime " in Data:
        Anime_Edit_List("remove")

    if "drop" in Data:
        if "drop anime" in Data:
            Anime_Edit_List("dropped")

    if "anime completed" in Data:
        Anime_Edit_List("completed")
MainExecution()