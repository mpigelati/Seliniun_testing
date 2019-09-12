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
import pandas as pd
import csv



username="v-mosaip@microsoft.com"

password=""
driver = webdriver.Chrome(r'C:\Python3.7\chromedriver.exe')
#driver.implicitly_wait()
#kaizala_web1 = "https://manage.kaiza.la"
page     = "https://www.youtube.com"

#driver = new WebDriverWait(driver, 10);
driver.get(page)
driver.maximize_window()

