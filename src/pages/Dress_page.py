from utils.utils import Utils
from selenium.webdriver.common.by import By

class Dress_page:

    def __init__(self,driver):
        self.driver = driver
        self.single_dress = "/html/body/div/div[2]/div/div[3]/div[2]/ul/li"
        self.add_to_cart_btn = "/html/body/div/div[2]/div/div[3]/div[2]/ul/li/div/div[2]/div[2]/a[1]"
        self.continue_shopping_btn = "/html/body/div/div[1]/header/div[3]/div/div/div[4]/div[1]/div[2]/div[4]/span/span"
        self.tshirt = "/html/body/div/div[1]/header/div[3]/div/div/div[6]/ul/li[3]/a"
    
    def get_single_dress(self):
        return Utils.wait_for_presence(self.driver, self.single_dress,30)
    
    def get_add_to_cart_btn(self):
        return Utils.wait_for_presence(self.driver, self.add_to_cart_btn,30)
    
    def get_continue_shopping_btn(self):
        return Utils.wait_to_be_clickable(self.driver, self.continue_shopping_btn,30)
    
    def get_tshirt(self):
        return Utils.wait_to_be_clickable(self.driver, self.tshirt,30)