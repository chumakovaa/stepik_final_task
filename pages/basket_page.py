from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.GO_TO_SHOPPING_LINK), 'There is no "Basket is empty" message'

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEM_IN_THE_BASKET), 'The basket is NOT empty'


