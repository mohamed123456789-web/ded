from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import pyautogui
from Speak import Speak
def Anime_Downloader(Anime_name):

    capabilities = webdriver.DesiredCapabilities.FIREFOX.copy()
    capabilities["marionette"] = True

    driver = webdriver.Firefox()

    options = Options()
    options.binary_location = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"# Optional, specify the Firefox binary path if necessary
    options.add_argument("--headless")  # Optional, run Firefox in headless mode
    options.set_preference("webdriver.gecko.driver", "C:\\Users\\ohamm\\Downloads\\geckodriver-v0.33.0-win-aarch64\\geckodriver.exe")

    driver.get("https://kayoanime.com/")

    search_box = driver.find_element(by=By.XPATH,value="/html/body/div[1]/div/div/header/div[2]/nav/div/div/div/ul/li/form/input")
    if search_box is not None:
        search_box.send_keys(Anime_name)
        search_box.send_keys(Keys.RETURN)
    else:
        Speak("Search box not found.")

    pyautogui.scroll(-150)

Anime_Downloader("demon slayer")
