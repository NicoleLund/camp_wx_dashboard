// Plotly stacked line charts of Temp, Winds, & Precip 
// See https://plotly.com/javascript/subplots/#stacked-subplots-with-a-shared-x-axis


// json data:
// d3.json("https://api.weather.gov/gridpoints/TWC/101,54").then(function(weather_data){
//     console.log(weather_data)

// // Wind chart. 
// var windSpeed=[]
// var windSpeed_times=[]


// // stacked chart for wind speed
// for (let index = 0; index < stacked_chart.windSpeed.values.length; index++) {
//     const forecasted_windSpeed_km_per_h = result.properties.windSpeed.values[i].value;
//     const forecastTime_windSpeed = result.properties.windSpeed.values[i].validTime

//     windSpeed_times.push(forecasted_windSpeed_km_per_h)
//     windSpeed.push(forecastTime_windSpeed)
// }
// console.log(temps)
// var trace1 = {
//     x: windSpeed_times,
//     y: windSpeed,
//     type: 'line'
//   };

// //stacked chart for wind gust
// var windGust=[]
// var windGust_times=[]

// for (let index = 0; index < stacked_chart.windGust.values.length; index++) {
//     const forecasted_windGust_km_per_h = result.properties.windGust.values[i].value;
//     const forecastTime_windGust = result.properties.windGust.values[i].validTime;

//     windGust_times.push(forecasted_windGust_km_per_h)
//     windGust.push(forecastTime_windGust)
// }

// var trace2 = {
//     x: windGust_times,
//     y: windGust,
//     xaxis: 'x2',
//     yaxis: 'y2',
//     type: 'line'
//   };

//   var data = [trace1, trace2];
  
//   var layout = {
//   grid: {
//       rows: 3,
//       columns: 1,
//       pattern: 'independent',
//       roworder: 'bottom to top'}
//   };
  
//   // Plot traces (wind speed and wind gust)
//   Plotly.newPlot('plot', data, layout);
// })

    // Probability of Precipitation. 
        // forecasted_probabilityOfPrecipitation = result.properties.probabilityOfPrecipitation.values[i].value
        // forecastTime_probabilityOfPrecipitation = result.properties.probabilityOfPrecipitation.values[i].validTime

    // Quantity of Precipitation. 
        // forecasted_quantityOfPrecipitation_mm = result.properties.quantitativePrecipitation.values[i].value
        // forecastTime_quantityOfPrecipitation = result.properties.quantitativePrecipitation.values[i].validTime


// Create a variable for lat and lon for drop down box
// var lat=31.7276
// var lon=-110.8754

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
// stacked chard for wind speed
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
    type: 'line'
  };
  
  var trace2 = {
    x: windGust_times,
    y: windGust,
    xaxis: 'x2',
    yaxis: 'y2',
    type: 'line'
  };
  
  var trace3 = {
    x: temp_times,
    y: temps,
    xaxis: 'x3',
    yaxis: 'y3',
    type: 'line'
  };
  
  var data = [trace1, trace2, trace3];
  
  var layout = {
  grid: {
      rows: 3,
      columns: 1,
      pattern: 'independent',
      roworder: 'bottom to top'}
  };
  
  // Plot traces (temperatures, wind speed and wind gust)
  Plotly.newPlot('plot', data, layout);
})

// Probability of Precipitation. 