from pages.Login_page import Login_page
from pages.Register_page import Register_page
from pages.Home_page import Home_page
from utils.utils import Utils

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys


# register an account and return the email registered

def register_test(driver):
    Home = Home_page(driver)
    Login = Login_page(driver)
    Register = Register_page(driver)

    # go to sign in page and  make new acc
    login_btn = Home.get_login_button()
    shop_row = Home.get_shop_row()
    login_btn.click()

    WebDriverWait(driver, 30).until(expected_conditions.staleness_of(shop_row))

    register_form = Login.get_register_form()
    register_email = Login.get_register_email()

    user_email = Utils.gen_email()
    register_email.clear()
    register_email.send_keys(user_email)
    register_form.submit()


    # register new acc
    mr = Register.get_mr()
    first_name = Register.get_first_name()
    last_name = Register.get_last_name()
    password = Register.get_password()
    addesss = Register.get_addesss()
    city = Register.get_city()
    state = Register.get_state()
    zip_code = Register.get_zip_code()
    phone = Register.get_phone()

    mr.click()
    first_name.send_keys("Bruce")
    last_name.send_keys("Wayne")
    password.send_keys("12345")
    addesss.send_keys("Wayne Manor")
    city.send_keys("Gotham City")
    state.select_by_value("30")
    zip_code.send_keys("08701")
    phone.send_keys("12345678901")
    # driver.get("http://automationpractice.com/index.php?controller=my-account")
    register_btn = Register.get_register_btn()
    register_btn.click()

    sign_out_btn = Home.get_sign_out_btn()
    sign_out_btn.click()

    return user_email