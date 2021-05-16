from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from multiprocessing import Pool, Manager
import re
import threading
import os
import time



chromedriver = 'C:/Users/doheun/Desktop/yam/chromedriver/chromedriver.exe'
threadLocal = threading.local()

ALLERGY_MENU = {
        'SHELL': ['회','해물,생선','매운탕,해물탕'],
        'NUT': [],
        'EGG': ['제과,베이커리'],
        'PNUT': [],
        'WHEAT': ['떡볶이','국수','제과,베이커리','냉면','돈까스,우동'],
        'FISH': ['회','해물,생선','매운탕,해물탕','아구'],
        'MILK': ['제과,베이커리'],
        'CLAM': ['회','해물,생선','매운탕,해물탕','조개'],
        'BEAN': [],
    }
#functions

def get_driver():
    driver = getattr(threadLocal, 'driver', None)
    if driver is None:

        webdriver.DesiredCapabilities.CHROME['acceptSslCerts']=True
        options = webdriver.ChromeOptions()
        options.add_argument('window-size=1920x1080')
        options.add_argument("disable-gpu")
        options.add_argument("headless")
        options.add_argument( 'user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        driver = webdriver.Chrome(chromedriver, chrome_options=options)
        setattr(threadLocal, 'driver', driver)
    return driver

def checkrest(result_list, url, id):
    driver=get_driver()
    driver.get(url)

    WebDriverWait(driver,timeout=10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#mArticle > div.cont_essential > div:nth-child(1) > div.place_details > div > h2")))
    name = driver.find_element_by_css_selector(
        '#mArticle > div.cont_essential > div:nth-child(1) > div.place_details > div > h2'
        ).text
    menu = driver.find_element_by_css_selector(
        '#mArticle > div.cont_essential > div:nth-child(1) > div.place_details > div > div > span.txt_location'
        ).text
    try:
        rate = driver.find_element_by_css_selector(
            '#mArticle > div.cont_evaluation > div.ahead_info > div > em'
        ).text
    except:
        pass
    else:
        rate = re.compile('[가-힣]+').sub('', rate) #remove korean
        if(float(rate)>3.5):
            result_list.append((name, rate, url, menu, id))

# Create your views here.

@login_required
def result(request, rest_list):
    start_time=time.time()
    from accounts.models import MSFList, ALLERGY_CHOICES
    rest_list=rest_list.rstrip(',').split(',')
    pool=Pool(processes = 4)
    manager=Manager()
    result_list = manager.list()
    pool.starmap(checkrest, [(result_list, f'https://place.map.kakao.com/{int(id)}', id) for id in rest_list])
    pool.close()
    pool.join()
    os.system("taskkill /f /im chromedriver.exe /T") #kill the chromedriver
    rest_dict = {}
    for i in result_list:
        menu = i[3]
        if menu in rest_dict:
            rest_dict[menu][0].append(i)
        else:
            rest_dict[menu]=([i], MSFList(ALLERGY_CHOICES, []))
    for menu in rest_dict.keys():
        rest_dict[menu][0].sort(key=lambda x: x[1], reverse=True )
    allergies=request.user.profile.allergy
    for allergy in allergies:
        for menu in ALLERGY_MENU[allergy]:
            if menu in rest_dict:
                rest_dict[menu][1].append(allergy)
    items= list(rest_dict.items())
    items.sort(key=lambda x: len(x[1][1]))
    print("---{}s seconds---".format(time.time()-start_time))
    return render(request, 'crawling/result.html', {'rest_list': items})