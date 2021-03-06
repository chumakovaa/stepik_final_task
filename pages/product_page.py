from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def compare_book_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        product_price_text = product_price.text
        message_price = self.browser.find_element(*ProductPageLocators.PRICE_MESSAGE_OF_SUCCESSFULLY_ADDED_BOOK)
        message_price_text = message_price.text
        assert product_price_text == message_price_text, f'Should be {product_price_text}'

    def compare_book_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_name_text = product_name.text
        message_name = self.browser.find_element(*ProductPageLocators.NAME_OF_SUCCESSFULLY_ADDED_BOOK)
        message_name_text = message_name.text
        assert product_name_text == message_name_text, f'Should be {product_name_text}'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE_BOOK_ADDED), "Success message is presented"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE_BOOK_ADDED), "Success message is presented"
