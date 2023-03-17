
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

PATH = "/Users/arianabootalebi/Documents/CODING/chromedriver"
#sets up chrome driver
#PATH = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://play.typeracer.com/")
driver.maximize_window()

def agreeBullshit():
    agreebutton = driver.find_element(By.XPATH, '//*[@id="qc-cmp2-ui"]/div[2]/div/button[3]')
    agreebutton.click()

def enterRace():
    enterbutton = driver.find_element(By.XPATH, '//*[@id="gwt-uid-1"]/a')
    enterbutton.click()

def getText():
    a = driver.find_element(By.XPATH,'//*[@id="gwt-uid-20"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[1]')
    b = driver.find_element(By.XPATH,'//*[@id="gwt-uid-20"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[2]')
    textbody = driver.find_element(By.XPATH, '//*[@id="gwt-uid-20"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[3]')
    output = str(a.text) + str(b.text)+ ' ' + str(textbody.text)

    return(output)

def waitForTimer():
    while True:
        try:
            driver.find_element(By.XPATH, '/html/body/div[5]/div/table/tbody/tr/td/table/tbody/tr/td[1]/img')
        except:
            break

def typeText(textForBox,timeToWaitBetweenCharacters):
    textlist = []
    for x in textForBox:
        textlist.append(x)
    elem = driver.find_element(By.XPATH, '//*[@id="gwt-uid-20"]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/input')
    for y in textlist:
        elem.send_keys(y)
        time.sleep(timeToWaitBetweenCharacters)

time.sleep(1)
agreeBullshit()  

time.sleep(1) 
enterRace()

time.sleep(2)
textForBox = getText()

waitForTimer()
typeText(textForBox, 0.0001)
#install most recommended version of node js 
time.sleep(3)
#driver.quit()