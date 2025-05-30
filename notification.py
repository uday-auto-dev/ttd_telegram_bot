import json
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

data_path = "data/info.json"
with open(data_path) as f:
    data_json = json.load(f)
    data = data_json["data"][0]

def fetch_ttd_notifications():
    options = webdriver.ChromeOptions()
    options.add_argument("headless")  # Use headless if needed
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(5)

    # driver.get(data["TTD_URL"])
    driver.get(os.environ["TTD_URL"])
    time.sleep(2)

    elements = driver.find_elements(By.XPATH, "//div[@class='card_scroll']/ul/li/p[1]")
    current = [e.text.strip() for e in elements if e.text.strip()]

    driver.quit()
    return current