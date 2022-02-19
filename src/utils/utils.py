from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import random
import string

class Utils:

    def wait_to_be_clickable(driver, selector, waitInterval):
        wait_element = WebDriverWait(driver, waitInterval).until(expected_conditions.element_to_be_clickable((By.XPATH,selector)))
        return wait_element
    
    def wait_for_presence(driver, selector, waitInterval):
        wait_element = WebDriverWait(driver, waitInterval).until(expected_conditions.presence_of_element_located((By.XPATH, selector)))
        return wait_element
    
    def gen_email():
        def random_char(char_num):
            return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))

        return random_char(7)+"@gmail.com"