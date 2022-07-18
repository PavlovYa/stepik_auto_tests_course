import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

class TestMainPage2():
    @pytest.mark.parametrize('linknumber', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905",])
    def test_guest_should_see_login_link (self, browser, linknumber):
        link = f"https://stepik.org/lesson/{linknumber}/step/1"
        browser.get(link)
        browser.implicitly_wait(10)     
        box = browser.find_element(By.CSS_SELECTOR, 'textarea')
        time.sleep(2)  
        box.send_keys(str(math.log(int(time.time()))))
        browser.implicitly_wait(10)

        button = browser.find_element(By.CSS_SELECTOR, ".submit-submission")        
        WebDriverWait(browser, 12).until(
        EC.element_to_be_clickable(button)
        )
        button.click()

        WebDriverWait(browser, 12).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint"))
        )
        msg = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint")
        assert msg.text =="Correct!"
        # print(msg.text)

