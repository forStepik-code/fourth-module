from selenium.webdriver.common.by import By


class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET = (By.CSS_SELECTOR, ".basket-mini .btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class CartPageLocators(object):
    ITEMS_LIST = (By.CSS_SELECTOR, "#content_inner")
    ITEM = (By.CSS_SELECTOR, ".basket-items")


class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REG_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators(object):
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner")
    BASKET_SUM = (By.CSS_SELECTOR, ".basket-mini")
    PRODUCT_NAME = (By.XPATH, "//div[@class='col-sm-6 product_main']/h1")
    PRICE = (By.XPATH, "//div[@class='col-sm-6 product_main']/p")
