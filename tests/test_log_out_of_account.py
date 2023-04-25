from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def test_log_out_log_out_from_account(email, password):
    chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument('--headless')
    chrome_options.add_argument('--window-size=1000,992')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.LINK_TEXT, 'Личный Кабинет').click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "Auth_login__3hAey")))
    driver.find_element(By.XPATH, './/fieldset[1]//input').send_keys(email)
    driver.find_element(By.XPATH, ".//input[@class='text input__textfield text_type_main-default' and @type='password']").send_keys(password)
    driver.find_element(By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
    WebDriverWait(driver, 8).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, 'Личный Кабинет')))
    driver.find_element(By.LINK_TEXT, 'Личный Кабинет').click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[@class='Account_button__14Yp3 text text_type_main-medium text_color_inactive']")))
    driver.find_element(By.XPATH, ".//button[@class='Account_button__14Yp3 text text_type_main-medium text_color_inactive']").click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//div[@class='Auth_login__3hAey']/h2")))
    assert driver.find_element(By.XPATH, ".//div[@class='Auth_login__3hAey']/h2").text == 'Вход'
    driver.quit()
