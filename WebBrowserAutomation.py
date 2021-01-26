import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# this class will test the main page login ONLY
class TestMainLoginPage(unittest.TestCase):

    # def __init__(self, driver):
    #     self.driver = webdriver.Chrome("./chromedriver")
    #     self.driver.maximize_window()
    #     self.driver.implicitly_wait(10)
        # accesses test website

    # setup method always runs first and is specific to the .TestCase with Python
    # kinda like the __init__ method
    # for each test case setup is run once
    # the same with teardown
    def setUp(self):
        self.driver = webdriver.Chrome("./chromedriver")
        self.driver.maximize_window()
        # accesses test website
        self.driver.get("https://parabank.parasoft.com/parabank/index.htm")

    # automatically runs since it starts with 'test'
    def testLoginPage(self):
        # get to the login page
        self.driver.get("https://parabank.parasoft.com/parabank/index.htm")
        # grab username input
        usernameInput = self.driver.find_element_by_name('username')
        # entering a username to login
        usernameInput.send_keys('john')
        # grab password input
        passwordInput = self.driver.find_element_by_name('password')
        # entering a password to login
        passwordInput.send_keys('demo')
        # clicking on 'Login'
        loginButton = self.driver.find_element_by_xpath("//input[@value='Log In']")
        loginButton.click()
        # assert makes sure that the test case ran successfully
        assert True

    # if you create a method that doesn't start with 'test' it will NOT run automatically
    # will this upload to github?

    # this runs at the end to close everything down
    # def tearDown(self):
    #     self.driver.close()


# second class will test new page along with its functionality
class TestAccountServicesPage(unittest.TestCase):

    def testConfirmCorrectPage(self):
        chromeDriver = self.driver
        # just trying to confirm that the title page is accurate
        self.assertEqual("ParaBank | Accounts Overview", chromeDriver.title)


# runs the suite of tests mentioned above
if __name__ == '__main__':
    unittest.main()
