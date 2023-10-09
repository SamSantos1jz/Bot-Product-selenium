from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui
import time

pyautogui.PAUSE = 0.3

from selenium import webdriver


driver = webdriver.Edge()

link_search = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

driver.get(link_search)

email_input = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/form/div[1]/div[1]/input")
email_input.send_keys("samteste@gmail.com")

password_input = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/form/div[1]/div[2]/input")
password_input.send_keys("12345")

button_login = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/form/div[2]/button")
button_login.click()

time.sleep(10)


driver.quit()