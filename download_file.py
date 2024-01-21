import time

from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": "C:\\Users\\aev32\\PycharmProjects\\QA_GURU_Python_9_7\\tmp",
    "download.prompt_for_download": False
}
options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
browser.config.driver = driver

browser.open("https://github.com/pytest-dev/pytest/blob/main/README.rst")
browser.element("[data-testid='download-raw-button']").click()
time.sleep(5)
