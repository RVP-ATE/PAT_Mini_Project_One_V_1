# PAT Mini Project One - Selenium Automation Framework

This project is an automated testing suite built using Python, Selenium WebDriver, and Pytest. It uses the Page Object Model (POM) design pattern to ensure scalable and maintainable test cases.

---

## 📁 Project Structure

PAT_Mini_Project_One_V_1/
├── Configuration/ # Test configuration and setup (e.g., conftest.py for fixtures)
├── PageObjects/ # Page Object Model classes (HomePage, LoginPage, etc.)
├── TestData/ # External test data (URLs, credentials, titles)
├── TestLocator/ # Element locators used in POM classes
├── TestScripts/ # Pytest-based test cases
├── .venv/ # Python virtual environment
└── .idea/ # IDE configuration files (e.g., PyCharm)


---

## ✅ Features

- URL and title validation
- Login and signup button visibility/clickability checks
- Valid and invalid login flows
- Logout verification
- Uses assertions to validate expected behavior
- Console printouts for success/failure status

---

## ⚙️ Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd PAT_Mini_Project_One_V_1


 📌 Requirements
Python 3.8+

Google Chrome (or other browser with WebDriver support)

ChromeDriver (match your Chrome version)

Selenium

Pytest

👥 Author
PAVAN KUMAR RV



