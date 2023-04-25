from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import random


def test_registration_entering_a_password_of_3_symbols():
    chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument('--headless')
    chrome_options.add_argument('--window-size=1000,992')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://stellarburgers.nomoreparties.site/register")
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "Auth_login__3hAey")))
    name = 'Test'
    email = f"arina_rodina_09_{random.randint(100, 999)}@yandex.ru"
    password_incorrect = '123'
    driver.find_element(By.XPATH, './/fieldset[1]//input').send_keys(name)
    driver.find_element(By.XPATH, './/fieldset[2]//input').send_keys(email)
    password_locator = driver.find_element(By.XPATH, ".//input[@class='text input__textfield text_type_main-default' and @type='password']")
    password_locator.send_keys(password_incorrect)
    assert len(password_locator.get_attribute('value')) <= 6
    driver.quit()


def test_registration_check_issue_for_incorrect_password(name):
    chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument('--headless')
    chrome_options.add_argument('--window-size=1000,992')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://stellarburgers.nomoreparties.site/register")
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "Auth_login__3hAey")))
    email = f"arina_rodina_09_{random.randint(100, 999)}@yandex.ru"
    password_incorrect = '123'
    driver.find_element(By.XPATH, './/fieldset[1]//input').send_keys(name)
    driver.find_element(By.XPATH, './/fieldset[2]//input').send_keys(email)
    password_locator = driver.find_element(By.XPATH, ".//input[@class='text input__textfield text_type_main-default' and @type='password']")
    password_locator.send_keys(password_incorrect)
    button_registration = driver.find_element(By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")
    button_registration.click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//p[@class='input__error text_type_main-default']")))
    negative_error = driver.find_element(By.XPATH, ".//p[@class='input__error text_type_main-default']")
    assert negative_error.text == 'Некорректный пароль'
    driver.quit()


def test_registration_filling_in_the_name_and_email_fields(name):
    chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument('--headless')
    chrome_options.add_argument('--window-size=1000,992')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://stellarburgers.nomoreparties.site/register")
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "Auth_login__3hAey")))
    email = f"arina_rodina_09_{random.randint(100, 999)}@yandex.ru"
    driver.find_element(By.XPATH, './/fieldset[1]//input').send_keys(name)
    driver.find_element(By.XPATH, './/fieldset[2]//input').send_keys(email)
    filling_value = driver.find_element(By.XPATH, './/fieldset[1]//input').get_attribute('value')
    filling_email = driver.find_element(By.XPATH, './/fieldset[2]//input').get_attribute('value')
    assert filling_value == name and filling_email == email
    driver.quit()


def test_registration_successful_registration(name):
    chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument('--headless')
    chrome_options.add_argument('--window-size=1000,992')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://stellarburgers.nomoreparties.site/register")
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "Auth_login__3hAey")))
    email = f"arina_rodina_09_{random.randint(100, 999)}@yandex.ru"
    password_correct = '123456'
    driver.find_element(By.XPATH, './/fieldset[1]//input').send_keys(name)
    driver.find_element(By.XPATH, './/fieldset[2]//input').send_keys(email)
    password_locator = driver.find_element(By.XPATH, ".//input[@class='text input__textfield text_type_main-default' and @type='password']")
    password_locator.send_keys(password_correct)
    button_registration = driver.find_element(By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")
    button_registration.click()
    WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "Auth_login__3hAey")))
    assert 'Войти' in driver.find_element(By.CLASS_NAME, "Auth_login__3hAey").text
    driver.quit()
