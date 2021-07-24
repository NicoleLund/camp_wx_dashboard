//Build query URL & d3.json
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
var precipitation=[]
var precipitation_times=[]
var quantityPrecipitation=[]
var quantityPrecipitation_times=[]

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
    // xaxis: '%d %B (%a)<br>%Y',
    mode: 'lines+markers',
    type: 'scatter'
  };
  
  var trace2 = {
    x: windGust_times,
    y: windGust,
    xaxis: 'x2',
    yaxis: 'y2',
    mode: 'lines+markers',
    type: 'scatter'
  };
  
  var trace3 = {
    x: temp_times,
    y: temps,
    xaxis: 'x3',
    yaxis: 'y3',
    mode: 'lines+markers',
    type: 'scatter'
  };
  
  // var data = [trace1, trace2];
  
  // var layout = {
  // grid: {
  //     rows: 2,
  //     columns: 1,
  //     pattern: 'independent',
  //     roworder: 'bottom to top'}
  // };
  
  // Plot traces (wind speed and wind gust)
  // Plotly.newPlot('plot', data, layout);

  //Formatting
//   var layout = {
//     yaxis: {windSpeed},
//     yaxis2: {WindGust},
//     yaxis3: {domain: [0.66, 1]}
//   };

// Probability of Precipitation. 
// stacked chart for Precipitation
for (let index = 0; index < stacked_chart.probabilityOfPrecipitation.values.length; index++) {
  const precipitation_GMT= stacked_chart.probabilityOfPrecipitation.values[index].validTime;
  const precipitation_element = stacked_chart.probabilityOfPrecipitation.values[index].value;
 
  precipitation_times.push(precipitation_GMT)
  precipitation.push(precipitation_element)
      
}

//stacked chart for quantity of precipitation
for (let index = 0; index < stacked_chart.quantitativePrecipitation.values.length; index++) {
  const quantityPrecipitation_GMT= stacked_chart.quantitativePrecipitation.values[index].validTime;
  const quantityPrecipitation_element= stacked_chart.quantitativePrecipitation.values[index].value;

  quantityPrecipitation_times.push(quantityPrecipitation_GMT)
  quantityPrecipitation.push(quantityPrecipitation_element)
}
console.log(temps)
var trace4 = {
  x: precipitation_times,
  y: precipitation,
  xaxis: 'x4',
  yaxis: 'y4',
  mode: 'lines+markers',
  type: 'scatter'
};

var trace5 = {
  x: quantityPrecipitation_times,
  y: quantityPrecipitation,
  xaxis: 'x5',
  yaxis: 'y5',
  mode: 'lines+markers',
  type: 'scatter'
  
};

var data = [trace1, trace2,trace3,trace4,trace5];

var layout = {
grid: {
    rows: 5,
    columns: 1,
    pattern: 'independent',
    roworder: 'bottom to top'}
};

// Plot traces (probability and quantity of precipitation)
Plotly.newPlot('plot', data, layout);

})


