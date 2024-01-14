from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
PATH = "C:/Users/gary/Desktop/selenium/chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get("https://www.dcard.tw/f")
print(driver.title)
search = driver.find_element_by_name("query")
search.clear()
search.send_keys("總統大選")
search.send_keys(Keys.RETURN)       # 相當於ENTER

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'atm_cs_1hcvtr6'))
)
time.sleep(3)
tieles = driver.find_elements_by_class_name("atm_cs_1hcvtr6")
for title in tieles:
    print(title.text)

# link = driver.find_element_by_link_text("總統大選理性討論")
# link.click()
# driver.back()       #上一頁
# driver.forward()

time.sleep(5)
driver.quit()