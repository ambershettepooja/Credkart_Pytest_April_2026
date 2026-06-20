import allure
import pytest
from faker import Faker



from PageObjects.Login_Page import Login_Page_Class
from PageObjects.Registration_Page import Registration_Page_Class
from utilities.Logger_Utils import log_generator_class
from utilities.readConfig import Read_Config_Class


@pytest.mark.usefixtures("browser_setup")
class Test_User_Profile_Class :
    driver = None # initially Browser has value None
    email = Read_Config_Class.get_data_for_email()
    password = Read_Config_Class.get_data_for_password()
    login_url = Read_Config_Class.get_data_for_login_page()
    home_page_url = Read_Config_Class.get_data_for_home_page()
    registration_url = Read_Config_Class.get_data_for_registration_page()
    log = log_generator_class.loggen_method()

    # but when methods are going to run driver == browser_setup from conftest

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Verify Application Url")
    @allure.description("This test case is to validate credkart title functionality ")
    @allure.link(login_url)
    @allure.story("Story 1")
    @allure.epic("Epic 1")
    def test_verify_application_url_001(self):
        # self.log.debug(" This is debug")
        # self.log.info(" This is info")
        # self.log.warning(" This is warning")
        # self.log.error(" This is error")
        # self.log.critical(" This is critical")

        self.log.info("Testcase test_verify_application_url_001 is started")
        self.driver.get(self.home_page_url)
        self.log.info(f"Opening Browser and getting {self.home_page_url}")
        self.log.info(f"Checking Page title")
        if self.driver.title == "CredKart":
            self.log.info("test_verify_application_url_001 is pass")
        else:
            self.log.info("test_verify_application_url_001 is fail")
            assert False
        self.log.info("test_verify_application_url_001 is complete")

    def test_verify_application_url_002(self):
        self.driver.get(self.home_page_url)
        assert "CredKart" == self.driver.title, \
            f"Testcase fail : title not matching :  You are landed at {self.driver.title}"


    def test_verify_application_url_003(self):
        self.driver.get(self.home_page_url)
        try :
            assert self.driver.title == "CredKart", \
            f"Testcase fail : title not matching :  You are landed at {self.driver.title}"
        finally :
            print("test_verify_application_url_001 is complete")

    def test_credkart_user_login_004(self):
        self.driver.get(self.login_url)

        # # Enter Email
        # email_text_box = self.driver.find_element(By.XPATH, "//input[@id='email']")
        # email_text_box.send_keys("Credence1@may2026.in")

        self.lpo = Login_Page_Class(driver = self.driver)
        self.lpo.enter_email(self.email)

        # Enter Password
        # password_text_box = self.driver.find_element(By.XPATH, "//input[@id='password']")
        # password_text_box.send_keys("Credence1@may2026.in")

        self.lpo.enter_password(self.password)

        # Click on login Button
        # login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        # login_button.click()

        self.lpo.click_submit_button()


        # Verify User login
        # try:
        #     WebDriverWait(self.driver, 5).until(
        #         expected_conditions.visibility_of_element_located((By.XPATH, "//a[@role='button']"))
        #     )
        #     login_name = self.driver.find_element(By.XPATH, "//a[@role='button']")
        #     self.driver.save_screenshot(
        #         f".\\Screenshots\\User login for {login_name.text} user is successfully.png"
        #         )
        #     print(f"User login for '{login_name.text}' user is successfully.")
        # except:
        #     self.driver.save_screenshot(
        #         f".\\Screenshots\\User login is failed.png"
        #         )
        #     print(f"User login is failed.")
        #     assert False

        if self.lpo.verify_menu() == "pass":
            self.driver.save_screenshot(f".\\Screenshots\\User login for user is successfully.png")
            print(f"User login for user is successfully.")
        else:
            self.driver.save_screenshot(
                f".\\Screenshots\\User login is failed.png"
                )
            print(f"User login is failed.")
            assert False





    def test_credkart_user_registration_005(self):
        self.driver.get(self.registration_url)
        name_data = Faker().user_name()
        email_data = Faker().email()
        self.rpo = Registration_Page_Class(self.driver)
        # Enter Name
        self.rpo.enter_name(name_data)
        # Enter Email
        self.rpo.enter_email(email_data)
        # Enter Password
        self.rpo.enter_password(self.password)
        # Enter Confirm Password
        self.rpo.enter_confirm_password(self.password)
        # Click on Register Button
        self.rpo.click_submit_button()
        # Verify User Registration
        if self.rpo.verify_menu() == "pass":
            self.driver.save_screenshot(f".\\Screenshots\\User registration for user {name_data} is successfully.png")
            print(f"User registration for user is successfully.")
        else:
            self.driver.save_screenshot(
                f".\\Screenshots\\User registration is failed.png"
                )
            print(f"User registration is failed.")
            assert False





# pytest -v -s -n=4 --html=HTML_Reports/My_report.html --browser headless

# 3 hr : credkart git jenkins

# plan 1 sunday: credkart git jenkins

# plan 2 monday to wednesday : credkart git jenkins / 2 project orange hrm
