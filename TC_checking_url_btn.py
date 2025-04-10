# Importing required modules
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import requests
from time import sleep

# Constants
URL = "https://www.guvi.in"
EXPECTED_TITLE = "GUVI | Learn to code in your native language"


# Fixture to launch browser for the test module
@pytest.fixture(scope="module")
def driver():
    # Create ChromeDriver service
    service_obj = Service("C:/Users/dell/PycharmProjects/driver/chromedriver.exe")
    driver = webdriver.Chrome()  # Optionally use: webdriver.Chrome(service=service_obj)
    driver.maximize_window()  # Maximize browser window
    yield driver  # Provide driver instance to tests
    driver.quit()  # Quit browser after tests complete


# TC1 - Check if the website URL is accessible (HTTP 200)
def test_tc1_check_url_valid():
    try:
        # Send GET request to the website
        response = requests.get(URL)

        # Assert that the status code is 200 (OK)
        assert response.status_code == 200, f"URL {URL} is not valid"
        print(f"TC1 Passed: URL responded with status {response.status_code}")
    except Exception as e:
        pytest.fail(f"TC1 Failed: Exception occurred - {e}")


# TC2 - Check if the website title is correct
def test_tc2_page_title(driver):
    try:
        # Open the website
        driver.get(URL)

        # Assert that the page title matches the expected title
        assert driver.title == EXPECTED_TITLE, f"Title mismatch! Expected '{EXPECTED_TITLE}', but got '{driver.title}'"
        print("TC2 Passed: Page title is correct")
    except Exception as e:
        pytest.fail(f"TC2 Failed: Exception occurred - {e}")


# TC3 - Check if the login button is visible and clickable
def test_tc3_login_button_visible_clickable(driver):
    try:
        # Navigate directly to sign-in page
        driver.get(URL + "/sign-in/")

        # Wait for login button to be visible
        login_visible = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "login-btn"))
        )
        assert login_visible.is_displayed(), "Login button is not visible"

        # Wait for login button to be clickable
        login_clickable = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "login-btn"))
        )
        assert login_clickable is not None, "Login button is not clickable"
        print("TC3 Passed: Login button is visible and clickable")
    except Exception as e:
        pytest.fail(f"TC3 Failed: Exception occurred - {e}")


# TC4 - Check if the Sign Up button is visible and clickable
def test_tc4_signup_button_visible_clickable(driver):
    try:
        # Open the homepage
        driver.get(URL)

        # Wait for the Sign Up button to be visible
        sign_up_visible = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
                                              "//a[@class='⭐️rawbli-0 bg-green-500 hover:bg-green-600 text-white font-normal py-2 px-4 rounded text-base min-h-8 h-8 align-middle mr-2']"))
        )
        assert sign_up_visible.is_displayed(), "Sign Up button is not visible"

        # Wait for the Sign Up button to be clickable
        sign_up_clickable = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "//a[@class='⭐️rawbli-0 bg-green-500 hover:bg-green-600 text-white font-normal py-2 px-4 rounded text-base min-h-8 h-8 align-middle mr-2']"))
        )
        assert sign_up_clickable is not None, "Sign Up button is not clickable"
        print("TC4 Passed: Sign Up button is visible and clickable")
    except Exception as e:
        pytest.fail(f"TC4 Failed: Exception occurred - {e}")


# TC5 - Check if the Sign In page exists by getting status code
def test_tc5_page_exists(driver):
    try:
        # Navigate to the sign-in page
        driver.get(URL + "/sign-in/")

        # Capture the current URL loaded
        current_url = driver.current_url

        # Send a GET request to check page availability
        response = requests.get(current_url)

        # Assert that the page returned status code 200
        assert response.status_code == 200, f"Webpage at {current_url} did not load properly"
        print("TC5 Passed: Sign-in page exists and loads successfully")
    except Exception as e:
        pytest.fail(f"TC5 Failed: Exception occurred - {e}")
