from selenium import webdriver
import selenium.webdriver.support.ui as ui
import time
import yaml
import csv
import pdb

print "just imported selenium"
stream   = file("config/settings.yml", "r")
settings = yaml.load(stream)

baseurl = settings["baseurl"]
driver = webdriver.Chrome("/Library/drivers/chromedriver")
wait = ui.WebDriverWait(driver,10)
driver.get(baseurl)

print "opening csv..."
with open("config/input_data_test.csv", "rU") as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    print(row["ABN"]) #row header is ABN in this case
     
    #pdb.set_trace()
    for instruction in settings['actions']:
      for key, value in instruction.items():
        print(driver.title)
        if key == "input":
          el = driver.find_element_by_id(value["id"])
          el.send_keys(row[value["row_header"]])
        elif key == "click":
          el = driver.find_element_by_id(value["id"])
          el.click()
        elif key == "wait":
          wait.until(lambda driver: driver.find_element_by_id(value['id']))
          print("found it")

#el = driver.find_element_by_id(el_id)
#print   .get_attribute("name")
