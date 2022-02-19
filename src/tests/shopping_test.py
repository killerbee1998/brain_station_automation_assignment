from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from utils.utils import Utils
from pages.Home_page import Home_page
from pages.Dress_page import Dress_page
from pages.Tshirt_page import Tshirt_page
from pages.Orders_page import Orders_page
from pages.Tshirt_cart import Tshirt_cart

def shoping_test(driver):

    Home = Home_page(driver)
    Dress = Dress_page(driver)
    Tshirt = Tshirt_page(driver)
    Tcart = Tshirt_cart(driver)
    Orders = Orders_page(driver)

    # go to dress page
    casual = Home.get_casual()
    dresses = Home.get_dresses()

    ActionChains(driver).move_to_element(dresses).perform()
    casual.click()

    WebDriverWait(driver, 30).until(expected_conditions.staleness_of(dresses))

    # add a dress to cart and then go to tshirts
    single_dress = Dress.get_single_dress()
    add_to_cart_btn = Dress.get_add_to_cart_btn()

    ActionChains(driver).move_to_element(single_dress).perform()
    add_to_cart_btn.click()

    continue_shopping_btn = Dress.get_continue_shopping_btn()
    tshirt = Dress.get_tshirt()

    continue_shopping_btn.click()
    tshirt.click()

    WebDriverWait(driver, 30).until(expected_conditions.staleness_of(single_dress))

    # filter by blue color and buy shirt
    blue = Tshirt.get_blue()

    single_tshirt = Tshirt.get_single_shirt()
    add_to_cart_btn = Tshirt.get_add_to_cart_btn()

    blue.click()
    ActionChains(driver).move_to_element(single_tshirt).perform()
    add_to_cart_btn.click()

    cart = Tshirt.get_cart()
    cart.click()

    driver.get("http://automationpractice.com/index.php?controller=order&step=1")
    
    # go to checkout and pay using cheque
    checkout_btn = Orders.get_checkout_btn()
    checkout_btn.click()

    agree_box = Orders.get_agree_box()
    agree_box.click()

    checkout_btn_2 = Orders.get_second_checkout_btn()
    checkout_btn_2.click()

    driver.get("http://automationpractice.com/index.php?fc=module&module=cheque&controller=payment")

    #sign out 
    sign_out_btn = Home.get_sign_out_btn()
    sign_out_btn.click()
