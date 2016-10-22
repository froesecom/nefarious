from selenium import webdriver
import time
import yaml

print "just imported selenium"
stream   = file("config/settings.yml", "r")
settings = yaml.load(stream)

baseurl = settings["baseurl"]
el_id = settings["input"]["id"]
#driver = webdriver.Chrome("/Library/drivers/chromedriver")
#driver.get(baseurl)
#el = driver.find_element_by_id(el_id)
#print el.get_attribute("name")
