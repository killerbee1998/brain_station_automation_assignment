from utils.utils import Utils
from selenium.webdriver.common.by import By 

class Home_page:

    def __init__(self, driver):
        self.driver = driver
        self.login_button = "/html/body/div/div[1]/header/div[2]/div/div/nav/div[1]/a"
        self.dresses = "/html/body/div/div[1]/header/div[3]/div/div/div[6]/ul/li[2]/a"
        self.casual = "/html/body/div/div[1]/header/div[3]/div/div/div[6]/ul/li[2]/ul/li[1]/a"
        self.tshirt = "/html/body/div/div[1]/header/div[3]/div/div/div[6]/ul/li[3]/a"
        self.shop_row = "/html/body/div/div[2]/div/div[2]/div"
        self.sign_out_btn = "/html/body/div/div[1]/header/div[2]/div/div/nav/div[2]/a"
    
    def get_login_button(self):
        return Utils.wait_to_be_clickable(self.driver,self.login_button,30)
    
    def get_dresses(self):
        return Utils.wait_for_presence(self.driver,self.dresses,30)
    
    def get_casual(self):
        return Utils.wait_for_presence(self.driver,self.casual,30)
    
    def get_tshirt(self):
        return Utils.wait_for_presence(self.driver,self.tshirt,30)
    
    def get_shop_row(self):
        return Utils.wait_for_presence(self.driver,self.shop_row,30)
    
    def get_sign_out_btn(self):
        return Utils.wait_to_be_clickable(self.driver, self.sign_out_btn, 30)
