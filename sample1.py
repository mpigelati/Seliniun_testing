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


#Note while Running program chang Chrome Driver path

#driver = webdriver.Chrome(r'C:\Python3.7\chromedriver.exe')
driver=webdriver.Chrome(r'/home/mohan/Downloads/chromedriver')
#driver.implicitly_wait()
#kaizala_web1 = "https://manage.kaiza.la"
page     = "https://www.youtube.com"

#driver = new WebDriverWait(driver, 10);
driver.get(page)
driver.maximize_window()

def find_videos(driver):
    video_path='//*[@id="contents"]/ytd-grid-renderer/div/ytd-grid-video-renderer'
    #driver.find_element_by_xpath('')
    print("Counting length",len(driver.find_elements_by_xpath(video_path)))

def  scroll_down_page():
    print("scrollDownPage")
    time.sleep(20)
    try:
      scrolls = 4
      while True:
        scrolls -= 1
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        print("started scrolling down")
        time.sleep(5)
        if scrolls < 0:
            break
    except:
        print("failed to scroll down the page")


def get_LisMenuInfo(driver):
    time.sleep(30)
    print("get list Menu info")
    list_menu= '//*[@id="tabsContainer"]'
    mylist='//*[@id="tabsContainer"]/div/paper-tab'
    #print("lengthListMenu", len(driver.find_elements_by_xpath(list_menu)))
    print("lengthListMenu", len(driver.find_elements_by_xpath(mylist))) #
    length= len(driver.find_elements_by_xpath(mylist))

    # Need to reduce code once basic code working
    mystring = mylist + '[' + str(2) + ']/div'
    try:
        driver.find_element_by_xpath(mystring).click()
        print("working")
        print("Before Creating Group_Bulk_Upload",driver.current_url)

    except:
        print("failed to validate")

"""
    for count in range(1,length):
        mystring = mylist + '[' + str(count) + ']/div'
        data1= driver.find_elements_by_xpath(mystring)
        print(data1)
        #if "Videos" in
         #   //*[@id="tabsContainer"]/div/paper-tab[1]/div
"""

def getHomeVideos(driver):
    print("get list of names for videos")
    time.sleep(30)
    #path1='//*[@id="page-manager"]/ytd-search/div/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer[1]/div[2]/ytd-item-section-renderer/div[3]'
    video_path = '//*[@id="contents"]/yt-horizontal-list-renderer/div[2]/div'
    print("length",len(driver.find_elements_by_xpath(video_path)))


def select_channel(driver):
    print("chennel select")
    path= '//*[@id="page-manager"]/ytd-search/div/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer[1]/div[2]/ytd-item-section-renderer/div[3]/ytd-channel-renderer/a/div[2]/ytd-channel-name/div[1]/div/yt-formatted-string'
    time.sleep(30)
    try:
        driver.find_element_by_xpath(path).click()

    except:
        print("failed to select chennel")
    # driver.find_element_by_id("text").click()


def search_step_Forum(driver):
    print("searching-STeP-IN Forum")

    driver.find_element_by_id("search").send_keys("STeP-IN Forum")
    driver.find_element_by_xpath("//*[@id='search-icon-legacy']/yt-icon").click()



search_step_Forum(driver) # searching for STeP-IN Forum page

select_channel(driver)

#getHomeVideos(driver) # Pending

get_LisMenuInfo(driver)

find_videos(driver)
#scroll_down_page(driver) Need to check the function for scroling down the web page
