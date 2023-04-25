from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def test_input_login_via_the_button_in_the_registration_form(email, password):
    chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument('--headless')
    chrome_options.add_argument('--window-size=1000,992')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://stellarburgers.nomoreparties.site/register")
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "Auth_login__3hAey")))
    input_from_registration = driver.find_element(By.LINK_TEXT, 'Войти')
    input_from_registration.click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "Auth_login__3hAey")))
    driver.find_element(By.XPATH, ".//fieldset[1]//input").send_keys(email)
    driver.find_element(By.XPATH, ".//input[@class='text input__textfield text_type_main-default' and @type='password']").send_keys(password)
    driver.find_element(By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg' and text()='Оформить заказ']")))
    order_button = driver.find_element(By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg' and text()='Оформить заказ']")
    assert order_button.text == 'Оформить заказ'
    driver.quit()


def test_input_login_via_button_personal_account(email,password):
    chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument('--headless')
    chrome_options.add_argument('--window-size=1000,992')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://stellarburgers.nomoreparties.site/")
    personal_account = driver.find_element(By.LINK_TEXT, 'Личный Кабинет')
    personal_account.click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "Auth_login__3hAey")))
    driver.find_element(By.XPATH, ".//fieldset[1]//input").send_keys(email)
    driver.find_element(By.XPATH, ".//input[@class='text input__textfield text_type_main-default' and @type='password']").send_keys(password)
    driver.find_element(By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg' and text()='Оформить заказ']")))
    order_button = driver.find_element(By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg' and text()='Оформить заказ']")
    assert order_button.text == 'Оформить заказ'
    driver.quit()


def test_input_login_via_button_personal_account(email, password):
    chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument('--headless')
    chrome_options.add_argument('--window-size=1000,992')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg' and text()='Войти в аккаунт']").click()
    driver.find_element(By.XPATH, ".//fieldset[1]//input").send_keys(email)
    driver.find_element(By.XPATH, ".//input[@class='text input__textfield text_type_main-default' and @type='password']").send_keys(password)
    driver.find_element(By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg' and text()='Оформить заказ']")))
    order_button = driver.find_element(By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg' and text()='Оформить заказ']")
    assert order_button.text == 'Оформить заказ'
    driver.quit()


def test_input_login_via_password_recovery_button(email, password):
    chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument('--headless')
    chrome_options.add_argument('--window-size=1000,992')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg' and text()='Войти в аккаунт']").click()
    driver.find_element(By.XPATH, ".//a[@class='Auth_link__1fOlj' and text()='Восстановить пароль']").click()
    driver.find_element(By.XPATH, ".//a[@class='Auth_link__1fOlj' and text()='Войти']").click()
    driver.find_element(By.XPATH, './/fieldset[1]//input').send_keys(email)
    driver.find_element(By.XPATH, ".//input[@class='text input__textfield text_type_main-default' and @type='password']").send_keys(password)
    driver.find_element(By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg' and text()='Оформить заказ']")))
    order_button = driver.find_element(By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg' and text()='Оформить заказ']")
    assert order_button.text == 'Оформить заказ'
    driver.quit()
