####################################################
# # refresh_data
# ----
# 
# Written in the Python 3.7.9 Environment
# 
# By Nicole Lund 
# 
# This Python script scrapes useful camping information from various 
# locations for storage in a postgreSQL DB and display on a webpage.
####################################################

# Import Dependencies
import pandas as pd 
import time
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

def nws_forecast():
   ####################################################
   # Collect All National Weather Service Forecasts
   ####################################################
   nws_forecast_dict = {}    

   return nws_forecast_dict

def fire_danger(browser):
   ####################################################
   # Collect All Fire Danger Levels
   ####################################################

   # Access Bog Springs site
   bog_springs_url = 'https://www.fs.usda.gov/recarea/coronado/recreation/camping-cabins/recarea/?recid=25732&actid=29'
   bog_springs_fire_level = get_fire_level(browser, bog_springs_url)
   bog_springs_fire = {
      "location": "Bog Springs",
      "fire_level": bog_springs_fire_level
   }

   # Access Rose Canyon site
   rose_canyon_url = 'https://www.fs.usda.gov/recarea/coronado/recreation/camping-cabins/recarea/?recid=25698&actid=29'
   rose_canyon_fire_level = get_fire_level(browser, rose_canyon_url)
   rose_canyon_fire = {
      "location": "Rose Canyon",
      "fire_level": rose_canyon_fire_level
   }
   # Access Spencer Canyon site
   spencer_canyon_url = 'https://www.fs.usda.gov/recarea/coronado/recreation/camping-cabins/recarea/?recid=25710&actid=29'
   spencer_canyon_fire_level = get_fire_level(browser, spencer_canyon_url)
   spencer_canyon_fire = {
      "location": "Spencer Canyon",
      "fire_level": spencer_canyon_fire_level
   }

   fire_danger_dict = {
      "bog_springs_fire": bog_springs_fire,
      "rose_canyon_fire": rose_canyon_fire,
      "spencer_canyon_fire": spencer_canyon_fire
   }
   # print(fire_danger_dict)

   return fire_danger_dict

def get_fire_level(browser,url):
   ####################################################
   # Collect Fire Danger Level for one site
   ####################################################
   browser.visit(url)
   html = browser.html
   soup = BeautifulSoup(html, 'html.parser')

   # Collect the current fire danger
   fire_danger = soup.find('div', class_='dangerlevel').text
   
   return fire_danger

def refresh():
   ####################################################
   # Refresh Weather Data
   ####################################################

   # Initialize browser
   executable_path = {'executable_path': ChromeDriverManager().install()}
   browser = Browser('chrome', **executable_path, headless=False)

   # Retrieve NWS JSON data
   nws_forecast_dict = nws_forecast()
   # print(nws_forecast_dict)
   
   # Retrieve Campground Fire Danger
   fire_danger_dict = fire_danger(browser)
   # print(fire_danger_dict)
   
   # Store all retrieved data within a single dictionary
   refreshed_data = nws_forecast_dict
   refreshed_data.update(fire_danger_dict)

   # print(refreshed_data)

   # Close splinter browser
   browser.quit()

   return(refreshed_data)


if __name__ == "__main__":
   refresh() 