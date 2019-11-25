from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = " http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ищем значение Х и заполняем ответ
    findX = browser.find_element_by_id("input_value").text
    ans = browser.find_element_by_id("answer")
    ans.send_keys(calc(findX))

    # Жмем чек-бокс
    option1 = browser.find_element_by_css_selector("#robotCheckbox")
    option1.click()

    # Жмем радиобаттон
    option2 = browser.find_element_by_css_selector("#robotsRule")
    option2.click()
    # Отправляем заполненную форму

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что форма прошла
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
