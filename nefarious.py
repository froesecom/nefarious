from selenium import webdriver
import time
import yaml
import csv

print "just imported selenium"
stream   = file("config/settings.yml", "r")
settings = yaml.load(stream)

baseurl = settings["baseurl"]
el_id = settings["input"]["id"]

with open("config/input_data.csv", "rU") as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    print(row["ABN"]) #row header is ABN in this case

#driver = webdriver.Chrome("/Library/drivers/chromedriver")

#driver.get(baseurl)
#el = driver.find_element_by_id(el_id)
#print el.get_attribute("name")
