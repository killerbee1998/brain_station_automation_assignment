from utils.utils import Utils
from selenium.webdriver.common.by import By 

class Login_page:

    def __init__(self, driver):
        self.driver = driver
        self.register_email = "/html/body/div/div[2]/div/div[3]/div/div/div[1]/form/div/div[2]/input"
        self.register_alert = "/html/body/div/div[2]/div/div[3]/div/div/div[1]/form/div/div[1]"
        self.register_form = "/html/body/div/div[2]/div/div[3]/div/div/div[1]/form"
        self.login_form = "/html/body/div/div[2]/div/div[3]/div/div/div[2]/form"
        self.login_email = "/html/body/div/div[2]/div/div[3]/div/div/div[2]/form/div/div[1]/input"
        self.login_pass = "/html/body/div/div[2]/div/div[3]/div/div/div[2]/form/div/div[2]/span/input"
        self.login_btn = "/html/body/div/div[2]/div/div[3]/div/div/div[2]/form/div/p[2]/button/span"
    
    def get_register_email(self):
        return Utils.wait_for_presence(self.driver, self.register_email, 30)

    def get_register_form(self):
        return Utils.wait_for_presence(self.driver, self.register_form, 30)
    
    def get_login_form(self):
        return Utils.wait_for_presence(self.driver, self.login_form, 30)
    
    def get_login_email(self):
        return Utils.wait_for_presence(self.driver, self.login_email, 30)
    
    def get_login_pass(self):
        return Utils.wait_for_presence(self.driver, self.login_pass, 30)
    
    def get_login_btn(self):
        return Utils.wait_to_be_clickable(self.driver, self.login_btn,30)