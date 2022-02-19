from utils.utils import Utils
from selenium.webdriver.common.by import By

class Tshirt_cart:

    def __init__(self, driver):
        self.driver = driver
        self.add_to_cart_btn = "//span[text()=\"Add to cart\"]"
        self.cart = "/html/body/div/div[1]/header/div[3]/div/div/div[3]/div/a"
        self.continue_shopping_btn = "/html/body/div/div[1]/header/div[3]/div/div/div[4]/div[1]/div[1]/span"
    
    def get_add_to_cart_btn(self):
        print("add")
        Utils.wait_to_be_clickable(self.driver, self.add_to_cart_btn, 30)
    
    def get_continue_shopping_btn(self):
        return Utils.wait_to_be_clickable(self.driver, self.continue_shopping_btn, 30)
        
    def get_cart(self):
        return Utils.wait_to_be_clickable(self.driver, self.cart, 30)