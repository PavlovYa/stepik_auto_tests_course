from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")

    first = browser.find_element(By.CSS_SELECTOR, "#num1")
    x = first.text
    second = browser.find_element(By.CSS_SELECTOR, "#num2")
    y = second.text

    answer = int(x) + int(y)

    select = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
    select.select_by_value(str(answer))
    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла