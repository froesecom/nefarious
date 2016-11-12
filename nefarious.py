from selenium import webdriver
import selenium.webdriver.support.ui as ui
import time
import yaml
import csv
import pdb

print "just imported selenium"
stream   = file("config/instructions.yml", "r")
settings = yaml.load(stream)

baseurl = settings["baseurl"]
driver = webdriver.Chrome("/Library/drivers/chromedriver")
wait = ui.WebDriverWait(driver,10)
driver.get(baseurl)

print "opening csv..."
with open("config/input_data_test.csv", "rU") as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
     
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
          print("wait is over")
        elif key == "click_child":
          el = driver.find_element_by_id(value["id"])
          el.find_elements_by_tag_name(value["tag"])[0].click()
        elif key == "switch_window":
          driver.switch_to_window(driver.window_handles[1])
          #driver.switch_to_window(value["target"])

#driver.quit()
