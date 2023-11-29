from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By # find html element
from selenium.webdriver.common.keys import Keys # send keys to html element 
from selenium.webdriver.support.ui import WebDriverWait # wait for page to load
from selenium.webdriver.support import expected_conditions as EC # wait for page to load
import time


service = Service(executable_path="chromedriver.exe")  
driver = webdriver.Chrome(service=service)

driver.get("https://www.24h.com.vn/")

kinhdoanh_class = "Kinh Doanh"
giavang_id = "Giá vàng"
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,"//*[@id='menu-24h-main-2023']/div[1]/ul/li[3]/a")))
kinhdoanh = driver.find_element(By.XPATH,"//*[@id='menu-24h-main-2023']/div[1]/ul/li[3]/a")
kinhdoanh.click()

WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,"//*[@id='maiContent']/main/section[1]/div/div[1]/a/div/header/h2")))
giavang = driver.find_element(By.XPATH,"//*[@id='maiContent']/main/section[1]/div/div[1]/a/div/header/h2")
giavang.click()

time.sleep(10)
driver.quit()