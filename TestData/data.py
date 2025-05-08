"""
This file contains all the data used
"""  # Module-level docstring explaining the purpose of the file


class Data:
    url = "https://www.guvi.in/"  # Base URL of the application under test
    expected_title = "GUVI | Learn to code in your native language"  # Expected page title for verification
    expected_url_after_login = "https://www.guvi.in/courses/?current_tab=myCourses"  # URL expected after successful login
    email = "manupavankumar@gmail.com"  # Valid email for login
    password = "Pavan#223"  # Valid password for login
    invalid_email = "manupavan@gmail.com"  # Invalid email for negative testing
    invalid_password = "Pavan123"  # Invalid password for negative testing
    expected_url_after_logout = "https://www.guvi.in/"  # URL expected after logging out
    expected_url_after_signup = "https://www.guvi.in/register/"  # URL expected after successful signup

