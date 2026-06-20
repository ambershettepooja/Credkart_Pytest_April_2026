import pytest

from PageObjects.Login_Page import Login_Page_Class
from utilities.Excel_Utilities import Excel_utils_class
from utilities.readConfig import Read_Config_Class


@pytest.mark.usefixtures("browser_setup")
class Test_Login_Excel_002:
    driver = None
    login_url = Read_Config_Class.get_data_for_login_page()
    excel_file_path = ".\\TestData\\Test_Data.xlsx"
    sheet_name = "login_data"

    def test_login_excel_006(self):

        self.max_rows = Excel_utils_class.get_max_row_of_excel(self.excel_file_path, self.sheet_name)
        result_status = []
        for i in range(2, self.max_rows+1):
            self.email = Excel_utils_class.read_data_from_excel(self.excel_file_path, self.sheet_name, i, 2)
            self.password = Excel_utils_class.read_data_from_excel(self.excel_file_path, self.sheet_name, i, 3)
            self.expected_result = Excel_utils_class.read_data_from_excel(self.excel_file_path, self.sheet_name, i, 4)
            self.lpo = Login_Page_Class(self.driver)
            self.driver.get(self.login_url)
            self.lpo.enter_email(self.email)
            self.lpo.enter_password(self.password)
            self.lpo.click_submit_button()
            if self.lpo.verify_menu() == "pass":
                self.lpo.click_menu_link()
                self.lpo.click_logout_link()
                actual_result = "login_pass"
            else:
                actual_result = "login_fail"

            Excel_utils_class.write_data_to_excel(self.excel_file_path, self.sheet_name, i, 5, actual_result)

            if actual_result == self.expected_result:
                test_status= "Test_Pass"
            else:
                test_status = "Test_Fail"
            Excel_utils_class.write_data_to_excel(self.excel_file_path, self.sheet_name, i, 6, test_status)

            result_status.append(test_status)

        if "Test_Fail" not in result_status:
            assert True
        else:
            assert False