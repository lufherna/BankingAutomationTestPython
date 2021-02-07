from selenium.webdriver.support.ui import WebDriverWait


# for any element we want to set the value of we follow the
# following procedure
class BasePageElement(object):
    locator = "q"

    def __set__(self, obj, value):
        driver = obj.driver
        #
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_name(self.locator))
        driver.find_element_by_name(self.locator).clear()
        driver.find_element_by_name(self.locator).send_keys(value)

    def __get__(self):