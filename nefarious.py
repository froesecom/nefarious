
from selenium import webdriver
import time

print "just imported selenium"
baseurl = ""
el_id = ""
mydriver = webdriver.Chrome()
mydriver.get(baseurl)
el = mydriver.get_element_by_id(el_id)
print el
