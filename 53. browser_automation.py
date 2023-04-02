# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 18:15:00 2022

@author: alvia
"""
#in the console
from selenium import webdriver
browser=webdriver.Chrome("path of chrome driver")
browser.get("https://www.selenium.org")
elem=browser.find_element_by_link_text('Download')
elem.click()
search=browser.find_elemen_nby_element_by_id('q')
search.send_keys('Download')


#how to automate whatsapp using selenium 
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome("/Users/path of the file")
driver.get("https://web.whatsapp.com")
wait=WebDriverWait(driver,600)
target='"Ravikiran"' #enter your friend's name
string="Message sent using python" #give your msg for the friend
x_arg='//span[contains(@title,'+target+')]''
target=wait.until(EC.presence_of_element_located((By.XPATH,x_arg)))
target.click()

input_box=driver.find_element_by_class_name('_1Plpp')
for i in range(50):
    input_box.send_keys(string+Keys.ENTER)