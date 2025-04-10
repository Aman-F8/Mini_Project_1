import pytest
from selenium import webdriver                                          # To control the browser
from selenium.webdriver.chrome.service import Service                   # To specify the ChromeDriver service path
from selenium.webdriver.support.ui import WebDriverWait                 # For waiting until elements appear
from selenium.webdriver.support import expected_conditions as EC        # To use pre-defined conditions like visibility, clickability
from selenium.webdriver.common.by import By                             # To specify element locator strategies (like By.XPATH)
from selenium.common.exceptions import WebDriverException               # Handle WebDriver exceptions
from time import sleep                                                  # For adding delays

# Constants for the URL and login credentials
URL = "https://www.guvi.in/"
INVALID_EMAIL = "infouser@gmail.com"
INVALID_PASSWORD = "qwerty@123"

@pytest.fixture(scope="module")
def driver():
    try:
        # Create a Service object with the path to chromedriver
        service_obj = Service("C:/Users/dell/PycharmProjects/driver/chromedriver.exe")
        driver = webdriver.Chrome()  # You can also use: webdriver.Chrome(service=service_obj)
        # Open the GUVI website
        driver.get(URL)
        # Maximize the browser window for better visibility
        driver.maximize_window()
        # Provide the WebDriver instance to the test function
        yield driver
    # Catch and report any WebDriver related exceptions
    except WebDriverException as e:
        pytest.fail(f"Failed to load URL: {e}")
        driver.quit()

@pytest.fixture()
def open_login_page(driver):
    try:
        # Wait for the login button to become clickable and click it
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@class='⭐️rawbli-0 text-decoration-none me-3 text-success text-base font-medium']"))
        )
        login_button.click()
        # Small delay to ensure the page loads completely
        sleep(2)
    except Exception as e:
        pytest.fail(f"Error while navigating to login page: {e}")

@pytest.mark.usefixtures("open_login_page")
def test_invalid_user_login(driver):
    try:
        email_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'email')))
        email_field.clear()
        email_field.send_keys(INVALID_EMAIL)

        password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))
        password_field.clear()
        password_field.send_keys(INVALID_PASSWORD)

        login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'login-btn')))
        login_button.click()
        sleep(3)

        error_elements = driver.find_elements(By.XPATH, "//div[contains(@class, 'alert') or contains(@class, 'error')]")
        assert error_elements, "Expected error message for invalid login, but none found."
        print("Invalid Login Detected:", error_elements[0].text)
    except Exception as e:
        print("Test for invalid login failed due to an exception:", e)


