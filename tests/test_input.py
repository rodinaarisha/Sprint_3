from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestLocators


class TestInput:

    def test_input_login_via_the_button_in_the_registration_form(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.form_for_filling))
        driver.find_element(*TestLocators.button_input_registration).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.form_for_filling))
        driver.find_element(*TestLocators.field_registration_login).send_keys('arina_rodina_09@yandex.ru')
        driver.find_element(*TestLocators.field_registration_password).send_keys('123456')
        driver.find_element(*TestLocators.button_input).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.button_place_an_order))
        order_button = driver.find_element(*TestLocators.button_place_an_order)
        assert order_button.text == 'Оформить заказ', 'Кнопка "Оформить" заказ должна отображаться после авторизации'

    def test_input_login_via_button_personal_account(self, driver):
        driver.find_element(*TestLocators.button_personal_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.form_for_filling))
        driver.find_element(*TestLocators.field_registration_login).send_keys('arina_rodina_09@yandex.ru')
        driver.find_element(*TestLocators.field_registration_password).send_keys('123456')
        driver.find_element(*TestLocators.button_input).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.button_place_an_order))
        order_button = driver.find_element(*TestLocators.button_place_an_order)
        assert order_button.text == 'Оформить заказ', 'Кнопка "Оформить" заказ должна отображаться после авторизации'

    def test_input_login_via_button_input_to_account(self, driver):
        driver.find_element(*TestLocators.button_input_to_account).click()
        driver.find_element(*TestLocators.field_registration_login).send_keys('arina_rodina_09@yandex.ru')
        driver.find_element(*TestLocators.field_registration_password).send_keys('123456')
        driver.find_element(*TestLocators.button_input).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.button_place_an_order))
        order_button = driver.find_element(*TestLocators.button_place_an_order)
        assert order_button.text == 'Оформить заказ', 'Кнопка "Оформить" заказ должна отображаться после авторизации'

    def test_input_login_via_password_recovery_button(self, driver):
        driver.find_element(*TestLocators.button_input_to_account).click()
        driver.find_element(*TestLocators.return_password).click()
        driver.find_element(*TestLocators.button_input_return_password).click()
        driver.find_element(*TestLocators.field_registration_login).send_keys('arina_rodina_09@yandex.ru')
        driver.find_element(*TestLocators.field_registration_password).send_keys('123456')
        driver.find_element(*TestLocators.button_input).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.button_place_an_order))
        order_button = driver.find_element(*TestLocators.button_place_an_order)
        assert order_button.text == 'Оформить заказ', 'Кнопка "Оформить" заказ должна отображаться после авторизации'
