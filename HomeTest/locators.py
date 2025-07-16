from selenium.webdriver.common.by import By

USERNAME_INPUT = (By.NAME, "user-name")
PASSWORD_INPUT = (By.NAME, "password")
LOGIN_BUTTON = (By.NAME, "login-button")

INVENTORY_LIST = (By.CLASS_NAME, "inventory_list")
INVENTORY_ITEM = (By.CLASS_NAME, "inventory_item")

All_DESCENDANTS = (By.XPATH, ".//*")
ACTUAL_CART_COUNT = (By.CLASS_NAME, "shopping_cart_badge")

