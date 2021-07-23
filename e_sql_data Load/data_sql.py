###################################################################
# holdings_clean.ipynb - Holdings file Clean
# by Tarak Patel
#
# This is Python script for cleanup of 5 Portfolio holdings excel file 
# downloaded from
# https://individuals.voya.com/product/variable-portfolio/holdings/monthly
#
# Then it combines all the df into one df to upload to SQL.
#
# This script was converted from holdings_clean.ipynb
####################################################################

# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd 
import json
import requests
import numpy as np
import datetime
from datetime import timedelta
from splinter import Browser
from bs4 import BeautifulSoup


# %%
# Pull metadata for Bog Springs Campgraound
bs_url = "https://api.weather.gov/points/31.7276,-110.8754"
response_bs = requests.get(bs_url)
data_bs = response_bs.json()
data_bs
grid_data_bs = data_bs["properties"]["forecastGridData"]
grid_data_bs


# %%
# Pull Forecast Grid data for BogSprings Campground
bs_forcast_url = grid_data_bs
response_bs_forecast = requests.get(bs_forcast_url)
data_bs_forecast = response_bs_forecast.json()

data_bs_forecast
lat_bs = data_bs_forecast["geometry"]["coordinates"][0][0][1]
lat_bs
lng_bs = data_bs_forecast["geometry"]["coordinates"][0][0][0]
lng_bs
elevation_bs = data_bs_forecast["properties"]["elevation"]["value"]
elevation_bs

# Create a Dataframe for Bog Springs Campground
bs_df = pd.DataFrame({"id": 1,
              "campground": "Bog Springs",
              "lat": [lat_bs],
              "lon": [lng_bs],
              "elevation": [elevation_bs],
              "nws_meta_url": [bs_url],
              "nws_grid_url": [grid_data_bs],
              "forest_url":"https://www.fs.usda.gov/recarea/coronado/recreation/camping-cabins/recarea/?recid=25732&actid=29",
              "campsite_url": "https://www.fs.usda.gov/Internet/FSE_MEDIA/fseprd746637.jpg",
              "fire_danger": "Very High",
              "map_code": '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3393.5714340164473!2d-110.87758868361043!3d31.72759998130141!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x86d6970db0a5e44d%3A0x1b48084e4d6db970!2sBog%20Springs%20Campground!5e0!3m2!1sen!2sus!4v1626560932236!5m2!1sen!2sus" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy"></iframe>' 
                    })
bs_df


# %%
# Pull Grid Data for Bog Springs CampGround
temp = []
for i in data_bs_forecast["properties"]["temperature"]["values"]:
    temp.append(i)
temp_df = pd.DataFrame(temp)
temp_df
# Temperature conversion to Degree Fahrenheit
temp_df['degF'] = (temp_df['value'] * 9 / 5) + 32
temp_df

# validTime Column split to date and time for Temperature
date_temp = temp_df['validTime'].str.split('T', n=1, expand=True)
time_temp = date_temp[1].str.split('+', n=1, expand=True)
time_temp
temp_df['date_temp'] = date_temp[0]
temp_df['time_temp'] = time_temp[0]

temp_df['date_time_temp'] = temp_df['date_temp'] + ' ' + temp_df['time_temp']
temp_df['date_time_temp'] = pd.to_datetime(temp_df['date_time_temp'])

# Pulling only today + 3 days worth of data
time_delta_temp = datetime.datetime.strptime(temp_df['date_temp'][0],"%Y-%m-%d") + timedelta(days = 4)
temp_df['times_temp'] = time_delta_temp.strftime("%Y-%m-%d")
temp_df = temp_df.loc[temp_df['date_temp'] < temp_df['times_temp']]
temp_df
# temp_df.dtypes


# ##### Pulling Wind Speed ########
wind_speed = []
for i in data_bs_forecast["properties"]["windSpeed"]["values"]:
    wind_speed.append(i) 
windSpeed_df = pd.DataFrame(wind_speed) 
windSpeed_df

# Converting KM/hour to Miles/hour
windSpeed_df['miles/hour'] = windSpeed_df['value'] * 0.621371
windSpeed_df

# validTime Column split to date and time for wind Speed
date_ws = windSpeed_df['validTime'].str.split('T', n=1, expand=True)
time_ws = date_ws[1].str.split('+', n=1, expand=True)
time_ws
windSpeed_df['date_ws'] = date_ws[0]
windSpeed_df['time_ws'] = time_ws[0]

windSpeed_df['date_time_ws'] = windSpeed_df['date_ws'] + ' ' + windSpeed_df['time_ws']
windSpeed_df['date_time_ws'] = pd.to_datetime(windSpeed_df['date_time_ws'])

# Pulling only today + 3 days worth of data
time_delta_ws = datetime.datetime.strptime(windSpeed_df['date_ws'][0],"%Y-%m-%d") + timedelta(days = 4)
windSpeed_df['times_ws'] = time_delta_ws.strftime("%Y-%m-%d")
windSpeed_df = windSpeed_df.loc[windSpeed_df['date_ws'] < windSpeed_df['times_ws']]
windSpeed_df
# windSpeed_df.dtypes


# ##### Pulling Wind Gusts ########
wind_gust = []
for i in data_bs_forecast["properties"]["windGust"]["values"]:
    wind_gust.append(i) 
wind_gust_df = pd.DataFrame(wind_gust) 
wind_gust_df

# Converting KM/hour to Miles/hour
wind_gust_df['m/h'] = wind_gust_df['value'] * 0.621371
wind_gust_df

# # validTime Column split to date and time for wind Gusts
date_wg = wind_gust_df['validTime'].str.split('T', n=1, expand=True)
time_wg = date_wg[1].str.split('+', n=1, expand=True)
time_wg
wind_gust_df['date_wg'] = date_wg[0]
wind_gust_df['time_wg'] = time_wg[0]

wind_gust_df['date_time_wg'] = wind_gust_df['date_wg'] + ' ' + wind_gust_df['time_wg']
wind_gust_df['date_time_wg'] = pd.to_datetime(wind_gust_df['date_time_wg'])
wind_gust_df

# Pulling only today + 3 days worth of data
time_delta_wg = datetime.datetime.strptime(wind_gust_df['date_wg'][0],"%Y-%m-%d") + timedelta(days = 4)
wind_gust_df['times_wg'] = time_delta_wg.strftime("%Y-%m-%d")
wind_gust_df = wind_gust_df.loc[wind_gust_df['date_wg'] < wind_gust_df['times_wg']]
wind_gust_df
# wind_gust_df.dtypes

# # ##### Pulling Probability Precipitation ########
prob_precip = []
for i in data_bs_forecast["properties"]["probabilityOfPrecipitation"]["values"]:
    prob_precip.append(i) 
prob_precip_df = pd.DataFrame(prob_precip) 
prob_precip_df

# # validTime Column split to date and time for Probability Precipitation
date_pp = prob_precip_df['validTime'].str.split('T', n=1, expand=True)
time_pp = date_pp[1].str.split('+', n=1, expand=True)
time_pp
prob_precip_df['date_pp'] = date_pp[0]
prob_precip_df['time_pp'] = time_pp[0]

prob_precip_df['date_time_pp'] = prob_precip_df['date_pp'] + ' ' + prob_precip_df['time_pp']
prob_precip_df['date_time_pp'] = pd.to_datetime(prob_precip_df['date_time_pp'])
prob_precip_df

# Pulling only today + 3 days worth of data
time_delta_pp = datetime.datetime.strptime(prob_precip_df['date_pp'][0],"%Y-%m-%d") + timedelta(days = 4)
prob_precip_df['times_pp'] = time_delta_pp.strftime("%Y-%m-%d")
prob_precip_df = prob_precip_df.loc[prob_precip_df['date_pp'] < prob_precip_df['times_pp']]
prob_precip_df
# prob_precip_df.dtypes

# # ##### Pulling quantity Precipitation ########
qty_precip = []
for i in data_bs_forecast["properties"]["quantitativePrecipitation"]["values"]:
    qty_precip.append(i) 
qty_precip_df = pd.DataFrame(qty_precip) 
qty_precip_df

# # validTime Column split to date and time for quantity Precipitation
date_qp = qty_precip_df['validTime'].str.split('T', n=1, expand=True)
time_qp = date_qp[1].str.split('+', n=1, expand=True)
time_qp
qty_precip_df['date_qp'] = date_qp[0]
qty_precip_df['time_qp'] = time_qp[0]

qty_precip_df['date_time_qp'] = qty_precip_df['date_qp'] + ' ' + qty_precip_df['time_qp']
qty_precip_df['date_time_qp'] = pd.to_datetime(qty_precip_df['date_time_qp'])
qty_precip_df

# Pulling only today + 3 days worth of data
time_delta_qp = datetime.datetime.strptime(qty_precip_df['date_qp'][0],"%Y-%m-%d") + timedelta(days = 4)
qty_precip_df['times_qp'] = time_delta_qp.strftime("%Y-%m-%d")
qty_precip_df = qty_precip_df.loc[qty_precip_df['date_qp'] < qty_precip_df['times_qp']]
qty_precip_df
# qty_precip_df.dtypes


bs_grid_df = pd.DataFrame({"id":1,
        "campground": "Bog Springs",
        "forecasted_temperature_degF": temp_df['degF'],
        "forecastTime_temperature": temp_df['date_time_temp'],
        "forecasted_windSpeed_miles_per_h": windSpeed_df['miles/hour'],
        "forecastTime_windSpeed": windSpeed_df['date_time_ws'],
        "forecasted_windGust_miles_per_h": wind_gust_df['m/h'],
        "forecastTime_windGust": wind_gust_df['date_time_wg'],
        "forecasted_probabilityOfPrecipitation": prob_precip_df['value'],
        "forecastTime_probabilityOfPrecipitation": prob_precip_df['date_time_pp'],
        "forecasted_quantityOfPrecipitation_mm": qty_precip_df['value'],
        "forecastTime_quantityOfPrecipitation": qty_precip_df['date_time_qp'],
       })
bs_grid_df
# bs_grid_df.dtypes

# %%
# Pull metadata for Rose Canyon Campgraound
rc_url = "https://api.weather.gov/points/32.395,-110.6911"
response_rc = requests.get(rc_url)
data_rc = response_rc.json()
data_rc
grid_data_rc = data_rc["properties"]["forecastGridData"]
grid_data_rc


# %%
# Pull Forecast Grid data for Rose Canyon Campground
rc_forcast_url = grid_data_rc
response_rc_forecast = requests.get(rc_forcast_url)
data_rc_forecast = response_rc_forecast.json()
data_rc_forecast
lat_rc = data_rc_forecast["geometry"]["coordinates"][0][0][1]
lat_rc
lng_rc = data_rc_forecast["geometry"]["coordinates"][0][0][0]
lng_rc
elevation_rc = data_rc_forecast["properties"]["elevation"]["value"]
elevation_rc

# Create a Dataframe for Rose Canyon Campground
rc_df = pd.DataFrame({"id": 2,
              "campground": "Rose Canyon",
              "lat": [lat_rc],
              "lon": [lng_rc],
              "elevation": [elevation_rc],
              "nws_meta_url": [rc_url],
              "nws_grid_url": [grid_data_rc],
              "forest_url":"https://www.fs.usda.gov/recarea/coronado/recreation/camping-cabins/recarea/?recid=25698&actid=29",
              "campsite_url": "https://cdn.recreation.gov/public/2019/06/20/00/19/232284_beeddff5-c966-49e2-93a8-c63c1cf21294_700.jpg",
            #   "nws_meta_json":[data_rc],
            #   "nws_grid_json": [data_rc_forecast],
              "fire_danger": "Very High",
              "map_code": '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3368.97130566869!2d-110.70672358360277!3d32.39313088108983!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x86d6400421614087%3A0xb6cfb84a4b05c95b!2sRose%20Canyon%20Campground!5e0!3m2!1sen!2sus!4v1626560965073!5m2!1sen!2sus" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy"></iframe>' 
                    })
rc_df


# %%
# Pull Grid Data for Rose Canyon CampGround
temp_rc = []
for i in data_rc_forecast["properties"]["temperature"]["values"]:
    temp_rc.append(i)
temp_rc_df = pd.DataFrame(temp_rc)
temp_rc_df
# Temperature conversion to Degree Fahrenheit
temp_rc_df['degF_rc'] = (temp_rc_df['value'] * 9 / 5) + 32
temp_rc_df

# validTime Column split to date and time for Temperature
date_temp_rc = temp_rc_df['validTime'].str.split('T', n=1, expand=True)
time_temp_rc = date_temp_rc[1].str.split('+', n=1, expand=True)
time_temp_rc
temp_rc_df['date_temp_rc'] = date_temp_rc[0]
temp_rc_df['time_temp_rc'] = time_temp_rc[0]

temp_rc_df['date_time_temp_rc'] = temp_rc_df['date_temp_rc'] + ' ' + temp_rc_df['time_temp_rc']
temp_rc_df['date_time_temp_rc'] = pd.to_datetime(temp_rc_df['date_time_temp_rc'])

# Pulling only today + 3 days worth of data
time_delta_temp_rc = datetime.datetime.strptime(temp_rc_df['date_temp_rc'][0],"%Y-%m-%d") + timedelta(days = 4)
temp_rc_df['times_temp_rc'] = time_delta_temp_rc.strftime("%Y-%m-%d")
temp_rc_df = temp_rc_df.loc[temp_rc_df['date_temp_rc'] < temp_rc_df['times_temp_rc']]
temp_rc_df
temp_rc_df.dtypes


# ##### Pulling Wind Speed ########
wind_speed_rc = []
for i in data_rc_forecast["properties"]["windSpeed"]["values"]:
    wind_speed_rc.append(i) 
windSpeed_rc_df = pd.DataFrame(wind_speed_rc) 
windSpeed_rc_df

# Converting KM/hour to Miles/hour
windSpeed_rc_df['miles/hour_rc'] = windSpeed_rc_df['value'] * 0.621371
windSpeed_rc_df

# validTime Column split to date and time for wind Speed
date_ws_rc = windSpeed_rc_df['validTime'].str.split('T', n=1, expand=True)
time_ws_rc = date_ws_rc[1].str.split('+', n=1, expand=True)
time_ws_rc
windSpeed_rc_df['date_ws_rc'] = date_ws_rc[0]
windSpeed_rc_df['time_ws_rc'] = time_ws_rc[0]

windSpeed_rc_df['date_time_ws_rc'] = windSpeed_rc_df['date_ws_rc'] + ' ' + windSpeed_rc_df['time_ws_rc']
windSpeed_rc_df['date_time_ws_rc'] = pd.to_datetime(windSpeed_rc_df['date_time_ws_rc'])

# Pulling only today + 3 days worth of data
time_delta_ws = datetime.datetime.strptime(windSpeed_rc_df['date_ws_rc'][0],"%Y-%m-%d") + timedelta(days = 4)
windSpeed_rc_df['times_ws_rc'] = time_delta_ws.strftime("%Y-%m-%d")
windSpeed_rc_df = windSpeed_rc_df.loc[windSpeed_rc_df['date_ws_rc'] < windSpeed_rc_df['times_ws_rc']]
windSpeed_rc_df
# windSpeed_rc_df.dtypes


# ##### Pulling Wind Gusts ########
wind_gust_rc = []
for i in data_rc_forecast["properties"]["windGust"]["values"]:
    wind_gust_rc.append(i) 
wind_gust_rc_df = pd.DataFrame(wind_gust_rc) 
wind_gust_rc_df

# Converting KM/hour to Miles/hour
wind_gust_rc_df['m/h_rc'] = wind_gust_rc_df['value'] * 0.621371
wind_gust_rc_df

# # validTime Column split to date and time for wind Gusts
date_wg_rc = wind_gust_rc_df['validTime'].str.split('T', n=1, expand=True)
time_wg_rc = date_wg_rc[1].str.split('+', n=1, expand=True)
time_wg_rc
wind_gust_rc_df['date_wg_rc'] = date_wg_rc[0]
wind_gust_rc_df['time_wg_rc'] = time_wg_rc[0]

wind_gust_rc_df['date_time_wg_rc'] = wind_gust_rc_df['date_wg_rc'] + ' ' + wind_gust_rc_df['time_wg_rc']
wind_gust_rc_df['date_time_wg_rc'] = pd.to_datetime(wind_gust_rc_df['date_time_wg_rc'])
wind_gust_rc_df

# Pulling only today + 3 days worth of data
time_delta_wg = datetime.datetime.strptime(wind_gust_rc_df['date_wg_rc'][0],"%Y-%m-%d") + timedelta(days = 4)
wind_gust_rc_df['times_wg_rc'] = time_delta_wg.strftime("%Y-%m-%d")
wind_gust_rc_df = wind_gust_rc_df.loc[wind_gust_rc_df['date_wg_rc'] < wind_gust_rc_df['times_wg_rc']]
wind_gust_rc_df
# wind_gust_rc_df.dtypes

# # # ##### Pulling Probability Precipitation ########
prob_precip_rc = []
for i in data_rc_forecast["properties"]["probabilityOfPrecipitation"]["values"]:
    prob_precip_rc.append(i) 
prob_precip_rc_df = pd.DataFrame(prob_precip_rc) 
prob_precip_rc_df

# # validTime Column split to date and time for Probability Precipitation
date_pp_rc = prob_precip_rc_df['validTime'].str.split('T', n=1, expand=True)
time_pp_rc = date_pp_rc[1].str.split('+', n=1, expand=True)
time_pp_rc
prob_precip_rc_df['date_pp_rc'] = date_pp_rc[0]
prob_precip_rc_df['time_pp_rc'] = time_pp_rc[0]

prob_precip_rc_df['date_time_pp_rc'] = prob_precip_rc_df['date_pp_rc'] + ' ' + prob_precip_rc_df['time_pp_rc']
prob_precip_rc_df['date_time_pp_rc'] = pd.to_datetime(prob_precip_rc_df['date_time_pp_rc'])
prob_precip_rc_df

# Pulling only today + 3 days worth of data
time_delta_pp = datetime.datetime.strptime(prob_precip_rc_df['date_pp_rc'][0],"%Y-%m-%d") + timedelta(days = 4)
prob_precip_rc_df['times_pp_rc'] = time_delta_pp.strftime("%Y-%m-%d")
prob_precip_rc_df = prob_precip_rc_df.loc[prob_precip_rc_df['date_pp_rc'] < prob_precip_rc_df['times_pp_rc']]
prob_precip_rc_df
# prob_precip_rc_df.dtypes

# # ##### Pulling quantity Precipitation ########
qty_precip_rc = []
for i in data_rc_forecast["properties"]["quantitativePrecipitation"]["values"]:
    qty_precip_rc.append(i) 
qty_precip_rc_df = pd.DataFrame(qty_precip_rc) 
qty_precip_rc_df

# # validTime Column split to date and time for quantity Precipitation
date_qp_rc = qty_precip_rc_df['validTime'].str.split('T', n=1, expand=True)
time_qp_rc = date_qp_rc[1].str.split('+', n=1, expand=True)
time_qp_rc
qty_precip_rc_df['date_qp_rc'] = date_qp_rc[0]
qty_precip_rc_df['time_qp_rc'] = time_qp_rc[0]

qty_precip_rc_df['date_time_qp_rc'] = qty_precip_rc_df['date_qp_rc'] + ' ' + qty_precip_rc_df['time_qp_rc']
qty_precip_rc_df['date_time_qp_rc'] = pd.to_datetime(qty_precip_rc_df['date_time_qp_rc'])
qty_precip_rc_df

# Pulling only today + 3 days worth of data
time_delta_qp = datetime.datetime.strptime(qty_precip_rc_df['date_qp_rc'][0],"%Y-%m-%d") + timedelta(days = 4)
qty_precip_rc_df['times_qp_rc'] = time_delta_qp.strftime("%Y-%m-%d")
qty_precip_rc_df = qty_precip_rc_df.loc[qty_precip_rc_df['date_qp_rc'] < qty_precip_rc_df['times_qp_rc']]
qty_precip_rc_df
# qty_precip_rc_df.dtypes


rc_grid_df = pd.DataFrame({"id":2,
        "campground": "Rose Canyon",
        "forecasted_temperature_degF": temp_rc_df['degF_rc'],
        "forecastTime_temperature": temp_rc_df['date_time_temp_rc'],
        "forecasted_windSpeed_miles_per_h": windSpeed_rc_df['miles/hour_rc'],
        "forecastTime_windSpeed": windSpeed_rc_df['date_time_ws_rc'],
        "forecasted_windGust_miles_per_h": wind_gust_rc_df['m/h_rc'],
        "forecastTime_windGust": wind_gust_rc_df['date_time_wg_rc'],
        "forecasted_probabilityOfPrecipitation": prob_precip_rc_df['value'],
        "forecastTime_probabilityOfPrecipitation": prob_precip_rc_df['date_time_pp_rc'],
        "forecasted_quantityOfPrecipitation_mm": qty_precip_rc_df['value'],
        "forecastTime_quantityOfPrecipitation": qty_precip_rc_df['date_time_qp_rc'],
       })
rc_grid_df
# rc_grid_df.dtypes


# %%
# Pull metadata for Spencer Canyon Campgraound
sc_url = "https://api.weather.gov/points/32.4186,-110.7383"
response_sc = requests.get(sc_url)
data_sc = response_sc.json()
data_sc
grid_data_sc = data_sc["properties"]["forecastGridData"]
grid_data_sc


# %%
# Pull Forecast Grid data for Spencer Canyon Campground
sc_forcast_url = grid_data_sc
response_sc_forecast = requests.get(sc_forcast_url)
data_sc_forecast = response_sc_forecast.json()
data_sc_forecast

lat_sc = data_sc_forecast["geometry"]["coordinates"][0][0][1]
lat_sc
lng_sc = data_sc_forecast["geometry"]["coordinates"][0][0][0]
lng_sc
elevation_sc = data_sc_forecast["properties"]["elevation"]["value"]
elevation_sc

# Create a Dataframe for Spencer Canyon Campground
sc_df = pd.DataFrame({"id": 3,
              "campground": "Spencer Canyon",
              "lat": [lat_sc],
              "lon": [lng_sc],
              "elevation": [elevation_sc],
              "nws_meta_url": [sc_url],
              "nws_grid_url": [grid_data_sc],
              "forest_url":"https://www.fs.usda.gov/recarea/coronado/recreation/camping-cabins/recarea/?recid=25710&actid=29",
              "campsite_url": "https://www.fs.usda.gov/Internet/FSE_MEDIA/fseprd746608.jpg",
            #   "nws_meta_json":[data_sc],
            #   "nws_grid_json": [data_sc_forecast],
              "fire_danger": "Very High",
              "map_code": '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3368.0814680369876!2d-110.74302428360251!3d32.41697578108229!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x86d61515ca1f56fd%3A0x242e26b2f2f72242!2sSpencer%20Canyon%20Campground!5e0!3m2!1sen!2sus!4v1626560995515!5m2!1sen!2sus" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy"></iframe>' 
                    })
sc_df


# %%
# Pull Grid Data for Spencer Canyon CampGround
temp_sc = []
for i in data_sc_forecast["properties"]["temperature"]["values"]:
    temp_sc.append(i)
temp_sc_df = pd.DataFrame(temp_sc)
temp_sc_df
# Temperature conversion to Degree Fahrenheit
temp_sc_df['degF_sc'] = (temp_sc_df['value'] * 9 / 5) + 32
temp_sc_df

# validTime Column split to date and time for Temperature
date_temp_sc = temp_sc_df['validTime'].str.split('T', n=1, expand=True)
time_temp_sc = date_temp_sc[1].str.split('+', n=1, expand=True)
time_temp_sc
temp_sc_df['date_temp_sc'] = date_temp_sc[0]
temp_sc_df['time_temp_sc'] = time_temp_sc[0]

temp_sc_df['date_time_temp_sc'] = temp_sc_df['date_temp_sc'] + ' ' + temp_sc_df['time_temp_sc']
temp_sc_df['date_time_temp_sc'] = pd.to_datetime(temp_sc_df['date_time_temp_sc'])

# Pulling only today + 3 days worth of data
time_delta_temp_sc = datetime.datetime.strptime(temp_sc_df['date_temp_sc'][0],"%Y-%m-%d") + timedelta(days = 4)
temp_sc_df['times_temp_sc'] = time_delta_temp_sc.strftime("%Y-%m-%d")
temp_sc_df = temp_sc_df.loc[temp_sc_df['date_temp_sc'] < temp_sc_df['times_temp_sc']]
temp_sc_df
# temp_sc_df.dtypes


# ##### Pulling Wind Speed ########
wind_speed_sc = []
for i in data_sc_forecast["properties"]["windSpeed"]["values"]:
    wind_speed_sc.append(i) 
windSpeed_sc_df = pd.DataFrame(wind_speed_sc) 
windSpeed_sc_df

# Converting KM/hour to Miles/hour
windSpeed_sc_df['miles/hour_sc'] = windSpeed_sc_df['value'] * 0.621371
windSpeed_sc_df

# validTime Column split to date and time for wind Speed
date_ws_sc = windSpeed_sc_df['validTime'].str.split('T', n=1, expand=True)
time_ws_sc = date_ws_sc[1].str.split('+', n=1, expand=True)
time_ws_sc
windSpeed_sc_df['date_ws_sc'] = date_ws_sc[0]
windSpeed_sc_df['time_ws_sc'] = time_ws_sc[0]

windSpeed_sc_df['date_time_ws_sc'] = windSpeed_sc_df['date_ws_sc'] + ' ' + windSpeed_sc_df['time_ws_sc']
windSpeed_sc_df['date_time_ws_sc'] = pd.to_datetime(windSpeed_sc_df['date_time_ws_sc'])

# Pulling only today + 3 days worth of data
time_delta_ws = datetime.datetime.strptime(windSpeed_sc_df['date_ws_sc'][0],"%Y-%m-%d") + timedelta(days = 4)
windSpeed_sc_df['times_ws_sc'] = time_delta_ws.strftime("%Y-%m-%d")
windSpeed_sc_df = windSpeed_sc_df.loc[windSpeed_sc_df['date_ws_sc'] < windSpeed_sc_df['times_ws_sc']]
windSpeed_sc_df
# windSpeed_sc_df.dtypes


# ##### Pulling Wind Gusts ########
wind_gust_sc = []
for i in data_sc_forecast["properties"]["windGust"]["values"]:
    wind_gust_sc.append(i) 
wind_gust_sc_df = pd.DataFrame(wind_gust_sc) 
wind_gust_sc_df

# Converting KM/hour to Miles/hour
wind_gust_sc_df['m/h_sc'] = wind_gust_sc_df['value'] * 0.621371
wind_gust_sc_df

# # validTime Column split to date and time for wind Gusts
date_wg_sc = wind_gust_sc_df['validTime'].str.split('T', n=1, expand=True)
time_wg_sc = date_wg_sc[1].str.split('+', n=1, expand=True)
time_wg_sc
wind_gust_sc_df['date_wg_sc'] = date_wg_sc[0]
wind_gust_sc_df['time_wg_sc'] = time_wg_sc[0]

wind_gust_sc_df['date_time_wg_sc'] = wind_gust_sc_df['date_wg_sc'] + ' ' + wind_gust_sc_df['time_wg_sc']
wind_gust_sc_df['date_time_wg_sc'] = pd.to_datetime(wind_gust_sc_df['date_time_wg_sc'])
wind_gust_sc_df

# Pulling only today + 3 days worth of data
time_delta_wg = datetime.datetime.strptime(wind_gust_sc_df['date_wg_sc'][0],"%Y-%m-%d") + timedelta(days = 4)
wind_gust_sc_df['times_wg_sc'] = time_delta_wg.strftime("%Y-%m-%d")
wind_gust_sc_df = wind_gust_sc_df.loc[wind_gust_sc_df['date_wg_sc'] < wind_gust_sc_df['times_wg_sc']]
wind_gust_sc_df
# wind_gust_sc_df.dtypes

# # # ##### Pulling Probability Precipitation ########
prob_precip_sc = []
for i in data_sc_forecast["properties"]["probabilityOfPrecipitation"]["values"]:
    prob_precip_sc.append(i) 
prob_precip_sc_df = pd.DataFrame(prob_precip_sc) 
prob_precip_sc_df

# # validTime Column split to date and time for Probability Precipitation
date_pp_sc = prob_precip_sc_df['validTime'].str.split('T', n=1, expand=True)
time_pp_sc = date_pp_sc[1].str.split('+', n=1, expand=True)
time_pp_sc
prob_precip_sc_df['date_pp_sc'] = date_pp_sc[0]
prob_precip_sc_df['time_pp_sc'] = time_pp_sc[0]

prob_precip_sc_df['date_time_pp_sc'] = prob_precip_sc_df['date_pp_sc'] + ' ' + prob_precip_sc_df['time_pp_sc']
prob_precip_sc_df['date_time_pp_sc'] = pd.to_datetime(prob_precip_sc_df['date_time_pp_sc'])
prob_precip_sc_df

# Pulling only today + 3 days worth of data
time_delta_pp = datetime.datetime.strptime(prob_precip_sc_df['date_pp_sc'][0],"%Y-%m-%d") + timedelta(days = 4)
prob_precip_sc_df['times_pp_sc'] = time_delta_pp.strftime("%Y-%m-%d")
prob_precip_sc_df = prob_precip_sc_df.loc[prob_precip_sc_df['date_pp_sc'] < prob_precip_sc_df['times_pp_sc']]
prob_precip_sc_df
# prob_precip_sc_df.dtypes

# # ##### Pulling quantity Precipitation ########
qty_precip_sc = []
for i in data_sc_forecast["properties"]["quantitativePrecipitation"]["values"]:
    qty_precip_sc.append(i) 
qty_precip_sc_df = pd.DataFrame(qty_precip_sc) 
qty_precip_sc_df

# # validTime Column split to date and time for quantity Precipitation
date_qp_sc = qty_precip_sc_df['validTime'].str.split('T', n=1, expand=True)
time_qp_sc = date_qp_sc[1].str.split('+', n=1, expand=True)
time_qp_sc
qty_precip_sc_df['date_qp_sc'] = date_qp_sc[0]
qty_precip_sc_df['time_qp_sc'] = time_qp_sc[0]

qty_precip_sc_df['date_time_qp_sc'] = qty_precip_sc_df['date_qp_sc'] + ' ' + qty_precip_sc_df['time_qp_sc']
qty_precip_sc_df['date_time_qp_sc'] = pd.to_datetime(qty_precip_sc_df['date_time_qp_sc'])
qty_precip_sc_df

# Pulling only today + 3 days worth of data
time_delta_qp = datetime.datetime.strptime(qty_precip_sc_df['date_qp_sc'][0],"%Y-%m-%d") + timedelta(days = 4)
qty_precip_sc_df['times_qp_sc'] = time_delta_qp.strftime("%Y-%m-%d")
qty_precip_sc_df = qty_precip_sc_df.loc[qty_precip_sc_df['date_qp_sc'] < qty_precip_sc_df['times_qp_sc']]
qty_precip_sc_df
# qty_precip_sc_df.dtypes


sc_grid_df = pd.DataFrame({"id":3,
        "campground": "Spencer Canyon",
        "forecasted_temperature_degF": temp_sc_df['degF_sc'],
        "forecastTime_temperature": temp_sc_df['date_time_temp_sc'],
        "forecasted_windSpeed_miles_per_h": windSpeed_sc_df['miles/hour_sc'],
        "forecastTime_windSpeed": windSpeed_sc_df['date_time_ws_sc'],
        "forecasted_windGust_miles_per_h": wind_gust_sc_df['m/h_sc'],
        "forecastTime_windGust": wind_gust_sc_df['date_time_wg_sc'],
        "forecasted_probabilityOfPrecipitation": prob_precip_sc_df['value'],
        "forecastTime_probabilityOfPrecipitation": prob_precip_sc_df['date_time_pp_sc'],
        "forecasted_quantityOfPrecipitation_mm": qty_precip_sc_df['value'],
        "forecastTime_quantityOfPrecipitation": qty_precip_sc_df['date_time_qp_sc'],
       })
sc_grid_df
# # sc_grid_df.dtypes


# %%
df = pd.concat([bs_df, rc_df, sc_df])

df.to_csv('finaldf.csv')
df
# df1 = df.set_index('id')
# df1


# %%
# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
import psycopg2


from postgres_pswd import host, database, username, passwd

# Define how many sectors to display in the output of the sector analysis
output='top3'

# Create engine to mutual_funds database

engine_startup = 'postgresql://hgquoluqhpempn:1250a45ed32360cfb6492b98943bc4cd80699a8f00a1144625b3cf52b2db11c9@ec2-44-194-112-166.compute-1.amazonaws.com:5432/d3lajcergj0dej?sslmode=require'
engine = create_engine(engine_startup)

# reflect the existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# View all of the classes that automap found
Base.classes.keys()

# Create our session (link) from Python to the DB
session = Session(bind=engine)


# %%
# Create table "camp_wx"

engine.execute('DROP TABLE IF EXISTS camp_wx CASCADE; 		CREATE TABLE "camp_wx" ( 		"id" int   NOT NULL, 		"campground" varchar(255)   NOT NULL, 		"lat" float   NOT NULL, 		"lon" float   NOT NULL, 		"elevation" float   NOT NULL, 		"nws_meta_url" varchar(2000)   NOT NULL, 		"nws_grid_url" varchar(2000)   NOT NULL, 		"forest_url" varchar(2000)   NOT NULL, 		"campsite_url" varchar(2000)   NOT NULL, 		"nws_meta_json" varchar(65535)   NOT NULL, 		"nws_grid_json" varchar(65535)   NOT NULL, 		"fire_danger" varchar(50)   NOT NULL, 		"map_code" varchar(20000)   NOT NULL 	);')


# %%
# upload df to camp_wx

df.to_sql('camp_wx', engine, if_exists='replace')


# %%
# create table cg_bog_spring

engine.execute('DROP TABLE IF EXISTS cg_bog_spring CASCADE; 		CREATE TABLE "cg_bog_spring" ( 		"id" int   NOT NULL, 		"campground" varchar(255)   NOT NULL, 		"forecasted_temperature_degF" float, 		"forecastTime_temperature" date, 		"forecasted_windSpeed_miles_per_h" float, 		"forecastTime_windSpeed" date, 		"forecasted_windGust_miles_per_h" float, 		"forecastTime_windGust" date, 		"forecasted_probabilityOfPrecipitation" float, 		"forecastTime_probabilityOfPrecipitation" date, 		"forecasted_quantityOfPrecipitation_mm" float, 		"forecastTime_quantityOfPrecipitation" date 	);')


# %%
# upload bs_grid_df to cg_bog_spring

bs_grid_df.to_sql('cg_bog_spring', engine, if_exists='replace')


# %%
# create table cg_rose_canyon

engine.execute('DROP TABLE IF EXISTS cg_rose_canyon CASCADE; 		CREATE TABLE "cg_rose_canyon" ( 		"id" int   NOT NULL, 		"campground" varchar(255)   NOT NULL, 		"forecasted_temperature_degF" float, 		"forecastTime_temperature" date, 		"forecasted_windSpeed_miles_per_h" float, 		"forecastTime_windSpeed" date, 		"forecasted_windGust_miles_per_h" float, 		"forecastTime_windGust" date, 		"forecasted_probabilityOfPrecipitation" float, 		"forecastTime_probabilityOfPrecipitation" date, 		"forecasted_quantityOfPrecipitation_mm" float, 		"forecastTime_quantityOfPrecipitation" date 	);')


# %%
# upload rc_grid_df to cg_rose_canyon

rc_grid_df.to_sql('cg_rose_canyon', engine, if_exists='replace')


# %%
# create table cg_spencer_canyon
engine.execute('DROP TABLE IF EXISTS cg_spencer_canyon CASCADE; 		CREATE TABLE "cg_spencer_canyon" ( 		"id" int   NOT NULL, 		"campground" varchar(255)   NOT NULL, 		"forecasted_temperature_degF" float, 		"forecastTime_temperature" date, 		"forecasted_windSpeed_miles_per_h" float, 		"forecastTime_windSpeed" date, 		"forecasted_windGust_miles_per_h" float, 		"forecastTime_windGust" date, 		"forecasted_probabilityOfPrecipitation" float, 		"forecastTime_probabilityOfPrecipitation" date, 		"forecasted_quantityOfPrecipitation_mm" float, 		"forecastTime_quantityOfPrecipitation" date 	);')


# %%
# upload sc_grid_df to cg_spencer_canyon

sc_grid_df.to_sql('cg_spencer_canyon', engine, if_exists='replace')


