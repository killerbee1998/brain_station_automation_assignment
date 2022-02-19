from pages.Login_page import Login_page
from pages.Home_page import Home_page
from utils.utils import Utils

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


# log into account
def login_test(driver, user_email):
    Home = Home_page(driver)
    Login = Login_page(driver)

    # go to sign in page
    login_btn = Home.get_login_button()
    login_btn.click()

    login_form = Login.get_login_form()
    login_email = Login.get_login_email()
    login_pass = Login.get_login_pass()

    login_email.clear()
    login_pass.clear()

    login_email.send_keys(user_email)
    login_pass.send_keys(12345)

    login_btn = Login.get_login_btn()
    login_btn.click()