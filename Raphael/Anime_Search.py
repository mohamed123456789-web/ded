import webbrowser
import time
import pyautogui
from Speak import Speak

def Anime_Voice_Search(Anime_Voices_Search):

    url = "https://aniwatch.to/home"

    webbrowser.open_new_tab(url)

    time.sleep(5)

    search_button = pyautogui.locateOnScreen("search_button.png", confidence=0.9)
    if search_button is not None:
        search_button_center = pyautogui.center(search_button)
        pyautogui.moveTo(search_button_center)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)
        pyautogui.write(Anime_Voices_Search)
        pyautogui.press("enter")
        time.sleep(1)

        filter_button = pyautogui.locateOnScreen("filter_button.png", confidence=0.8)
        if filter_button is not None:
            filter_button_center = pyautogui.center(filter_button)
            pyautogui.moveTo(filter_button_center)
            time.sleep(3)
            pyautogui.scroll(-700)
        else:
            print("Filter button not found.")
    else:
        print("Search button not found.")
        Speak("Search button not found.")


def Anime_Text_Search():
    url = "https://aniwatch.to/home"

    webbrowser.open_new_tab(url)

    time.sleep(3)


    search_button = pyautogui.locateOnScreen("search_button.png", confidence=0.9)
    if search_button is not None:
        Anime_Texts_Search = pyautogui.prompt(text="",title="Enter Anime Name")
        search_button_center = pyautogui.center(search_button)
        pyautogui.moveTo(search_button_center)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)
        pyautogui.write(Anime_Texts_Search)
        pyautogui.press("enter")
        time.sleep(1)

        filter_button = pyautogui.locateOnScreen("filter_button.png", confidence=0.8)
        if filter_button is not None:
            filter_button_center = pyautogui.center(filter_button)
            pyautogui.moveTo(filter_button_center)
            time.sleep(3)
            pyautogui.scroll(-700)
        else:
            print("Filter button not found.")
    else:
        print("Search button not found.")
        Speak("Search button not found.")

def Anime_List():
    url = "https://aniwatch.to/user/watch-list"

    webbrowser.open_new_tab(url)

def Anime_Add_List(what_list):
    filter_button = pyautogui.locateOnScreen("filter_button.png", confidence=0.8)
    if filter_button is not None:
        filter_button_center = pyautogui.center(filter_button)
        pyautogui.moveTo(filter_button_center)
        time.sleep(3)
        pyautogui.scroll(-350)

    anime_list_button = pyautogui.locateOnScreen("Anime_Add_List.png", confidence=0.8)
    if anime_list_button is not None:
        anime_list_button_center = pyautogui.center(anime_list_button)
        time.sleep(2)
        pyautogui.moveTo(anime_list_button_center)
        time.sleep(2)
        pyautogui.click()
    if what_list == "watching":
        anime_watching = pyautogui.locateOnScreen("anime_watching.png", confidence=0.8)
        time.sleep(3)
        anime_watching_center = pyautogui.center(anime_watching)
        time.sleep(3)
        pyautogui.moveTo(anime_watching_center)
        time.sleep(2)
        pyautogui.click()
        Speak("anime added to watching list")
    else:
        Speak("Could not locate watching button")

    if what_list == "on hold" or what_list == "hold":
        anime_onhold = pyautogui.locateOnScreen("anime_onhold.png",confidence=0.8)
        anime_onhold_center = pyautogui.center(anime_onhold)
        pyautogui.moveTo(anime_onhold_center)
        pyautogui.click()
        Speak("anime added to on hold")

    if what_list == "plan to watch":
        time.sleep(3)
        anime_plan_to_watch = pyautogui.locateOnScreen("anime_plantowatch.png", confidence=0.8)
        anime_plan_to_watch_center = pyautogui.center(anime_plan_to_watch)
        pyautogui.moveTo(anime_plan_to_watch_center)
        time.sleep(2)
        pyautogui.click()
        Speak("anime added to plan to watch")

    if what_list == "dropped" or what_list == "drop":
        anime_dropped = pyautogui.locateOnScreen("anime_dropped.png",confidence=0.8)
        anime_dropped_center = pyautogui.center(anime_dropped)
        pyautogui.moveTo(anime_dropped_center)
        time.sleep(2)
        pyautogui.click()
        time.sleep(2)
        Speak("anime added to dropped list")

    if what_list == "completed":
        pyautogui.scroll(-250)
        anime_completed = pyautogui.locateOnScreen("anime_completed.png",confidence=0.8)
        anime_completed_center = pyautogui.center(anime_completed)
        pyautogui.moveTo(anime_completed_center)
        time.sleep(2)
        pyautogui.click()
        time.sleep(2)
        Speak("anime added to completed list")
    else:
        print("Filter button not found.")

def Anime_Edit_List(Edit_list):
    filter_button = pyautogui.locateOnScreen("filter_button.png", confidence=0.8)
    if filter_button is not None:
        filter_button_center = pyautogui.center(filter_button)
        pyautogui.moveTo(filter_button_center)
        time.sleep(3)
        pyautogui.scroll(-350)

    anime_edit_list_button = pyautogui.locateOnScreen("anime_edit_list_button.png",confidence=0.8)
    if anime_edit_list_button is not None:
        anime_edit_list_button_center = pyautogui.center(anime_edit_list_button)
        pyautogui.moveTo(anime_edit_list_button_center)
        time.sleep(2)
        pyautogui.click()
    if Edit_list == "watching":
        Anime_Add_List("watching")
    if Edit_list == "plan to watch":
        Anime_Add_List("plan to watch")
    if Edit_list == "drop" or Edit_list == "dropped":
        Anime_Add_List("dropped")
    if Edit_list == "completed" or Edit_list == "complete":#
        Anime_Add_List("completed")
    if Edit_list == "remove":
        anime_remove_list = pyautogui.locateOnScreen("anime_remove_list.png",confidence=0.8)
        if anime_remove_list is not None:
            anime_remove_list_center = pyautogui.center(anime_remove_list)
            pyautogui.moveTo(anime_remove_list_center)
            pyautogui.click()
            Speak("anime removed from watchlist")

