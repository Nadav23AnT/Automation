from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

url = "https://www.google.com/intl/iw/earth/"
driver = webdriver.Chrome(r'E:\Selenium\chromedriver.exe')
driver.get(url)
wait = WebDriverWait(driver, 10)
launch_earth = wait.until(ec.element_to_be_clickable(By.XPATH, '/html/body/header/div/nav[1]/ul[2]/li[2]/a/span/span'))
launch_earth.click()
