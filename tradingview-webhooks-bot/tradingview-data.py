from selenium import webdriver
from bs4 import BeautifulSoup

#options = webdriver.FirefoxOptions()
#options.headless = True
#driver = webdriver.Firefox(options=options)
#driver.get('https://www.newegg.com')
#print(BeautifulSoup(driver.page_source, 'html.parser').prettify())
#driver.close()

def WebDriver():
    options = webdriver.FirefoxOptions()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    return driver