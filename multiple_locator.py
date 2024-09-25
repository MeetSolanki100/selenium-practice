from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://www.amazon.in/s?k=laptop&crid=2HKYWR7ULS4H7&sprefix=laptop%2Caps%2C193&ref=nb_sb_noss_1")  
elems = driver.find_elements(By.CLASS_NAME, "puis-card-container")
print(f"{len(elems)} elements found...")
file=0
for elem in elems:
    d = elem.get_attribute("outerHTML")
    with open(f"data/{file}.html", "w", encoding="utf-8") as f:
        f.write(d)
        file += 1
time.sleep(2)
driver.close()