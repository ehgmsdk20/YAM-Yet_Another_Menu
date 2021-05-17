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
import os
import time
import re

BASE_DIR = os.path.abspath(os.path.join(os.path.join((os.path.dirname(__file__)), os.pardir), os.pardir))
chromedriver = os.path.join(BASE_DIR, 'chromedriver', 'chromedriver')

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

def get_driver(driver=None):
    if driver is None:
        options = webdriver.chrome.options.Options()
        options.add_argument("--proxy-server=socks5://127.0.0.1:9050")
        options.add_argument('window-size=1920x1080')
        options.add_argument('headless')
        options.add_argument("disable-gpu")
        options.add_argument( 'user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36')
        prefs = {'profile.default_content_setting_values': {'cookies' : 2, 'images': 2, 'plugins' : 2, 'popups': 2, 'geolocation': 2, 'notifications' : 2, 'auto_select_certificate': 2, 'fullscreen' : 2, 'mouselock' : 2, 'mixed_script': 2, 'media_stream' : 2, 'media_stream_mic' : 2, 'media_stream_camera': 2, 'protocol_handlers' : 2, 'ppapi_broker' : 2, 'automatic_downloads': 2, 'midi_sysex' : 2, 'push_messaging' : 2, 'ssl_cert_decisions': 2, 'metro_switch_to_desktop' : 2, 'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement' : 2, 'durable_storage' : 2}}   
        options.add_experimental_option('prefs', prefs)
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        driver = webdriver.Chrome(chromedriver, chrome_options=options)
    return driver

def checkrest(rest_dict, url, id, driver):
    from accounts.models import MSFList, ALLERGY_CHOICES
    driver.get(url)
    
    try:
        WebDriverWait(driver,timeout=5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#mArticle > div.cont_essential > div:nth-child(1) > div.place_details > div > div > span.txt_location")))
    except:
        print("page not loaded")
        return

    name = driver.find_element_by_xpath("//meta[@property='og:title']").get_attribute("content")
    print(name)
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
            if menu in rest_dict:
                rest_dict[menu][0].append((name, rate, url, menu, id))
            else:
                rest_dict[menu]=([(name, rate, url, menu, id)], MSFList(ALLERGY_CHOICES, []))
# Create your views here.

@login_required
def result(request, rest_list):
    start_time = time.time()
    rest_list=rest_list.rstrip(',').split(',')
    rest_dict = {}
    driver = get_driver()
    for id in rest_list:
        checkrest(rest_dict, f'https://place.map.kakao.com/{int(id)}', id, driver)
    driver.quit()
    
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
