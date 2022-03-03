from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.browser.current_url, '"Login" not in url'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form is not presented'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Register form is not presented'

    def register_new_user(self, email, password):
        input_register_email = self.browser.find_element(*LoginPageLocators.INPUT_REGISTER_EMAIL)
        input_register_email.send_keys(email)
        input_register_password = self.browser.find_element(*LoginPageLocators.INPUT_REGISTER_PASSWORD)
        input_register_password.send_keys(password)
        input_repeat_register_password = self.browser.find_element(*LoginPageLocators.INPUT_REPEAT_REGISTER_PASSWORD)
        input_repeat_register_password.send_keys(password)
        submit_registration_button = self.browser.find_element(*LoginPageLocators.SUBMIT_REGISTRATION_BUTTON)
        submit_registration_button.click()
