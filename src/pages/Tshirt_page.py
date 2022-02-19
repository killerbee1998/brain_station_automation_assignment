from utils.utils import Utils
from selenium.webdriver.common.by import By

class Tshirt_page:

    def __init__(self,driver):
        self.driver = driver
        self.blue = "/html/body/div/div[2]/div/div[3]/div[1]/div[1]/div[1]/form/div/div[2]/ul/li[2]/label/a"
        self.single_shirt = "/html/body/div/div[2]/div/div[3]/div[2]/ul/li"
        self.add_to_cart_btn = "/html/body/div/div[2]/div/div[3]/div[2]/ul/li/div/div[2]/div[2]/a[1]/span"
        self.continue_shopping_btn = "/html/body/div/div[1]/header/div[3]/div/div/div[4]/div[1]/div[1]/span"
        self.cart = "/html/body/div/div[1]/header/div[3]/div/div/div[3]/div/a"
        self.checkout = "/html/body"

    
    def get_blue(self):
        return Utils.wait_for_presence(self.driver, self.blue,30)

    def get_single_shirt(self):
        return Utils.wait_for_presence(self.driver, self.single_shirt,30)
    
    def get_add_to_cart_btn(self):
        return Utils.wait_for_presence(self.driver, self.add_to_cart_btn,30)
    
    def get_continue_shopping_btn(self):
        return Utils.wait_to_be_clickable(self.driver, self.continue_shopping_btn,30)
    
    def get_cart(self):
        return Utils.wait_to_be_clickable(self.driver, self.cart, 30)

    def get_checkout(self):
        return Utils.wait_for_presence(self.driver, self.checkout,30)