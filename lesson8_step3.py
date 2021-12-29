from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math
def calc(x,y):
    return str(int(x)+int(y))


link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_id("num1")
    x=num1.text
    num2=browser.find_element_by_id("num2")
    y=num2.text
    res = calc(x,y)
    print(res)
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(res)
    button=browser.find_element_by_css_selector("[type='submit']")
    button.click()
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
