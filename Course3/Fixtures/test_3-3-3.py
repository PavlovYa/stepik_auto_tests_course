from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

def test_1():
    try: 
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
        input1.send_keys("Ivan")

        input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
        input2.send_keys("Ivan")

        input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
        input3.send_keys("Ivan")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        assert welcome_text == "Congratulations! You have successfully registered!"

    finally:

        time.sleep(1)
        browser.quit()

def test_2():
    try: 
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
        input1.send_keys("Ivan")

        input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
        input2.send_keys("Ivan")

        input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
        input3.send_keys("Ivan")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        assert welcome_text == "Congratulations! You have successfully registered!"

    finally:

        time.sleep(1)
        browser.quit()

pytest.main()