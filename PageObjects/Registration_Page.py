import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.Login_Page import Login_Page_Class


class Registration_Page_Class(Login_Page_Class):
    # activity
    text_name_id = "name"
    text_confirm_password_id = "password-confirm"

    def enter_name(self, name):
        time.sleep(2)
        name_text = self.driver.find_element(By.ID, self.text_name_id)
        name_text.send_keys(name)

    def enter_confirm_password(self, confirm_password):
        confirm_password_text = self.driver.find_element(By.ID, self.text_confirm_password_id)
        confirm_password_text.send_keys(confirm_password)


import PageObjects.Login_Page


class Registration_Page_Class(Login_Page_Class):
    # activity
    text_name_id = "name"
    text_confirm_password_id = "password-confirm"

    def enter_name(self, name):
        time.sleep(2)
        name_text = self.driver.find_element(By.ID, self.text_name_id)
        name_text.send_keys(name)

    def enter_confirm_password(self, confirm_password):
        confirm_password_text = self.driver.find_element(By.ID, self.text_confirm_password_id)
        confirm_password_text.send_keys(confirm_password)

