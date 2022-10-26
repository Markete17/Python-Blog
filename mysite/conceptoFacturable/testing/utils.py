import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def slow_typing(element, text):
    for character in text:
        element.send_keys(character)
        time.sleep(0.3)


def setup_chrome():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("http://localhost:8000/conceptos/")
    driver.maximize_window()
    return driver


def go_to_element(driver, pk):
    driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);")

    time.sleep(2)
    href = '//a[@href="/conceptos/'+pk+'"]'
    driver.find_element("xpath", href).click()


def login(driver):
    username = driver.find_element("name", "username")

    slow_typing(
        username,
        'marcos')
    password = driver.find_element("name", "password")
    slow_typing(
        password,
        'Hola12345')

    driver.find_element(By.TAG_NAME, 'input').submit()
