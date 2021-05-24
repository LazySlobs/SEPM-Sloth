from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.ui import Select

path = "C:\Program Files (x86)\msedgedriver.exe"

# Create Driver
driver = webdriver.Edge(path)
driver.maximize_window()

#  Test Url
url = "https://learn.letskodeit.com/p/practice"
url1 = "https://en.wikipedia.org/wiki/Python_%28programming_language%29"
url2 = "https://www.geeksforgeeks.org/deque-in-python/"
url3 = "https://quotes.toscrape.com/"
# React Website
url4 = "https://www.khanacademy.org/"
# Angular Website
url5 = "https://www.forbes.com/?sh=322095c92254"
driver.get(url5)



# HighLight button function
def highlight(element, effect_time, color, border):
    """Highlights (blinks) a Selenium Webdriver element"""
    driver = element._parent
    def apply_style(s):
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                              element, s)
    original_style = element.get_attribute('style')
    apply_style("border: {0}px solid {1};".format(border, color))
    time.sleep(effect_time)
    apply_style(original_style)


# get href_button
def href_button():
  # List of href button
  link_buttons = []
  links = driver.find_elements_by_xpath("//a[@href]")

  # Add label of href button to List
  for link in links:
    if link.text != "":
       link_buttons.append(link.text)

  print(link_buttons)
  button = input("Enter your button: ")
  if button in link_buttons:
   try:
     print(button)
     driver.find_element_by_xpath(f"//*[contains(text(), '{button}')]").click()
   except Exception:
    print("Button not available")





# get label_button
def label_button():
 # List of label button
 label_buttons = []
 labels = driver.find_elements_by_tag_name("label")

 # Add label of href button to List
 for label in labels:
     if label.text != "":
          label_buttons.append(label.text)

 print(label_buttons)
 button = input("Enter your button: ")
 if button in label_buttons:
   try:
     print(button)
     driver.find_element_by_xpath(f"//label[@for='{button.lower()}')]").click()
   except Exception:
    print("Button not available")




# get normal_button
def normal_button():
 # List of normal button
 normal_buttons = []
 buttons = driver.find_elements_by_xpath('//button')
 for button in buttons:
     if button.text != "":
         normal_buttons.append(button.text)

 print(normal_buttons)
 button = input("Enter your button: ")
 if button in normal_buttons:
   try:
     print(button)
     WebDriverWait(driver,1).until(EC.element_to_be_clickable((By.XPATH,f"//button[normalize-space()='{button}']"))).click()
   except Exception:
    print("Button not available")





#get input_button
def input_button():

 input_buttons = []
 input_elements = driver.find_elements_by_xpath("//input[@value]")
 for input_value in input_elements:
     if input_value.text != "":
         input_buttons.append(input_value.get_attribute('value'))

 print(input_buttons)
 button = input("Enter your button: ")
 if button in input_buttons:
     try:
         print(button)
         driver.find_element_by_xpath(f"//input[@value='{button}']").click()
     except Exception:
         print("Button not available")


#get place_holder_button
def place_holder_button():

 place_holder_buttons = []
 place_holder_elements = driver.find_elements_by_xpath("//input[@placeholder]")
 for place_holder_value in place_holder_elements:
     if place_holder_value.text != "":
         place_holder_buttons.append(place_holder_value.get_attribute('placeholder'))

 print(place_holder_buttons)
 button = input("Enter your button: ")
 if button in place_holder_buttons:
     try:
         print(button)
         driver.find_element_by_xpath(f"//input[@placeholder='{button}']").click()
     except Exception:
         print("Button not available")


