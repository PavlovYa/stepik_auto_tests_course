from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/math.html")

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    element0 = browser.find_element(By.CSS_SELECTOR, "#answer")
    element0.send_keys(y)

    element1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    element1.click()

    element2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    element2.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла