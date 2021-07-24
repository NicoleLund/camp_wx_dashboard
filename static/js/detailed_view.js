var location_display = d3.select("#selected_campground").text();

switch(location_display) {
    case "Bog Springs Campground":
        d3.json("api/bog_springs.json").then((detailed_data) => {
            console.log('Bog Springs Data');
            console.log(detailed_data);

            build_page(detailed_data);

        });
        break;
    
    case "Rose Canyon Campground":
        d3.json("api/rose_canyon.json").then((detailed_data) => {
            console.log('Rose Canyon Data');
            console.log(detailed_data);


        });
        break;

    case "Spencer Canyon Campground":
        d3.json("api/spencer_canyon.json").then((detailed_data) => {
            console.log('Spencer Canyon Data');
            console.log(detailed_data);


        });
        break;

    default:
        d3.json("api/bog_springs.json").then((detailed_data) => {
            console.log('Bog Springs Data');
            console.log(detailed_data);


        });
};

function build_page(data) {
    // Add fire danger level
    d3.select("#fire_level")
        .append("p")
        .text(data[0].fire_danger);

    // Add forest service url
    d3.select('#forest_service')
        .append("a")
        .attr("href", data[0].forest_url)
        .attr("target", "_blank")
        .html(data[0].campground + ' Forest Service Webpage');
        
    // Add line chart to carousel
    // d3.select("#line_chart")
    //     .append("div")
    //     .html("<img src='https://pandas.pydata.org/pandas-docs/stable/_images/frame_plot_subplots.png'>");
    line_chart(data);

    // Add google map to carousel
    d3.select("#google_map")
        .append("div")
        .html(data[0].map_code);

    // Add campground image to carousel
    d3.select("#campground_image")
        .append("div")
        .html("<img src='" + data[0].campsite_url +"'>");
};

function line_chart(data) {
    var temps = data[1].forecasted_temperature_degF
    var temp_times = data[1].forecastTime_temperature
    var windGust = data[1].forecasted_windGust_miles_per_h
    var windGust_times = data[1].forecastTime_windGust
    var windSpeed = data[1].forecasted_windSpeed_miles_per_h
    var windSpeed_times = data[1].forecastTime_windSpeed
    var precipitation = data[1].forecasted_probabilityOfPrecipitation
    var precipitation_times = data[1].forecastTime_probabilityOfPrecipitation
    var quantityPrecipitation = data[1].forecasted_quantityOfPrecipitation_mm
    var quantityPrecipitation_times = data[1].forecastTime_quantityOfPrecipitation

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
      Plotly.newPlot('line_chart', data, layout);

}
