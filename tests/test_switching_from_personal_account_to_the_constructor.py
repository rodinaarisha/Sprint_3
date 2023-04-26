from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestLocators


class TestSwitchingFromAccount:

    def test_switching_click_the_Constructor(self, driver):
        driver.find_element(*TestLocators.button_personal_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.form_for_filling))
        driver.find_element(*TestLocators.field_registration_login).send_keys('arina_rodina_09@yandex.ru')
        driver.find_element(*TestLocators.field_registration_password).send_keys('123456')
        driver.find_element(*TestLocators.button_input).click()
        WebDriverWait(driver, 8).until(expected_conditions.visibility_of_element_located(TestLocators.button_personal_account))
        driver.find_element(*TestLocators.button_personal_account).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.button_exit))
        driver.find_element(*TestLocators. button_constructor).click()
        WebDriverWait(driver, 8).until(expected_conditions.visibility_of_element_located(TestLocators.title_collect_burger))
        burger_link = driver.find_element(*TestLocators.title_collect_burger)
        assert burger_link.text == 'Соберите бургер', 'Название "Соберите бургер отображается на странице"'

    def test_switching_click_the_logo_Stellar_Burgers(self, driver):
        driver.find_element(*TestLocators.button_personal_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.form_for_filling))
        driver.find_element(*TestLocators.field_registration_login).send_keys('arina_rodina_09@yandex.ru')
        driver.find_element(*TestLocators.field_registration_password).send_keys('123456')
        driver.find_element(*TestLocators.button_input).click()
        WebDriverWait(driver, 8).until(expected_conditions.visibility_of_element_located(TestLocators.button_personal_account))
        driver.find_element(*TestLocators.button_personal_account).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.button_exit))
        driver.find_element(*TestLocators.button_stellar_burgers).click()
        WebDriverWait(driver, 8).until(expected_conditions.visibility_of_element_located(TestLocators.title_collect_burger))
        burger_link = driver.find_element(*TestLocators.title_collect_burger)
        assert burger_link.text == 'Соберите бургер', 'Название "Соберите бургер отображается на странице"'
