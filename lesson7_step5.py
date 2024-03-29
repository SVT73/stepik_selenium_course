import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

# link = "http://suninjuly.github.io/simple_form_find_task.html"
link = "https://suninjuly.github.io/math.html"

try:
    browser = webdriver.Firefox()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, '[id="input_value"]')
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    input2 = browser.find_element(By.ID, "robotCheckbox")
    input2.click()
    input3 = browser.find_element(By.ID, "robotsRule")
    input3.click()
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла