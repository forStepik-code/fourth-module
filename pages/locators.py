from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators(object):
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner")
    BASKET_SUM = (By.CSS_SELECTOR, ".basket-mini")
    PRODUCT_NAME = (By.XPATH, "//div[@class='col-sm-6 product_main']/h1")
    PRICE = (By.XPATH, "//div[@class='col-sm-6 product_main']/p")

