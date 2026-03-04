from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

chrome_path = r"C:\development\chromedriver-win64\chromedriver.exe"
service = Service(chrome_path)
driver = webdriver.Chrome()

driver.get("https://translate.yandex.com/en/?source_lang=en&target_lang=am")
wait = WebDriverWait(driver, 15)

while True:
    my_text = input("What's your text: ")
    wait.until(EC.presence_of_element_located((By.ID,"fakeArea"))).send_keys(my_text)
    driver.find_element(By.ID,"fakeArea").send_keys(my_text)
    waiting_time = len(my_text)/5
    print(waiting_time)
    time.sleep(2)
    answer = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"span.YPkS7KbdpWfGdYKd3QB9")))
    print(answer.text)

driver.close()