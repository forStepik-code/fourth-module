import pytest
import random
import string

from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = open_product_page(browser, link)
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = open_product_page(browser, link)
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = open_product_page(browser, link)
    page.go_to_cart_page()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.has_empty_items_message()
    cart_page.is_not_have_items()


@pytest.mark.cart_user
class TestUserAddToCartFromProductPage(object):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = open_product_page(browser, self.link)
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.register_new_user("{}@{}.{}".format(randomString(), randomString(), randomString()),
                                     randomString(10))
        page.should_be_authorized_user()

    def test_user_can_add_product_to_cart(self, browser):
        page = open_product_page(browser, self.link)
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()
        page.success_message_contains_product_name(page.get_product_name())
        page.basket_contains_costs(page.get_product_price())

    def test_user_cant_see_success_message(self, browser):
        page = open_product_page(browser, self.link)
        page.success_message_is_not_exist()


def open_product_page(browser, link):
    page = ProductPage(browser, link)
    page.open()
    return page


def randomString(length=5):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))
