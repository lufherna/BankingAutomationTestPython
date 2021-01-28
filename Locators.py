from selenium.webdriver.common.by import By


# create a class that defines all the inputs and buttons
# from the main page
class MainPageLocators(object):
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")


class SearchResultsPageLocators(object):
    pass
