from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import os

import xlrd
import time
import datetime
import pandas as pd
import json
import csv


#Note while Running program chang Chrome Driver path

driver = webdriver.Chrome(r'C:\Python3.7\chromedriver.exe')
#driver=webdriver.Chrome(r'/home/mohan/Downloads/chromedriver')
#driver.implicitly_wait()

page     = "https://www.youtube.com/watch?v=zICJVigQyuQ"

#driver = new WebDriverWait(driver, 10);
driver.get(page)
driver.maximize_window()
time.sleep(10)
setting='//*[@id="movie_player"]/div[21]/div[2]/div[2]/button[3]'

driver.find_element_by_xpath(setting).click()

time.sleep(10)
quality='//*[@id="ytp-id-18"]/div/div/div[4]/div[1]'
driver.find_element_by_xpath(quality).click()

str_360p='//*[@id="page-manager"]/ytd-watch-flexy'
driver.find_element_by_xpath(str_360p).click()








