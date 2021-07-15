// Plotly stacked line charts of Temp, Winds, & Precip 
// See https://plotly.com/javascript/subplots/#stacked-subplots-with-a-shared-x-axis


// json data:
var whitetail_url = "https://api.weather.gov/gridpoints/TWC/100,55"
    // Temperature chart. Convert temperature to Farenheit. Convert time to Arizona from GMT.
        // forecasted_temperature_degC = result.properties.temperature.values[i].value
        // forecastTime_temperature = result.properties.temperature.values[i].validTime

    // Wind chart. Convert to miles per hour if you like. Convert time to Arizona from GMT.
        // forecasted_windSpeed_km_per_h = result.properties.windSpeed.values[i].value
        // forecastTime_windSpeed = result.properties.windSpeed.values[i].validTime

        // forecasted_windGust_km_per_h = result.properties.windGust.values[i].value
        // forecastTime_windGust = result.properties.windGust.values[i].validTime

    // Probability of Precipitation. Convert time to Arizona from GMT.
        // forecasted_probabilityOfPrecipitation = result.properties.probabilityOfPrecipitation.values[i].value
        // forecastTime_probabilityOfPrecipitation = result.properties.probabilityOfPrecipitation.values[i].validTime

    // Quantity of Precipitation. Convert to inches. Convert time to Arizona from GMT.
        // forecasted_quantityOfPrecipitation_mm = result.properties.quantitativePrecipitation.values[i].value
        // forecastTime_quantityOfPrecipitation = result.properties.quantitativePrecipitation.values[i].validTime

