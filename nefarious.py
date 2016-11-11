from selenium import webdriver
import time
import yaml
import csv
import pdb

print "just imported selenium"
stream   = file("config/settings.yml", "r")
settings = yaml.load(stream)

baseurl = settings["baseurl"]
driver = webdriver.Chrome("/Library/drivers/chromedriver")

print "opening csv..."
with open("config/input_data_test.csv", "rU") as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    print(row["ABN"]) #row header is ABN in this case
     
    #pdb.set_trace()
    for instruction in settings['actions']:
      print("hello?")
      #if key == "input":
     #   el = driver.find_element_by_id() 
        

#driver.get(baseurl)
#el = driver.find_element_by_id(el_id)
#print   .get_attribute("name")
