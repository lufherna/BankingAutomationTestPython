from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chromeDriver = webdriver.Chrome("/chromedriver")

# accesses test website
chromeDriver.get("https://parabank.parasoft.com/parabank/index.htm")
print(chromeDriver.title)

