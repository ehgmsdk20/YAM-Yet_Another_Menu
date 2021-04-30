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
import time
import re


chromedriver = 'C:/Users/doheun/Desktop/yam/chromedriver' # 셀레늄이 이용할 크롤링 드라이버 디렉토리를 입력

# Create your views here.

@login_required
def result(request, rest_list):
    
    options = webdriver.ChromeOptions()

    options.add_argument('window-size=1920x1080')
    options.add_argument('headless')
    options.add_argument("disable-gpu")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(chromedriver, chrome_options=options)
    
    rest_list=rest_list.rstrip(',').split(',')
    name_list=[]
    for id in rest_list:
        driver.get(f'https://place.map.kakao.com/{int(id)}')
        WebDriverWait(driver,timeout=2).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#mArticle > div.cont_essential > div:nth-child(1) > div.place_details > div > h2")))
        name = driver.find_element_by_css_selector(
            '#mArticle > div.cont_essential > div:nth-child(1) > div.place_details > div > h2'
        ).text
        
        try:
            WebDriverWait(driver,timeout=2).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#mArticle > div.cont_evaluation > div.ahead_info > div > em")))
        except:
            continue
        else:
            rate = driver.find_element_by_css_selector(
                '#mArticle > div.cont_evaluation > div.ahead_info > div > em'
            ).text
            rate = re.compile('[가-힣]+').sub('', rate) #remove korean
            if(float(rate)>3.5):
                name_list.append(name)
        
    return render(request, 'crawling/result.html', {'rest_list': name_list})