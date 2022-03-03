from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_empty_message(self):
        # Т.к. не смогла подобрать уникальный селектор сообщения (чтобы он отсутствовал в корзине, где добавлены товары)
        # решила сравнивать по линку, который из пустой корзины должен вести на Main page
        selected_language = self.browser.find_element(*BasketPageLocators.SELECTED_LANGUAGE)
        selected_language_value = selected_language.get_attribute('value')
        link = self.browser.find_element(*BasketPageLocators.GO_TO_SHOPPING_LINK)
        link.click()
        assert self.browser.current_url == f'http://selenium1py.pythonanywhere.com/{selected_language_value}/', \
            'There is no "Basket is empty" message'

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEM_IN_THE_BASKET), 'The basket is NOT empty'


