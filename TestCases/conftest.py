import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
service = Service(ChromeDriverManager().install())



def pytest_addoption(parser):
    parser.addoption("--browser")
# Here, we are going to add "--browser" command line argument which user define Or custom argument .

# --browser chrome
# --browser firefox


@pytest.fixture(scope ="class")
def browser_setup(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        print("Launching chrome browser")
        driver = webdriver.Chrome(service=service)
    elif browser == "firefox":
        print("Launching firefox browser")
        driver = webdriver.Firefox()
    elif browser == "edge":
        print("Launching edge browser")
        driver = webdriver.Edge()
    elif browser == "headless":
        print("Launching headless chrome browser")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options = chrome_options)
    else:
        print("Launching chrome browser")
        driver =  webdriver.Chrome()
    driver.maximize_window()
    request.cls.driver = driver # attaching driver to class
    driver.implicitly_wait(2)
    yield driver
    driver.quit()

