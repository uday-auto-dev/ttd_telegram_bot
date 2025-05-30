import json
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def fetch_ttd_notifications():
    options = webdriver.ChromeOptions()
    options.add_argument("headless")  # Use headless if needed
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(5)

    driver.get(os.environ["TTD_URL"])
    time.sleep(2)

    elements = driver.find_elements(By.XPATH, "//div[@class='card_scroll']/ul/li/p[1]")
    current = [e.text.strip() for e in elements if e.text.strip()]

    driver.quit()
    return current