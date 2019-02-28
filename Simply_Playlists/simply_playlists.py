#!/usr/bin/env python3
import sys
import warnings
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import os

try:
    import bs4
except ImportError:
    warnings.warn("dependency not found, please install bs4")
try:
    import requests
except ImportError:
    warnings.warn("dependency not found, please install requests")



def getStatus(soupDataLocal):
    initial = (soupDataLocal.find(attrs={"class":"ytp-time-display notranslate"}))
    endTime = initial.find(attrs={"class":"ytp-time-duration"}).text
    currTime = initial.find(attrs={"class":"ytp-time-current"}).text
    res = int(parseTime(endTime)) - int(parseTime(currTime))
    print("Current ", currTime, "|  Duration ", endTime)
    return res





def parseTime(timeString):
    hours = 0
    minutes = 0
    seconds = 0
    StringBuilder = ""
    counter = 0
    for x in timeString:
        if x == ":":
            counter+=1
    for x in timeString:
        if x == ":":
            if len(StringBuilder) == 0:
                continue
            if counter == 0:
                seconds = int(StringBuilder)
            elif counter == 1:
                minutes = int(StringBuilder)
            elif counter == 2:
                hours = int(StringBuilder)
            StringBuilder = ""
            counter -=1
        else:
            StringBuilder+=str(x)
    if len(StringBuilder) > 0:
        seconds = int(StringBuilder)
    minutes+=(hours*60)
    seconds+=(minutes*60)
    return seconds




def main(counter):
    path_to_extension = r'adBlock_Data'
    chrome_options = Options()
    chrome_options.add_argument('load-extension=' + path_to_extension)
    url = str(sys.argv[counter])
    rootPath = os.getcwd()
    driver = webdriver.Chrome(rootPath+"/chromedriver",options=chrome_options)
    driver.create_options()
    driver.implicitly_wait(10)
    driver.get(url)
    WebDriverWait(driver, 10)
    driver.refresh()
    time.sleep(10)
    # myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, r'//*[@id="movie_player"]/div[26]/div[2]/div[1]/a[2]')))
    nameOfSong = None
    timeVid = 0
    while True:
        time.sleep(timeVid + 5)
        page = driver.execute_script('return document.body.innerHTML')
        soup = bs4.BeautifulSoup(driver.page_source, 'html.parser')
        timeVid = 0
        try:
            timeVid = getStatus(soup)
            initial = (soup.find(attrs={"class": "title style-scope ytd-video-primary-info-renderer"}))
            subPage = initial.find(attrs={"class": "style-scope ytd-video-primary-info-renderer"}).text
            print(subPage)
            songNumber = (soup.find(attrs={"class": "ytp-playlist-menu-button-text"})).text
            print(songNumber)
            if nameOfSong == subPage:
                currCount = 0
                StrBuild = ""
                for c in songNumber:
                    if c == "/":
                        currCount = int(StrBuild)
                        StrBuild = ""
                    else:
                        StrBuild += c
                maxCount = int(StrBuild)
                if maxCount == currCount:
                    driver.close()
                    if len(sys.argv)>counter+1:
                        main(counter+1)
                        break
                    else:
                        break
                else:
                    #//*[@id="movie_player"]/div[26]/div[2]/div[1]/a[2]
                    print("skipping")
                    try:
                        driver.find_element_by_xpath(r'//*[@id="movie_player"]/div[27]/div[2]/div[1]/a[2]').click()
                    except:
                        driver.find_element_by_xpath(r'//*[@id="movie_player"]/div[26]/div[2]/div[1]/a[2]').click()
                    continue
            nameOfSong = subPage
        except:
            print("error")
            continue

if __name__ == "__main__":
    main(1)
