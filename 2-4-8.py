from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # говорим Selenium проверять в течение 10 секунд, пока сумма не будет =100
    button = WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    # Жмем кнопку
    findButton = browser.find_element_by_id("book")
    findButton.click()

    # Переключаемся на другое окно
    # new_window = browser.window_handles[1]
    # browser.switch_to.window(new_window)

    # Тащим значение Х и заполняем ответ
    findХ = browser.find_element_by_id("input_value").text
    fillX = browser.find_element_by_id("answer")
    ans = fillX.send_keys(calc(findХ))

    # Отправляем заполненную форму
    button = browser.find_element_by_id("solve")
    button.click()

    # Проверяем, что форма прошла
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
