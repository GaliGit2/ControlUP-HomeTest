from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from HomeTest.config import DEFAULT_TIMEOUT, ELEMENTS_NOT_FOUND_EXCEPTION, ITEMS_NOT_FOUND_EXCEPTION, \
    NOT_A_NUMBER_EXCEPTION


def wait_and_click(driver, by, locator, timeout=DEFAULT_TIMEOUT):
    WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((by, locator))
    ).click()

def wait_and_send_keys(driver, by, locator, text, timeout=DEFAULT_TIMEOUT):
    WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located((by, locator))
    ).send_keys(text)

def wait_and_find_all_inside_element(parent_element, by, locator, timeout=DEFAULT_TIMEOUT):
    WebDriverWait(parent_element, timeout).until(
        lambda el: parent_element.find_elements(by, locator)
    )
    elements = parent_element.find_elements(by, locator)
    if not elements:
        raise Exception(f"{ELEMENTS_NOT_FOUND_EXCEPTION}: ({by}, '{locator}')")
    return elements

def click_element_by_text(elements, expected_text):
    expected_text = expected_text.lower()
    for el in elements:
        if expected_text == el.text.lower():
            el.click()
            return
    raise Exception(f"{ELEMENTS_NOT_FOUND_EXCEPTION}: {expected_text}")

def wait_and_get_text(driver, by, locator, timeout=DEFAULT_TIMEOUT):
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located((by, locator))
    ).text

def wait_and_find_all_in_element(driver, parent_by, parent_locator, child_by, child_locator, timeout=DEFAULT_TIMEOUT):
    parent = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((parent_by, parent_locator))
    )
    return parent.find_elements(child_by, child_locator)

def get_first_item_or_fail(items):
    first_item = next(iter(items), None)
    assert first_item is not None, ITEMS_NOT_FOUND_EXCEPTION
    return first_item

def parse_number(input_str: str) -> int:
    try:
        return int(input_str)
    except ValueError:
        raise ValueError(f"{NOT_A_NUMBER_EXCEPTION}: '{input_str}'")