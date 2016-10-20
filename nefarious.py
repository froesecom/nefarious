
from selenium import webdriver
import time

print "just imported selenium"
baseurl = ""
el_id = ""
driver = webdriver.Chrome("/Library/drivers/chromedriver")
driver.get(baseurl)
el = driver.find_element_by_id(el_id)
print el.get_attribute("name")
