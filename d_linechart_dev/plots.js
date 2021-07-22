// Plotly stacked line charts of Temp, Winds, & Precip 
// See https://plotly.com/javascript/subplots/#stacked-subplots-with-a-shared-x-axis


// json data:
// d3.json("https://api.weather.gov/gridpoints/TWC/101,54").then(function(weather_data){console.log(weather_data)


    // Probability of Precipitation. 
        // forecasted_probabilityOfPrecipitation = result.properties.probabilityOfPrecipitation.values[i].value
        // forecastTime_probabilityOfPrecipitation = result.properties.probabilityOfPrecipitation.values[i].validTime

    // Quantity of Precipitation. 
        // forecasted_quantityOfPrecipitation_mm = result.properties.quantitativePrecipitation.values[i].value
        // forecastTime_quantityOfPrecipitation = result.properties.quantitativePrecipitation.values[i].validTime

////////////////////////////////////////////////////////
//Build query URL
d3.json("https://api.weather.gov/gridpoints/TWC/101,54").then(function(weather_data){
    console.log(weather_data)

// create variables for stacked chart
var stacked_chart=weather_data.properties
var temps=[]
var temp_times=[]
var windGust=[]
var windGust_times=[]
var windSpeed=[]
var windSpeed_times=[]

// stacked chart for temperatures
for (let index = 0; index < stacked_chart.temperature.values.length; index++) {
    const temp_GMT= stacked_chart.temperature.values[index].validTime;
    const temp_element = stacked_chart.temperature.values[index].value;
   
    temp_times.push(temp_GMT)
    temps.push(temp_element)
        
}
// // Wind chart. Convert to miles per hour if you like. Convert time to Arizona from GMT.
//stacked chart for wind gust
for (let index = 0; index < stacked_chart.windGust.values.length; index++) {
    const gust_GMT= stacked_chart.windGust.values[index].validTime;
    const gust_element= stacked_chart.windGust.values[index].value;

    windGust_times.push(gust_GMT)
    windGust.push(gust_element)
}
// // Wind chart. 
// stacked chart for wind speed
for (let index = 0; index < stacked_chart.windSpeed.values.length; index++) {
    const speed_GMT= stacked_chart.windSpeed.values[index].validTime;
    const speed_element= stacked_chart.windSpeed.values[index].value;

    windSpeed_times.push(speed_GMT)
    windSpeed.push(speed_element)
}
console.log(temps)
var trace1 = {
    x: windSpeed_times,
    y: windSpeed,
    type: 'scatter'
  };
  
  var trace2 = {
    x: windGust_times,
    y: windGust,
    xaxis: '%d %B (%a)<br>%Y',
    yaxis: 'y2',
    type: 'scatter'
  };
  
//   var trace3 = {
//     x: temp_times,
//     y: temps,
//     xaxis: '%d %B (%a)<br>%Y',
//     yaxis: 'y3',
//     type: 'line'
//   };
  
  var data = [trace1, trace2];
  
  var layout = {
  grid: {
      rows: 3,
      columns: 1,
      pattern: 'independent',
      roworder: 'bottom to top'}
  };
  
  // Plot traces (wind speed and wind gust)
  Plotly.newPlot('plot', data, layout);

  //Formatting
//   var layout = {
//     yaxis: {windSpeed},
//     yaxis2: {WindGust},
//     yaxis3: {domain: [0.66, 1]}
//   };
})

// Probability of Precipitation. 