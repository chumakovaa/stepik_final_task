from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, 'btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    NAME_OF_SUCCESSFULLY_ADDED_BOOK = (By.CSS_SELECTOR, '.alert-success:first-child strong')
    PRICE_MESSAGE_OF_SUCCESSFULLY_ADDED_BOOK = (By.CSS_SELECTOR, '.alert-info strong')
    SUCCESS_MESSAGE_BOOK_ADDED = (By.CLASS_NAME, 'alertinner')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")