# -*- coding: utf-8 -*-
"""
Created on Wed May  1 08:59:01 2019

@author: nehaj
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver= webdriver.Chrome("chromedriver.exe")
driver.maximize_window()
driver.get("https://www.iemcrp.com/")
wait=WebDriverWait(driver,600)

target1 = driver.find_element_by_link_text('Institute of Engineering and Management,Kolkata(104)').click()

username="Your_Username"
password="Your_Password"

us=driver.find_element_by_id("text1")
us.clear()
us.send_keys(username)

pswd=driver.find_element_by_id("text2")
pswd.clear()
pswd.send_keys(password)
login = driver.find_element_by_xpath("//select[@name='mtype']/option[text()='Student']").click()

go=driver.find_element_by_id("submit1").click()

mytext = driver.find_element_by_xpath("//td/table/tbody/tr[12]").click()
resultbutton  = driver.find_elements_by_tag_name('input')[0].click()
short_performance = driver.find_element_by_tag_name('table').text
detail_performance = driver.find_element_by_tag_name('div').text
print(short_performance, '\n\n', detail_performance)
#time.sleep(5)

driver.quit()
