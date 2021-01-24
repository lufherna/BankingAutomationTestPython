import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# this class will test the main page login ONLY
class mainLoginPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("./chromedriver")
        self.driver.maximize_window()
        # accesses test website
        self.driver.get("https://parabank.parasoft.com/parabank/index.htm")

    def testLoginInputs(self):
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

    # def tearDown(self):
    #     self.driver.quit()

# runs the suite of tests mentioned above
if __name__ == '__main__':
    unittest.main()


