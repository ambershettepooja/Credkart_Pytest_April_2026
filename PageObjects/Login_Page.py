from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Login_Page_Class:
    # activity
    text_email_id = "email"
    text_password_id ="password"
    btn_login_class = "btn"
    click_menu_class = "dropdown-toggle"
    click_logout_link_partial_link_text = "Logout"


    def __init__(self, driver):
        self.driver = driver


# define drive : conftest
# use : testcase
# using driver method at page object also (not for setup and teardown)

    def enter_email(self, email):
        email_text = self.driver.find_element(By.ID, self.text_email_id)
        email_text.send_keys(email)


    def enter_password(self, password):
        password_text = self.driver.find_element(By.ID, self.text_password_id)
        password_text.send_keys(password)

    def click_submit_button(self):
        login_button = self.driver.find_element(By.CLASS_NAME, self.btn_login_class)
        login_button.click()

    def verify_menu(self):
        try:
            WebDriverWait(self.driver, 5).until(
                expected_conditions.visibility_of_element_located((By.CLASS_NAME, self.click_menu_class))
            )
            menu_link = self.driver.find_element(By.CLASS_NAME, self.click_menu_class)
            return "pass"
        except:
            return "fail"

    def click_menu_link(self):
        menu_link = self.driver.find_element(By.CLASS_NAME, self.click_menu_class)
        menu_link.click()

    def click_logout_link(self):
        logout_link = self.driver.find_element(By.PARTIAL_LINK_TEXT, self.click_logout_link_partial_link_text)
        logout_link.click()