// Plotly box plot of all forecasted temperatures for each campground 
// See https://plotly.com/javascript/box-plots/

//Save config information
const url = "http://api.openweathermap.org/data/2.5/weather?"
const units = "metric"

//Build query URL
//Create a variable for lat and lon for drop down box
var lat=31.7276
var lon=-110.8754

//Need to revisit API_KEY!!
const query_url = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${"9ca576dc7d5026950320de9f12287dfb"}&units=metric`

d3.json(query_url).then(function(weather_data){
    console.log(weather_data)

//Create box plot
///Should these be in separate graphs due to the disparity in the ticker values?
    var y0 = [weather_data.main.temp_max, weather_data.main.temp_min, weather_data.main.temp];
    var y1 = [weather_data.wind.gust, weather_data.wind.speed];      
    var trace1 = {
      y: y0,
      type: 'box'
    };
    var trace2 = {
        y: y1,
        type: 'box'
      };
  
    var data = [trace1,trace2];
    
    Plotly.newPlot('plot', data);
    
})
