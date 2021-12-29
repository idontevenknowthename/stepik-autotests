from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))




link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    value = browser.find_element_by_id("input_value")
    x = value.text
    res = calc(x)
    input3 = browser.find_element_by_id("answer")
    input3.send_keys(res)
    chkbx = browser.find_element_by_id("robotCheckbox")
    chkbx.click()
    rb=browser.find_element_by_id("robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", rb)
    rb=rb.click()
    button=browser.find_element_by_css_selector("[type='submit']")
    button.click()

    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
