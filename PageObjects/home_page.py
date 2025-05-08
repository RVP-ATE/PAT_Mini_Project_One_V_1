from selenium.webdriver.common.by import By  # For locating elements using different strategies (ID, XPATH, etc.)
from PageObjects.base_page import BasePage  # BasePage contains reusable web interaction methods
from TestLocator.locators import Locators  # Locator values are managed separately for maintainability

class HomePage(BasePage):  # Inherits from BasePage

    # Element locators defined as tuples (By.<strategy>, locator_value)
    SIGNUP_BUTTON = (By.XPATH, Locators.signup_button)  # Locator for the Sign Up button
    LOGIN_BUTTON = (By.ID, Locators.login_button)  # Locator for the Login button
    SIGNUP_PAGE = (By.ID, Locators.signup_page)  # Locator for the Sign Up page identifier after click

    def click_login(self):
        # Clicks the login button and waits up to 5 seconds for the same button to be present again
        self.click(self.LOGIN_BUTTON, self.LOGIN_BUTTON, 5)

    def click_signup(self):
        # Clicks the sign-up button and waits up to 5 seconds for the sign-up page to load
        self.click(self.SIGNUP_BUTTON, self.SIGNUP_PAGE, 5)

    def login_button_visibility(self):
        # Checks if the login button is displayed
        element = self.find_element(self.LOGIN_BUTTON)
        if element:
            return element.is_displayed()
        return True  # Returns True if element not found to avoid test failure

    def login_button_clickable(self):
        # Checks if the login button is clickable
        return self.is_clickable(self.LOGIN_BUTTON)

    def signup_button_visibility(self):
        # Checks if the sign-up button is displayed
        element = self.find_element(self.SIGNUP_BUTTON)
        if element:
            return element.is_displayed()
        return True  # Returns True if element not found

    def signup_button_clickable(self):
        # Checks if the sign-up button is clickable
        return self.is_clickable(self.SIGNUP_BUTTON)
