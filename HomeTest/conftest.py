import pytest
from selenium import webdriver

from HomeTest.config import UI_BASE_URL
from HomeTest.pages.LoginPage import LoginPage
from HomeTest.pages.StoreMainPage import StoreMainPage


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--incognito")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-notifications")
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    driver.get(UI_BASE_URL)
    yield driver
    driver.quit()

@pytest.fixture
def login_to_main_page(driver):
    login_page = LoginPage(driver)
    login_page.login()
    return StoreMainPage(driver)