from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os
import wget

PATH = "C:/Users/gary/Desktop/selenium/chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.instagram.com/")

username = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "username"))
)

password = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "password"))
)

login = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')

password.clear()
username.clear()
username.send_keys('gary__0214')
password.send_keys('24811043')

login.click()

search = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div'))
)
search.click()

search = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]'))
)
search.click()

search = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input'))
)

# search = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.CLASS_NAME, '//*[@id="mount_0_0_Bh"]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input'))
# )

# search = driver.find_elements_by_class_name('x1lliihq x1n2onr6 x5n08af')
# search.click()

# keyword = "#cat"
# search.send_keys(keyword)
# time.sleep(1)
# search.send_keys(Keys.RETURN)
# time.sleep(1)
# search.send_keys(Keys.RETURN)

# WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.CLASS_NAME, "_aagt"))
# )

# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# time.sleep(5)

# imgs = driver.find_elements_by_class_name("_aagt")


# path = os.path.join(keyword)
# os.mkdir(path)

# count = 1
# for img in imgs:
#     save_as = os.path.join(path, keyword + str(count) + '.jpg')
#     wget.download(img.get_attribute("src"), save_as)
#     #print(img.get_attribute("src"))
#     count += 1