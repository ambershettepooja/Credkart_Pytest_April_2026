import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class Read_Config_Class:

    @staticmethod
    def get_data_for_email():
        email = config.get("login data", "email")
        return email

    @staticmethod
    def get_data_for_password():
        password = config.get("login data", "password")
        return password

    @staticmethod
    def get_data_for_home_page():
        home_page = config.get("app url", "home_page")
        return home_page


    @staticmethod
    def get_data_for_login_page():
        login_page = config.get("app url", "login_page")
        return login_page

    @staticmethod
    def get_data_for_registration_page():
        registration_page = config.get("app url", "registration_page")
        return registration_page
