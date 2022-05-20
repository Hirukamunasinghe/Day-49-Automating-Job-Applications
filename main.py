from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver_service = Service(executable_path="C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=driver_service)
URL ="https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"
driver.get(URL)

sign_up_link = driver.find_element(By.XPATH,"/html/body/div[1]/header/nav/div/a[2]")
sign_up_link.click()

#email
email = driver.find_element(By.ID,"username")
email.send_keys("munasinghehiruka@gmail.com")
email.send_keys(Keys.ENTER)

#password
password = driver.find_element(By.ID,"password")
password.send_keys("Hirukamun1234@")
time.sleep(3)
password.send_keys(Keys.ENTER)


#Python developer job
python_developer_job = driver.find_element(By.LINK_TEXT,"Junior Python Engineer")
python_developer_job.click()

#save
save_button = driver.find_element(By.XPATH,"/html/body/div[6]/div[3]/div[3]/div[2]/div/section[2]/div/div/div[1]/div/div[1]/div/div[2]/div[3]/div/button")
save_button.click()

#follow
follow_button = driver.find_element(By.XPATH,'//*[@id="ember362"]/section/div[1]/div[1]/button')
follow_button.click()
#driver.close()

