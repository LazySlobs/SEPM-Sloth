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
url4 = "https://quotes.toscrape.com/"
driver.get(url)



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

# open_window_elem = driver.find_element_by_xpath("//*[contains(text(), 'Open Window')]")
# highlight(open_window_elem, 100
#           , "red", 5)



# print(clickable_button)
# buttons = driver.find_element_by_link_text("Hide").click()
# driver.find_element_by_xpath("//*[contains(text(), 'object-oriented')]").click()

# List of href button
link_buttons = []
links = driver.find_elements_by_xpath("//a[@href]")

# Add label of href button to List
for link in links:
    link_buttons.append(link.text)

# get href_button
def href_button():
 button = input("Enter your button: ")
 if button in link_buttons:
   try:
     print(button)
     driver.find_element_by_xpath(f"//*[contains(text(), '{button}')]").click()
   except Exception:
    print("Button not available")



# List of label button
label_buttons = []
labels = driver.find_elements_by_tag_name("label")

# Add label of href button to List
for label in labels:
    label_buttons.append(label.text)

def label_button():
 button = input("Enter your button: ")
 if button in label_buttons:
   try:
     print(button)
     driver.find_element_by_xpath(f"//label[@for='{button.lower()}')]").click()
   except Exception:
    print("Button not available")

 # List of normal button
normal_buttons = []
buttons = driver.find_elements_by_xpath('//button')
for button in buttons:
    normal_buttons.append(button.text)

def normal_button():
 button = input("Enter your button: ")
 if button in normal_buttons:
   try:
     print(button)
     WebDriverWait(driver,1).until(EC.element_to_be_clickable((By.XPATH,f"//button[normalize-space()='{button}']"))).click()
   except Exception:
    print("Button not available")

normal_button()
