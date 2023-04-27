from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestLocators


class TestTransferToAccount:

    def test_check_history(self, driver):
        driver.find_element(*TestLocators.button_personal_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.form_for_filling))
        driver.find_element(*TestLocators.field_registration_login).send_keys('arina_rodina_09@yandex.ru')
        driver.find_element(*TestLocators.field_registration_password).send_keys('123456')
        driver.find_element(*TestLocators.button_input).click()
        WebDriverWait(driver, 8).until(expected_conditions.visibility_of_element_located(TestLocators.button_personal_account))
        driver.find_element(*TestLocators.button_personal_account).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.button_history_shop))
        history_shop = driver.find_element(*TestLocators.button_history_shop)
        assert history_shop.text == 'История заказов', "В личном кабинете должен отображаться раздел 'История заказов'"
