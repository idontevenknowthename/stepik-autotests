from selenium import webdriver
import time


link = "http://suninjuly.github.io/registration1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_class_name("first")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_class_name("second")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name("third")
    input3.send_keys("petrov@mail.ru")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(3)
    welcome_text_elt=browser.find_element_by_tag_name("h1")
    welcome_text=welcome_text_elt.text
    assert"Congratulations! You have successfully registered!"==welcome_text

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
