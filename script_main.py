from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui
from time import sleep
from elements import input_code
import pandas

pyautogui.PAUSE = 0.3

from selenium import webdriver


driver = webdriver.Edge()

link_search = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

driver.get(link_search)

email_input = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/form/div[1]/div[1]/input")
email_input.send_keys("samteste@gmail.com")

password_input = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/form/div[1]/div[2]/input")
password_input.send_keys("12345")

sleep(2)

button_login = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/form/div[2]/button")
button_login.click()

# cadastrando produtos

table = pandas.read_csv("product.csv")

for row in table.index:

    codigo = table.loc[row, "codigo"]
    marca = table.loc[row, "marca"]
    tipo = table.loc[row, "tipo"]
    categoria = table.loc[row, "categoria"]
    preco_unitario = table.loc[row, "preco_unitario"]
    custo = table.loc[row, "custo"]

    input_code_register = driver.find_element(By.XPATH, input_code)
    input_code_register.send_keys(codigo)





sleep(10)