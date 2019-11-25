from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ищем значение Х
    findX = browser.find_element_by_css_selector("#input_value")
    x = findX.text
    y = calc(x)
    # Заполняем Х
    fillAnswer = browser.find_element_by_css_selector("#answer")
    fillAnswer.send_keys(y)
    # Жмем чекбокс
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
