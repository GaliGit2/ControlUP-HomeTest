import pytest
from selenium import webdriver

from HomeTest.locators import USERNAME_INPUT, PASSWORD_INPUT, LOGIN_BUTTON, \
    All_DESCENDANTS, ACTUAL_CART_COUNT
from config import USERNAME, PASSWORD, EXPECTED_INVENTORY_ITEMS_COUNT, ITEMS_WRONG_COUNT_EXCEPTION, \
    EXPECTED_CART_COUNT, ADD_TO_CART, CART_WRONG_COUNT_EXCEPTION, UI_BASE_URL
from ui_helpers import *

#UI Tests

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
    wait_and_send_keys(driver, *USERNAME_INPUT, USERNAME)
    wait_and_send_keys(driver, *PASSWORD_INPUT, PASSWORD)
    wait_and_click(driver, *LOGIN_BUTTON)

    yield driver
    driver.quit()

#Scenario 1: Verify Inventory Items
def test_login_and_check_items(driver):
    items = get_all_items(driver)
    actual_inventory_items_count = len(items)
    assert actual_inventory_items_count == EXPECTED_INVENTORY_ITEMS_COUNT, (
        f"{ITEMS_WRONG_COUNT_EXCEPTION} - Expected: {EXPECTED_INVENTORY_ITEMS_COUNT}, Got: {actual_inventory_items_count}"
    )

#Scenario 2: Add Item to Cart
def test_add_to_cart_and_check_icon(driver):
    items = get_all_items(driver)
    first_item = get_first_item_or_fail(items)
    all_item_descendants = wait_and_find_all_inside_element(first_item, *All_DESCENDANTS)
    click_element_by_text(all_item_descendants, ADD_TO_CART)
    cart_text_count = wait_and_get_text(driver, *ACTUAL_CART_COUNT)
    cart_actual_count = parse_number(cart_text_count)
    assert cart_actual_count == EXPECTED_CART_COUNT, (
        f"{CART_WRONG_COUNT_EXCEPTION} - Expected: {EXPECTED_CART_COUNT}, Got: {cart_actual_count}")