from selenium import webdriver
from selenium.webdriver import Chrome


driver = webdriver.Chrome(executable_path="lib\chromedriver.exe")
browser = "chrome"


def open_website(url):
    """
    docstring
    """
    driver.get(url)
    pass
