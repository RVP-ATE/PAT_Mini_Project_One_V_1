"""
This file contains all the web locators like xpath, id, tag name, link text etc.,
"""  # Docstring describing the purpose of this file


class Locators:

    # common
    login_button = "login-btn"  # ID of the login button (used across multiple pages)

    # login page
    email_locator = "email"  # ID of the email input field
    password_locator = "password"  # ID of the password input field

    # signup page
    signup_page = "signup-btn"  # ID of the sign-up button or identifier on the signup page

    # homepage
    signup_button = "//a[text()='Sign up']"  # XPath for the sign-up button on the home page
    error_message = "//div[@class='invalid-feedback']"  # XPath for error message after invalid login

    # course page
    drop_contents = "//*[@id='drop_contents']"  # XPath for the dropdown contents (e.g., after login)
    drop_down = "dropdown_container"  # ID of the dropdown button/menu
    sign_out_button = "//div[text()='Sign Out']"  # XPath for the "Sign Out" option in the dropdown



