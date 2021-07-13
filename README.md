# camp_wx_dashboard

### Data Sources
* National Weather Service API: <a href="https://www.weather.gov/documentation/services-web-api" target="_blank">https://www.weather.gov/documentation/services-web-api</a>
* National Weather Service API usage: <a href="https://weather-gov.github.io/api/" target="_blank">https://weather-gov.github.io/api/</a>
* Find Latitude/Longitude for Addresses: <a href="https://www.latlong.net/convert-address-to-lat-long.html" target="_blank">https://www.latlong.net/convert-address-to-lat-long.html</a>
* Whitetail Campground (11200 N., Whitetail Rd, Mt Lemmon, AZ 85619): 
    * **Point metadata:** <a href="https://api.weather.gov/points/32.4128,-110.7313" target="_blank">https://api.weather.gov/points/32.4128,-110.7313</a>
    * **Forecast grid data (detailed data organized by arrays of measurements rather than time objects):** <a href="https://api.weather.gov/gridpoints/TWC/100,55" target="_blank">https://api.weather.gov/gridpoints/TWC/100,55</a>
* Show Low Lake Campground (5800 Show Low Lake Rd, Lakeside, AZ 85929)
* Crescent Moon Ranch (300 Red Rock Crossing Rd, Sedona, AZ 86336)
* Indian Garden Campground (Bright Angel Trail, Grand Canyon Village, AZ 86023)
* Madera Canyon (S Madera Canyon Rd, Amado, AZ 85645)

### Technologies
* Underlying Components
    * Python Flask (similar to Mars webscraping challenge)
    * postgreSQL database (similar to Mars webscraping challenge)
* Visible Dashboard
    * Button to update database (similar to Mars webscraping)
    * Plotly box plot of all forecasted temperatures for each campground (<a href="https://plotly.com/javascript/box-plots/" target="_blank">https://plotly.com/javascript/box-plots/</a>)
    * single item slick carousel of Campground detailed forecasts as stacked line charts of Temp, Winds, & Precip similar to NWS hourly graph (<a href="https://kenwheeler.github.io/slick/" target="_blank">https://kenwheeler.github.io/slick/</a>)
    * 
### Sample Layout
![sample](sample_layout.png)
