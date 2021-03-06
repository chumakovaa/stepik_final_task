from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')
    INPUT_REGISTER_EMAIL = (By.CSS_SELECTOR, '[name="registration-email"]')
    INPUT_REGISTER_PASSWORD = (By.CSS_SELECTOR, '[name="registration-password1"]')
    INPUT_REPEAT_REGISTER_PASSWORD = (By.CSS_SELECTOR, '[name="registration-password2"]')
    SUBMIT_REGISTRATION_BUTTON = (By.CSS_SELECTOR, '[name="registration_submit"]')


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
    GO_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-group a.btn')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    GO_TO_SHOPPING_LINK = (By.CSS_SELECTOR, '#content_inner a')
    ITEM_IN_THE_BASKET = (By.CSS_SELECTOR, '.basket-items')
    SELECTED_LANGUAGE = (By.CSS_SELECTOR, 'option[selected="selected"]')