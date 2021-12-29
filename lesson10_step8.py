from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))




link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    value=browser.find_element_by_id("input_value")
    button=browser.find_element_by_id("book")
    button.click()
    value=browser.find_element(By.ID, "input_value")
    x = value.text
    res = calc(x)
    input3 = browser.find_element_by_id("answer")
    input3.send_keys(res)
    button=browser.find_element_by_css_selector("[type='submit']")
    button.click()

    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
