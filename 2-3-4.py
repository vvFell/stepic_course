from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Жмем кнопку
    findButton = browser.find_element_by_css_selector("button.btn")
    findButton.click()

    # мочим alert
    alert = browser.switch_to.alert
    alert.accept()

    # Тащим значение Х и заполняем ответ
    findХ = browser.find_element_by_id("input_value").text
    fillX = browser.find_element_by_id("answer")
    ans = fillX.send_keys(calc(findХ))

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
