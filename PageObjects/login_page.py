from selenium.webdriver.common.by import By  # For locating elements using ID, XPATH, etc.
from PageObjects.base_page import BasePage  # Inherits reusable methods from BasePage
from TestLocator.locators import Locators  # Imports locator values from the locators module
from TestData.data import Data  # Imports test data like valid/invalid email and password


class LoginPage(BasePage):  # Represents the login page and actions that can be performed on it

    # Locators for input fields and buttons
    EMAIL_INPUT = (By.ID, Locators.email_locator)  # Locator for the email input field
    PASSWORD_INPUT = (By.ID, Locators.password_locator)  # Locator for the password input field
    LOGIN_BUTTON = (By.ID, Locators.login_button)  # Locator for the login button
    DROP_DOWN = (By.ID, Locators.drop_down)  # Locator for the dropdown after successful login


    def enter_valid_email(self):
        # Enters a valid email from test data into the email field
        self.enter_text(self.EMAIL_INPUT, Data.email)

    def enter_valid_password(self):
        # Enters a valid password from test data into the password field
        self.enter_text(self.PASSWORD_INPUT, Data.password)

    def enter_invalid_email(self):
        # Enters an invalid email from test data
        self.enter_text(self.EMAIL_INPUT, Data.invalid_email)

    def enter_invalid_password(self):
        # Enters an invalid password from test data
        self.enter_text(self.PASSWORD_INPUT, Data.invalid_password)

    def click_login(self):
        # Clicks the login button and waits for dropdown element to appear (indicating successful login)
        self.click(self.LOGIN_BUTTON, self.DROP_DOWN, 5)

    def click_login_Invalid(self):
        # Clicks the login button without waiting for dropdown (used for invalid login)
        self.click(self.LOGIN_BUTTON)

    def validate_email_box(self):
        # Returns True if the email input field is empty
        email_input = self.find_element(self.EMAIL_INPUT)
        value = email_input.get_attribute("value")
        return value == ""

    def validate_password_box(self):
        # Returns True if the password input field is empty
        password_input = self.find_element(self.PASSWORD_INPUT)
        value = password_input.get_attribute("value")
        return value == ""
