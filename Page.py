# this will be used to give the other pages
# base drivers and necessary info
# we're going to define a class for each page we're going to test
from locator import *


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    def is_title_matches(self):
        return "Python" in self.driver.title

    def click_go_button(self):
        # by putting the asterisk it separates it into two entities
        # it's called splat or unpack
        userNameInput = self.driver.find_element(*MainPageLocators.USERNAME_INPUT)
        userNameInput.click()


class SearchResultPage(BasePage):

    def is_results_found(self):
        return "No results found!" not in self.driver.page_source
