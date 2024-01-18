from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import os
import time

service = ChromeService(executable_path=ChromeDriverManager().install())
contador_execucoes = 0
limite_execucoes = 1000
driver = webdriver.Chrome(service=service)
while contador_execucoes < limite_execucoes:
    try:
        link_to_open = 'https://www.blockaway.net'
        driver.get(link_to_open)

        text_box = driver.find_element(By.ID, 'url')

        text_box.send_keys(f'www.twitch.tv/kufipov')
        botao = driver.find_element(By.XPATH, '//*[@id="requestSubmit"]')
        botao.click()
        time.sleep(70)
        contador_execucoes += 1
    except Exception as e:
        print('Ocorreu um erro')
    time.sleep(10)

driver.quit()