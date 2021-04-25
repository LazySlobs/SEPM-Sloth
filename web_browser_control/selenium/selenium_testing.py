from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

path = "C:\Program Files (x86)\msedgedriver.exe"


driver = webdriver.Edge(path)
driver.maximize_window()
url = "https://learn.letskodeit.com/p/practice"
url1 = "https://en.wikipedia.org/wiki/Python_%28programming_language%29"
url2 = "https://www.geeksforgeeks.org/deque-in-python/"
url4 = "https://quotes.toscrape.com/"
driver.get(url4)



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

# open_window_elem = driver.find_element_by_xpath("//*[contains(text(), 'Mouse Hover')]")
# highlight(open_window_elem, 100
#           , "red", 5)



clickable_button = []
elems = driver.find_elements_by_xpath("//a[@href]")
# for elem in elems:
#     print(elem.text)


for elem in elems:
    clickable_button.append(elem.text)


print(clickable_button)
# buttons = driver.find_element_by_link_text("Hide").click()
# driver.find_element_by_xpath("//*[contains(text(), 'object-oriented')]").click()

button = input("Enter your button: ")
if button in clickable_button:
   print(button)
   driver.find_element_by_xpath(f"//*[contains(text(), '{button}')]").click()


