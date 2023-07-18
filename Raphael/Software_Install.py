import webbrowser
import time
import pyautogui
from Speak import Speak

def Software_Install(Software_Name):
    url = "https://getintopc.com/"

    webbrowser.open_new_tab(url)

    time.sleep(3)

    search_button_software = pyautogui.locateOnScreen("search_button_software.png", confidence=0.8)
    if search_button_software is not None:
        search_button_software_center = pyautogui.center(search_button_software)
        pyautogui.moveTo(search_button_software_center)
        pyautogui.click()
        time.sleep(4)
        pyautogui.write(Software_Name)
        pyautogui.press("enter")
        time.sleep(4)

        filter_button = pyautogui.locateOnScreen("filter_button.png", confidence=0.8)
        if filter_button is not None:
            filter_button_center = pyautogui.center(filter_button)
            pyautogui.moveTo(filter_button_center)
            time.sleep(3)
            pyautogui.scroll(-200)

    else:
        print("Search button not found.")
        Speak("Search button not found.")

def Software_Text_Search():
    url = "https://getintopc.com/"

    webbrowser.open_new_tab(url)

    time.sleep(3)

    search_button_software = pyautogui.locateOnScreen("search_button_software.png", confidence=0.8)
    if search_button_software is not None:
        search_text_software = pyautogui.prompt(text="",title="Enter Anime Name")
        search_button_software_center = pyautogui.center(search_button_software)
        pyautogui.moveTo(search_button_software_center)
        pyautogui.click()
        time.sleep(4)
        pyautogui.write(search_text_software)
        pyautogui.press("enter")
        time.sleep(4)

        filter_button = pyautogui.locateOnScreen("filter_button.png", confidence=0.8)
        if filter_button is not None:
            filter_button_center = pyautogui.center(filter_button)
            pyautogui.moveTo(filter_button_center)
            time.sleep(3)
            pyautogui.scroll(-200)

    else:
        print("Search button not found.")
        Speak("Search button not found.")

