from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from multiprocessing import Pool
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import random,time,os,re
from time import sleep
import config
cwd = os.getcwd()
opts = Options()
opts.headless = True
opts.add_argument('log-level=3') 
dc = DesiredCapabilities.CHROME
dc['loggingPrefs'] = {'driver': 'OFF', 'server': 'OFF', 'browser': 'OFF'}
opts.add_argument('--ignore-ssl-errors=yes')
opts.add_argument("--start-maximized")
opts.add_argument('--ignore-certificate-errors')
opts.add_argument('--disable-blink-features=AutomationControlled')
opts.add_experimental_option('excludeSwitches', ['enable-logging'])
# opts.add_argument("--window-size=500,300")
def xpath_type(el,mount):
    return wait(browser,15).until(EC.element_to_be_clickable((By.XPATH, el))).send_keys(mount)
def xpath_fast(el):
    return wait(browser,1).until(EC.element_to_be_clickable((By.XPATH, el))).click()
def xpath_el(el):
    element_all = wait(browser,30).until(EC.presence_of_element_located((By.XPATH, el)))
    
    element_all.click()
 
def date():
    date = f"[{time.strftime('%d-%m-%y %X')}]"
    return date
global no
no = 0
def bot():
    email = config.account.split("|")[0]
    password = config.account.split("|")[1]
    global browser
    browser = webdriver.Chrome(ChromeDriverManager().install(),options=opts, desired_capabilities=dc)
    browser.get("https://admin.google.com/u/6/ac/users?hl=en")

    print(f'[+] {date()} Login')
    sleep(1)
    xpath_type('//*[@type="email"]',email)
    sleep(1)
    xpath_type('//input[@type="email"]',Keys.ENTER)
    xpath_type('//*[@type="password"]',password)
    sleep(1)
    xpath_type('//input[@type="password"]',Keys.ENTER)
    sleep(5)
    acc = 50
    repeat = 1
    for i in range(1,5000):
        if repeat == 5:
            break
        try:
            print(f'[+] {date()} Trying to delete {acc} accounts')
            xpath_el('//div[@aria-label="Select all rows"]')
            
            try:
                xpath_fast('//div[text()="Email"]/following-sibling::div/div[contains(@title,"admin")]/ancestor::td/ancestor::tr/td[1]')
            except:
                pass
            xpath_el('(//*[@title="More options"])[1]')
            xpath_type('/html/body/div[7]/c-wiz/div/div[1]/div/div/div[2]/div/div[3]/div/div/span[4]',Keys.ENTER)
          
            sleep(1)
            for i in range(1,5):
                xpath_el(f'(html/body/div[7]/div[5]/div/div[2]/span/div/span/div/c-wiz/div[2]/span/div/div[1]/label/div[1]/div[2])[{i}]')
            element_all = wait(browser,30).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[7]/div[5]/div/div[2]/span/div/span/div/c-wiz/div[3]/div[2]")))
            browser.execute_script("arguments[0].scrollIntoView();", element_all)
            xpath_el("/html/body/div[7]/div[5]/div/div[2]/span/div/span/div/c-wiz/div[3]/div[2]")
            xpath_el('//span[text()="Done"]')
            print(f'[+] {date()} Done delete {acc} accounts')
            acc = acc + 50
            sleep(2)
            browser.refresh()
            sleep(1)
            browser.refresh()
            sleep(0.5)
            browser.refresh()
            sleep(0.5)
            browser.refresh()
            sleep(0.5)
            browser.refresh()
            sleep(0.5)
            browser.refresh()
            sleep(0.5)
        except Exception as e:
            repeat = repeat +1
bot()