from HomeTest.config import ADD_TO_CART
from HomeTest.locators import INVENTORY_LIST, INVENTORY_ITEM, All_DESCENDANTS, ACTUAL_CART_COUNT
from HomeTest.helpers.ui_helpers import wait_and_find_all_in_element, get_first_item_or_fail, wait_and_find_all_inside_element, \
    click_element_by_text, wait_and_get_text, parse_number


class StoreMainPage:
    def __init__(self, driver):
        self.driver = driver

    def get_all_items(self):
        return wait_and_find_all_in_element(self.driver, *INVENTORY_LIST, *INVENTORY_ITEM)

    def get_count_items(self):
        items = self.get_all_items()
        return len(items)

    def add_item_to_cart(self):
        items = self.get_all_items()
        first_item = get_first_item_or_fail(items)
        all_item_descendants = wait_and_find_all_inside_element(first_item, *All_DESCENDANTS)
        click_element_by_text(all_item_descendants, ADD_TO_CART)

    def get_cart_icon_number(self):
        cart_text_count = wait_and_get_text(self.driver, *ACTUAL_CART_COUNT)
        return parse_number(cart_text_count)
