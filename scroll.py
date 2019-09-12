from selenium import webdriver
import time
#driver = webdriver.Chrome(r'C:\Python3.7\chromedriver.exe')
driver=webdriver.Chrome(r'/home/mohan/Downloads/chromedriver')
#driver.implicitly_wait()
#kaizala_web1 = "https://manage.kaiza.la"
page     = "https://www.youtube.com"

#driver = new WebDriverWait(driver, 10);
driver.get(page)
driver.maximize_window()


time.sleep(20)
try:
    scrolls = 4
    while True:
        scrolls -= 1
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        time.sleep(3)
        if scrolls < 0:
            break

except:
    print("failed")
