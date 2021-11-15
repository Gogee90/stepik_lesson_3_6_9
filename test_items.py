from selenium.webdriver.common.by import By
import time


# тест написан только для браузера Хром, так что не бейте меня :)
# Тест должен запускаться с параметром language следующей командой:
# pytest --language=es test_items.py
# и проходить успешно. Достаточно, чтобы код работал только для браузера ---> Сhrome <-----.


def test_button_appearance(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    time.sleep(30)
    add_to_busket_btn = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    assert add_to_busket_btn, "The page does not contain such element"
