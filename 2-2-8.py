from selenium import webdriver
import time
import os

try:
    link = " http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ищем и заполняем first name
    findName = browser.find_element_by_css_selector("[name='firstname']")
    fillName = findName.send_keys("Vovan")

    # Ищем и заполняем last name
    findLast = browser.find_element_by_css_selector("[name='lastname']")
    fillLast = findLast.send_keys("Vovi")

    # Ищем и заполняем email
    findEmail = browser.find_element_by_css_selector("[name='email']")
    fillEmail = findEmail.send_keys("Vovanmail@mail.net")

    # Жмем кнопку и грузим файл
    current_dir = os.path.abspath(os.path.dirname("file.txt"))
    file_path = os.path.join(current_dir, 'file.txt')
    # element.send_keys(file_path)
    file = browser.find_element_by_id("file")
    file.send_keys(file_path)

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
