import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chromeDriver = webdriver.Chrome("./chromedriver")


# this class will test the main page login ONLY
class mainLoginPageTest(unittest.TestCase):

    def enterCorrectUNandPW(self):
        # accesses test website
        chromeDriver.get("https://parabank.parasoft.com/parabank/index.htm")
        # grab username input
        usernameInput = chromeDriver.find_element_by_name('username')
        # entering a username to login
        usernameInput.send_keys('john')

        # grab password input
        passwordInput = chromeDriver.find_element_by_name('password')
        # entering a password to login
        passwordInput.send_keys('demo')
        # clicking on 'Login'
        loginButton = chromeDriver.find_element_by_xpath("//input[@value='Log In']")
        loginButton.click()

    # closes the browser window
    chromeDriver.close()