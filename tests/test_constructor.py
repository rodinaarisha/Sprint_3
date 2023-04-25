from selenium import webdriver
from selenium.webdriver.common.by import By


def test_constructor_switch_to_sauces_tab():
    chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument('--headless')
    chrome_options.add_argument('--window-size=1000,992')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://stellarburgers.nomoreparties.site")
    sauces = driver.find_element(By.XPATH, ".//span[@class='text text_type_main-default' and text()='Соусы']")
    sauces.click()
    sauces_label=driver.find_element(By.XPATH,".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Соусы']")
    example_sauce=driver.find_element(By.XPATH, ".//p[@class='BurgerIngredient_ingredient__text__yp3dH' and text()='Соус Spicy-X']")
    assert sauces_label.text =='Соусы' and example_sauce.text=='Соус Spicy-X'
    driver.quit()


def test_constructor_switch_to_fillings_tab():
    chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument('--headless')
    chrome_options.add_argument('--window-size=1000,992')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://stellarburgers.nomoreparties.site")
    fillings = driver.find_element(By.XPATH, ".//span[@class='text text_type_main-default' and text()='Начинки']")
    fillings.click()
    fillings_label=driver.find_element(By.XPATH,".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Начинки']")
    example_fillings=driver.find_element(By.XPATH, ".//p[@class='BurgerIngredient_ingredient__text__yp3dH' and text()='Говяжий метеорит (отбивная)']")
    assert fillings_label.text =='Начинки' and example_fillings.text=='Говяжий метеорит (отбивная)'
    driver.quit()


def test_constructor_switch_to_fillings_tab():
    chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument('--headless')
    chrome_options.add_argument('--window-size=1000,992')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://stellarburgers.nomoreparties.site")
    fillings = driver.find_element(By.XPATH, ".//span[@class='text text_type_main-default' and text()='Начинки']")
    fillings.click()
    breads = driver.find_element(By.XPATH, ".//span[@class='text text_type_main-default' and text()='Булки']")
    breads.click()
    breads_label = driver.find_element(By.XPATH,".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Булки']")
    example_breads = driver.find_element(By.XPATH, ".//p[@class='BurgerIngredient_ingredient__text__yp3dH' and text()='Флюоресцентная булка R2-D3']")
    assert breads_label.text =='Булки' and example_breads.text =='Флюоресцентная булка R2-D3'
    driver.quit()
