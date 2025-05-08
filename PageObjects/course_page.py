from selenium.webdriver.common.by import By  # Used to locate elements by different strategies (ID, XPATH, etc.)
from PageObjects.base_page import BasePage  # Imports the BasePage class for reusable methods
from TestLocator.locators import Locators  # Imports locator values from a separate locators file

class CoursePage(BasePage):  # Inherits from BasePage to reuse Selenium actions

    # Element locators defined using tuples (By.<strategy>, locator_value)
    PROFILE = (By.ID, Locators.drop_down)  # Dropdown element for user profile
    SIGN_OUT_BUTTON = (By.XPATH, Locators.sign_out_button)  # Sign-out button inside the dropdown
    DROP_CONTENTS = (By.XPATH, Locators.drop_contents)  # Contents that appear after clicking profile
    LOGIN_BUTTON = (By.ID, Locators.login_button)  # Login button visible after successful sign-out

    def sign_out(self):
        # Click on the profile dropdown
        self.click(self.PROFILE)

        # Ensure the dropdown contents and sign-out button are visible and clickable
        self.is_visible(self.DROP_CONTENTS)
        self.is_visible(self.SIGN_OUT_BUTTON)
        self.is_clickable(self.SIGN_OUT_BUTTON)

        # Click the sign-out button and wait for the login button to appear
        self.click(self.SIGN_OUT_BUTTON, self.LOGIN_BUTTON, 2)









