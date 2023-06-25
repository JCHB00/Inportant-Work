#Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Firefox()
browser.get("https://tophub.today/")
elem = browser.find_element(By.XPATH, '/html/body/div[1]/div[4]/div[3]/div[4]/div[2]/div/div[2]/div[1]/a[1]/div/span[2]')
print(elem.text)
browser.quit()
