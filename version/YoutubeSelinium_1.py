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

#driver = webdriver.Chrome(r'C:\Python3.7\chromedriver.exe')
driver=webdriver.Chrome(r'/home/mohan/Downloads/chromedriver')
#driver.implicitly_wait()

page     = "https://www.youtube.com"

#driver = new WebDriverWait(driver, 10);
driver.get(page)
driver.maximize_window()

my_time= datetime.datetime.now()


def My_date_Time():
    date_time_str = '2018-06-29 08:15:27.243860'
    date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')
    # date_time_obj = datetime.datetime.strptime(date_time_str, '%d-%m-%Y %H:%M:%S.%f')

    print('Date:', date_time_obj.date())
    print('Time:', date_time_obj.time())
    print('Date-time:', date_time_obj)

    combine = str(date_time_obj.date()) + ":" + str(date_time_obj.time())
    print(combine)
    return combine




def StoreToExcel(Metadata):
    print("\n\n\n""5:--> Meatadata",)
    print("MetaData-->", Metadata, "\n\n\n\n")
    print(type(Metadata))

    with open('people1.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(Metadata)



# Getting Video information
def videosTag(driver):
    print("4:--> videosTag Function")
    J_data = []
    dataList=[]
    time.sleep(30)
    print("End video")
    mylist='//*[@id="contents"]/ytd-grid-renderer/div/ytd-grid-video-renderer'
    time_count = "/div/ytd-thumbnail/a/div[1]/ytd-thumbnail-overlay-time-status-renderer"
    videoName = "/div/div[1]/div/h3/a"

    time.sleep(40)
    videosCount = len(driver.find_elements_by_xpath(mylist))
    print("4--->VideosCount", videosCount)
    for count in range(1,videosCount): #Need to implement function  to
        print("Count:-->",count)
        dataList.append(count)
        #print("time-Count", mylist + '[' + str(count)+ ']'+ time_count)
        #print("Video name",mylist+'['+str(count)+']'+videoName)

        Ttime_count =  mylist + '[' + str(count) + ']' + time_count
        TvideoName =  mylist + '[' + str(count) + ']' + videoName
        # Getting Video name
        PVideo_name = driver.find_element_by_xpath(TvideoName).text
        print("4:--->videoName", PVideo_name)

        dataList.append(PVideo_name)
        # Getting Time stamp
        Time_stamp = driver.find_element_by_xpath(Ttime_count).text
        print("4:--->time",Time_stamp)
        dataList.append(Time_stamp)

        Video_links= driver.find_element_by_xpath(TvideoName).get_attribute('href')
        print("4:--->videolink",Video_links)
        dataList.append(Video_links)
   #     print("MetaData-->", dataList, "\n\n\n\n")
        #print("dataList",dataList)

        J_data.append(
            {
                'Count'    :dataList[0],
                'VideoName': dataList[1],
                'TimeStamp': dataList[2],
                'VideoLink': dataList[3],

            })

        with open("data.json", 'w')as fd:
            json.dump(J_data, fd, indent=4)

        StoreToExcel(dataList)
        dataList.clear()

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
    print("3:-->get_LisMenuInfo Function")
    time.sleep(20)

    list_menu= '//*[@id="tabsContainer"]'
    mylist='//*[@id="tabsContainer"]/div/paper-tab'
    #print("lengthListMenu", len(driver.find_elements_by_xpath(list_menu)))
    print("3:--->lengthListMenu", len(driver.find_elements_by_xpath(mylist))) #
    length= len(driver.find_elements_by_xpath(mylist))

    # Need to reduce code once basic code working
    mystring = mylist + '[' + str(2) + ']/div'
    try:
        driver.find_element_by_xpath(mystring).click()
        print("3:--->working")
        print("3:--->Before Creating Group_Bulk_Upload",driver.current_url)

    except:
        print("failed to validate")

"""
    Need to improve code for listing all the Menu in youtube
    for count in range(1,length):
        mystring = mylist + '[' + str(count) + ']/div'
        data1= driver.find_elements_by_xpath(mystring)
        print(data1)
        #if "Videos" in
         #   //*[@id="tabsContainer"]/div/paper-tab[1]/div
"""

def getHomeVideos(driver):
    print("get list of names for videos")
    time.sleep(20)
    #path1='//*[@id="page-manager"]/ytd-search/div/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer[1]/div[2]/ytd-item-section-renderer/div[3]'
    video_path = '//*[@id="contents"]/yt-horizontal-list-renderer/div[2]/div'
    print("length",len(driver.find_elements_by_xpath(video_path)))


def select_channel(driver):
    print("2:-->select_channel Function")
    path= '//*[@id="page-manager"]/ytd-search/div/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer[1]/div[2]/ytd-item-section-renderer/div[3]/ytd-channel-renderer/a/div[2]/ytd-channel-name/div[1]/div/yt-formatted-string'
    time.sleep(20)
    try:
        driver.find_element_by_xpath(path).click()

    except:
        print("2-->failed to select chennel")
    # driver.find_element_by_id("text").click()


def search_step_Forum(driver):
    print("1:-->searching-STeP-IN Forum Function")

    driver.find_element_by_id("search").send_keys("STeP-IN Forum")
    driver.find_element_by_xpath("//*[@id='search-icon-legacy']/yt-icon").click()

#dat_time = My_date_Time()# To get Present date and Time

search_step_Forum(driver) # searching for STeP-IN Forum page

select_channel(driver)

#getHomeVideos(driver) # Pending

get_LisMenuInfo(driver)

videosTag(driver)
#scroll_down_page(driver) Need to check the function for scroling down the web page