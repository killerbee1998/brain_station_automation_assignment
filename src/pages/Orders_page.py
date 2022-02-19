from utils.utils import Utils
from selenium.webdriver.common.by import By

class Orders_page:

    def __init__(self,driver):
        self.driver = driver
        self.checkout_btn = "/html/body/div/div[2]/div/div[3]/div/form/p/button"
        self.agree_box = "/html/body/div/div[2]/div/div[3]/div/div/form/div/p[2]/div"
        self.second_checkout_btn = "/html/body/div/div[2]/div/div[3]/div/div/form/p/button/span"
        self.pay_by_check_btn = "/html/body/div/div[2]/div/div[3]/div/div/div[3]/div[2]/div/p/a"
    
    def get_checkout_btn(self):
        return Utils.wait_to_be_clickable(self.driver, self.checkout_btn, 30)
    
    def get_agree_box(self):
        return Utils.wait_to_be_clickable(self.driver, self.agree_box, 30)
    
    def get_second_checkout_btn(self):
        return Utils.wait_for_presence(self.driver,self.second_checkout_btn, 30)
    
    def pay_by_check_btn(self):
        return Utils.wait_to_be_clickable(self.driver, self.pay_by_check_btn, 30)