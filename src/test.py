from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from utils.utils import Utils
from pages.Home_page import Home_page
from pages.Dress_page import Dress_page
from pages.Tshirt_page import Tshirt_page
from pages.Orders_page import Orders_page
from pages.Tshirt_cart import Tshirt_cart

from tests.register_test import register_test
from tests.login_test import login_test
from tests.shopping_test import shoping_test


ser = Service("src\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)
driver.get('http://automationpractice.com/index.php')


Home = Home_page(driver)
Dress = Dress_page(driver)
Tshirt = Tshirt_page(driver)
Tcart = Tshirt_cart(driver)
Orders = Orders_page(driver)

# register 2 people
email_1 = register_test(driver)
email_2 = register_test(driver)

# login 1st person
login_test(driver, email_1)

# shopping test(buy a casual dress and a t shirt)
shoping_test(driver)

# login 2nd person
login_test(driver, email_2)

# shopping test(buy a casual dress and a t shirt)
shoping_test(driver)