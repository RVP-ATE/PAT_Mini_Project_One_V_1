import time
from sys import base_prefix

# Importing required page objects and test configuration
from PageObjects.home_page import HomePage
from PageObjects.login_page import LoginPage
from PageObjects.base_page import BasePage
from PageObjects.course_page import CoursePage
from TestData.data import Data
from Configuration.conftest import driver

# TC-001: Validate the current URL after loading the page
def test_url(driver):
    driver.get(Data.url)
    base_page = BasePage(driver)

    # Assert that the actual URL matches the expected URL
    assert base_page.fetch_url() == Data.url
    print("SUCCESS: URL is valid")

# TC-002: Validate the page title
def test_title(driver):
    driver.get(Data.url)
    base_page = BasePage(driver)

    # Assert that the actual title matches the expected title
    assert base_page.fetch_title() == Data.expected_title
    print("SUCCESS: Title is valid")

# TC-003.1: Check visibility of the login button
def test_login_button_visibility(driver):
    driver.get(Data.url)
    home_page = HomePage(driver)

    # Assert that the login button is visible on the homepage
    assert home_page.login_button_visibility() is True, "FAILURE: Login Button is NOT visible"
    print("SUCCESS: Login Button is Visible")

# TC-003.2: Check if the login button is clickable
def test_login_button_clickable(driver):
    driver.get(Data.url)
    home_page = HomePage(driver)

    # Assert that the login button is clickable
    assert home_page.login_button_clickable() is True, "FAILURE: Login Button is NOT clickable"
    print("SUCCESS: Login Button is Clickable")

# TC-004.1: Check visibility of the signup button
def test_signup_button_visibility(driver):
    driver.get(Data.url)
    home_page = HomePage(driver)

    # Assert that the signup button is visible on the homepage
    assert home_page.signup_button_visibility() is True, "FAILURE: Signup Button is NOT visible"
    print("SUCCESS: Signup Button is Visible")

# TC-004.2: Check if the signup button is clickable
def test_signup_button_clickable(driver):
    driver.get(Data.url)
    home_page = HomePage(driver)

    # Assert that the signup button is clickable
    assert home_page.signup_button_visibility() is True, "FAILURE: Signup Button is NOT clickable"
    print("SUCCESS: Signup Button is Clickable")

# TC-005: Validate the URL after clicking the signup button
def test_signup_page_url(driver):
    driver.get(Data.url)
    home_page = HomePage(driver)
    home_page.click_signup()
    base_page = BasePage(driver)

    # Assert that the redirected URL matches the expected signup URL
    assert base_page.fetch_url() == Data.expected_url_after_signup
    print("SUCCESS: URL is valid")

# TC-006.1: Verify email input field is empty upon opening login page
def test_email_input(driver):
    driver.get(Data.url)
    home_page = HomePage(driver)
    home_page.click_login()
    login_page = LoginPage(driver)

    # Assert that the email input field is empty
    assert login_page.validate_email_box(), "FAILURE: Email textbox is not empty"
    print("SUCCESS: Email textbox is empty")

# TC-006.2: Verify password input field is empty upon opening login page
def test_password_input(driver):
    driver.get(Data.url)
    home_page = HomePage(driver)
    home_page.click_login()
    login_page = LoginPage(driver)

    # Assert that the password input field is empty
    assert login_page.validate_password_box(), "FAILURE: Password textbox is not empty"
    print("SUCCESS: Password textbox is empty")

# TC-006: Perform a valid login and verify successful login
def test_valid_login(driver):
    driver.get(Data.url)
    home_page = HomePage(driver)
    home_page.click_login()
    login_page = LoginPage(driver)
    login_page.enter_valid_email()
    login_page.enter_valid_password()
    login_page.click_login()

    # Assert that the URL after login matches the expected URL
    assert Data.expected_url_after_login == driver.current_url
    print("SUCCESS: Login successful")

# TC-007: Perform logout after login and verify successful logout
def test_logout(driver):
    driver.get(Data.url)
    home_page = HomePage(driver)
    home_page.click_login()
    login_page = LoginPage(driver)
    login_page.enter_valid_email()
    login_page.enter_valid_password()
    login_page.click_login()
    course_page = CoursePage(driver)
    course_page.sign_out()

    # Assert that the URL after logout matches the expected logout URL
    assert Data.expected_url_after_logout == driver.current_url
    print("SUCCESS: Logout successful")

# TC-008: Attempt invalid login and verify failure
def test_invalid_login(driver):
    driver.get(Data.url)
    home_page = HomePage(driver)
    home_page.click_login()
    login_page = LoginPage(driver)
    login_page.enter_invalid_email()
    login_page.enter_invalid_password()
    login_page.click_login_Invalid()

    # Assert that the URL did not change to the authenticated user page
    assert Data.expected_url_after_login != driver.current_url
    print("SUCCESS: Login unsuccessful")












