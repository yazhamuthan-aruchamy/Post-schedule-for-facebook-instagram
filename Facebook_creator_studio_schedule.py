import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
import pyautogui
from selenium.webdriver.common.action_chains import ActionChains
import csv
from colorama import Fore
import getpass


Email_id = input("\033[1;32m Enter your Valid Email Address here : \t")
Password = getpass.getpass("\033[1;32m Enter the Password Here : \t")
file_csv = input("\033[1;32m Enter Your CSV path here: \t ")
Chrome_path = input("\033[1;32m Enter your Chrome Path here: \t")
print(Fore.RED + "NOTE : YOU NEED TO ONLY USE THE IMAGE WITH THE ASPECT RATIO OR ELSE THIS WILL FAIL")


options = webdriver.ChromeOptions()
options.add_argument('proxy-server=106.122.8.54:3128')
options.add_argument(r'--user-data-dir={}'.format(Chrome_path))
browser = uc.Chrome(options=options)
browser.maximize_window()

browser.get("https://business.facebook.com/creatorstudio/home")
try:
    time.sleep(4)
    login_button = browser.find_element(By.XPATH, "//*[starts-with(@id,'u_0_0_')]/div[2]/div/div[2]/div/div/div/div[2]/div/div")
    login_button.click()
    time.sleep(3)
    login = browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div[2]/div[2]/form/div/div[1]/input")
    action = ActionChains(browser)
    action.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE * 10).perform()
    login.clear()
    login.click()
    login.send_keys(Email_id)
    time.sleep(3)
    passwords = browser.find_element(By.XPATH, "//*[@id='pass']")
    action = ActionChains(browser)
    action.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE * 10).perform()
    passwords.clear()
    passwords.click()
    time.sleep(2)
    passwords.send_keys(Password)
    time.sleep(3)
    ok_button = browser.find_element(By.XPATH, "//*[@id='loginbutton']")
    ok_button.click()
    time.sleep(10)
except:
    pass
with open(file_csv, newline='', mode='r') as csvfile:
    reading = csv.DictReader(csvfile)
    for row in reading:
        file_path = row['filepath']
        title_text = row['title']
        facebook_date_count = row['facebookdate']
        facebook_hours_count = row['facebookhour']
        facebook_minutes_count = row['facebookminutes']
        facebook_time_count = row['facebooktime']
        instagram_date_count = row['instagramdate']
        instagram_hours_count = row['instagramhour']
        instagram_minutes_count = row['instagramminutes']
        instagram_time_count = row['instagramtime']
        
        
        browser.get("https://business.facebook.com/latest/composer?nav_ref=media_manager_redirect_home&ref=biz_web_home&context_ref=HOME")
        time.sleep(3)
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div/div[1]/div[1]/div/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div[2]/div[1]/div/div[2]/div"))).click()
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div[3]/div/div/div[2]/div/div"))).click()
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div/div[1]/div[1]/div/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div[2]/div[1]/div/div[2]/div"))).click()
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div/div[1]/div[1]/div/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div[1]/div[1]/div[3]/div/div[1]/div/div/div"))).click()
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div/div[1]/div[1]/div/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div[2]/div[1]/div[2]/div/div[1]/div"))).click()
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div/div"))).click()
        time.sleep(3)
        pyautogui.write(file_path)
        time.sleep(2) 
        pyautogui.press('enter')
        time.sleep(3)
        text_box = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div/div[1]/div[1]/div/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div[1]/div[1]/div[3]/div/div[2]/div[1]/div[2]/div[2]/div/div[2]/div/div/div/div[1]/div[2]/div/div/div/div[1]/div/div/div/div/div/div/div")))
        text_box.click()
        time.sleep(2)
        text_box.send_keys(title_text)
        WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div/div[1]/div[1]/div/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div[1]/div[1]/div[4]/div/div/div[1]/div[2]/div[1]/div[2]/div[2]"))).click()
        #facebook schedule
        date_schedule = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div/div[1]/div[1]/div/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div[1]/div[1]/div[4]/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div[1]/div/div[2]/div/div/div/div[1]/div[2]/div/div/input")))
        date_schedule.click()
        action = ActionChains(browser)
        action.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE * 10).perform()
        time.sleep(3)
        date_schedule.send_keys(facebook_date_count)
        hours_time = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div/div[1]/div[1]/div/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div[1]/div[1]/div[4]/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div/div/div[2]/div[1]/div/input")))
        hours_time.click()
        hours_time.send_keys(facebook_hours_count)
        minutes_time = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div/div[1]/div[1]/div/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div[1]/div[1]/div[4]/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div/div/div[2]/div[2]/div/input")))
        minutes_time.click()
        minutes_time.send_keys(facebook_minutes_count)
        time_formate = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div/div[1]/div[1]/div/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div[1]/div[1]/div[4]/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div/div/div[2]/div[3]/div/input")))
        time_formate.click()
        time_formate.send_keys(facebook_time_count)
        #instgram.schdule
        time.sleep(4)
        Action_button = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div/div[1]/div[1]/div/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div[1]/div[1]/div[4]/div/div/div[1]/div[2]/div[2]/div[4]/div")))
        browser.execute_script("arguments[0].scrollIntoView(true);",Action_button)
        instagram_schedule = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div/div[1]/div[1]/div/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div[1]/div[1]/div[4]/div/div/div[1]/div[2]/div[2]/div[3]/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div/div/div[1]/div[2]/div/div/input")))
        instagram_schedule.click()
        action = ActionChains(browser)
        action.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE * 15).perform()
        instagram_schedule.send_keys(instagram_date_count)
        instagram_hours = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div/div[1]/div[1]/div/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div[1]/div[1]/div[4]/div/div/div[1]/div[2]/div[2]/div[3]/div[2]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div[1]/div/div[2]/div[1]/div/input")))
        instagram_hours.click()
        instagram_hours.send_keys(instagram_hours_count)
        instagram_minutes = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div/div[1]/div[1]/div/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div[1]/div[1]/div[4]/div/div/div[1]/div[2]/div[2]/div[3]/div[2]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div[1]/div/div[2]/div[2]/div/input")))
        instagram_minutes.click()
        instagram_minutes.send_keys(instagram_minutes_count)
        instagram_formate = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div/div[1]/div[1]/div/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div[1]/div[1]/div[4]/div/div/div[1]/div[2]/div[2]/div[3]/div[2]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div[1]/div/div[2]/div[3]/div/input")))
        instagram_formate.click()
        instagram_formate.send_keys(instagram_time_count)
        schedule_button_click = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div/div[1]/div[1]/div/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div[2]/div/div[2]/div")))
        schedule_button_click.click()
        time.sleep(5)