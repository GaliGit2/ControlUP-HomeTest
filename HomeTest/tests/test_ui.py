from HomeTest.config import ITEMS_WRONG_COUNT_EXCEPTION, \
    EXPECTED_INVENTORY_ITEMS_COUNT, EXPECTED_CART_COUNT, CART_WRONG_COUNT_EXCEPTION


#UI Tests

#Scenario 1: Verify Inventory Items
def test_login_and_check_items(login_to_main_page):
    # login returns the StoreMainPage
    actual_inventory_items_count = login_to_main_page.get_count_items()
    assert actual_inventory_items_count == EXPECTED_INVENTORY_ITEMS_COUNT, (
        f"{ITEMS_WRONG_COUNT_EXCEPTION} - Expected: {EXPECTED_INVENTORY_ITEMS_COUNT}, Got: {actual_inventory_items_count}"
    )

#Scenario 2: Add Item to Cart
def test_add_to_cart_and_check_icon(login_to_main_page):
    # login returns the StoreMainPage
    login_to_main_page.add_item_to_cart()
    cart_actual_count = login_to_main_page.get_cart_icon_number()
    assert cart_actual_count == EXPECTED_CART_COUNT, (
        f"{CART_WRONG_COUNT_EXCEPTION} - Expected: {EXPECTED_CART_COUNT}, Got: {cart_actual_count}")