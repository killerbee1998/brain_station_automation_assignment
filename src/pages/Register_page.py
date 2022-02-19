from utils.utils import Utils
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class Register_page:

    def __init__(self, driver):
        self.driver = driver
        self.mr = "/html/body/div/div[2]/div/div[3]/div/div/form/div[1]/div[1]/div[1]/label/div"
        self.first_name = "/html/body/div/div[2]/div/div[3]/div/div/form/div[1]/div[2]/input"
        self.last_name = "/html/body/div/div[2]/div/div[3]/div/div/form/div[1]/div[3]/input"
        self.password = "/html/body/div/div[2]/div/div[3]/div/div/form/div[1]/div[5]/input"
        self.address = "/html/body/div/div[2]/div/div[3]/div/div/form/div[2]/p[4]/input"
        self.city = "/html/body/div/div[2]/div/div[3]/div/div/form/div[2]/p[6]/input"
        self.state = "/html/body/div/div[2]/div/div[3]/div/div/form/div[2]/p[7]/div/select"
        self.zip_code = "/html/body/div/div[2]/div/div[3]/div/div/form/div[2]/p[8]/input"
        self.phone = "/html/body/div/div[2]/div/div[3]/div/div/form/div[2]/p[13]/input"
        self.register_form = "/html/body/div/div[2]/div/div[3]/div/div/form"
        self.register_btn = "/html/body/div/div[2]/div/div[3]/div/div/form/div[4]/button/span"
        
    

    def get_mr(self):
        return Utils.wait_to_be_clickable(self.driver, self.mr, 30)
    
    def get_first_name(self):
        return Utils.wait_for_presence(self.driver, self.first_name, 30)
    
    def get_last_name(self):
        return Utils.wait_for_presence(self.driver, self.last_name, 30)
    
    def get_password(self):
        return Utils.wait_for_presence(self.driver, self.password, 30)
    
    def get_addesss(self):
        return Utils.wait_for_presence(self.driver, self.address, 30)
    
    def get_city(self):
        return Utils.wait_for_presence(self.driver, self.city, 30)

    def get_state(self):
        return Select(Utils.wait_for_presence(self.driver, self.state, 30))
    
    def get_zip_code(self):
        return Utils.wait_for_presence(self.driver, self.zip_code, 30)
    
    def get_phone(self):
        return Utils.wait_for_presence(self.driver, self.phone, 30)

    def get_register_btn(self):
        return Utils.wait_to_be_clickable(self.driver, self.register_btn, 30)
    
    def get_register_form(self):
        return Utils.wait_for_presence(self.driver, self.phone, 30)