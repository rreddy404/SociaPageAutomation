# _____________________________________________________________________________

# Social Media Website Automation

# _____________________________________________________________________________

import selenium
import os
import time
import csv
import random


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import chrome

# Specified Location of Chrome Driver
chromedriver = '/usr/local/bin/chromedriver'
browser = webdriver.Chrome(chromedriver)


# _____________________________________________________________________________

# Function: Log into Website
# LUser: Username
# LPass: Password
# _____________________________________________________________________________

def WebLogin(LUser, LPass):
    browser.get('https://www.example.com/')

    username = browser.find_element_by_id("login-email")
    password = browser.find_element_by_id("login-password")

    username.send_keys(LUser)
    password.send_keys(LPass)
    browser.find_element_by_id("login-submit").click()

# _____________________________________________________________________________

# Function: Import CSV file and Open Each URL Link
# CsvFilename: The Name of the CSV File, Must be in the same folder
# Interval: Minimum Time Interval, Maximum is Interval + 30
# ______________________________________________________________________________

def RunCsvFile(CsvFilename, Interval):

    # Opens CSV File and Removes the utf-8 Encoding
    UrlsCsv = open(CsvFilename, newline='', encoding='utf-8').read().splitlines()

    # Cycles the CVS File
    for UrlRows in UrlsCsv:

        # Adds Time Interval to Wait on Each Page
        TimeInt = random.randint(Interval, Interval + 30)

        # Randomized Height to Scroll on each Page
        ScrollInt = random.randint(600, 1280)
        ScrolltoPoint = "window.scrollTo(0," + str(ScrollInt) + ");"

        # Opens URLs, Scrolls on Page, Wait Time
        browser.get(urlrows)
        browser.execute_script(ScrolltoPoint)
        time.sleep(TimeInt)

    # Logs Out of Website
    browser.get('https://www.example.com/logout/') # Example: 'https://www.linkedin.com/m/logout/'

    # Waits/Quits Browser
    time.sleep(10)
    browser.quit()


# _____________________________________________________________________________

# Calls the Functions, Requires User Information
# _____________________________________________________________________________

WebLogin('Username@email.com', 'userpassword')
RunCsvFile('URLS.csv', 60)












