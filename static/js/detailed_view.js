// ####################################################
// detailed_view.js
// ----
// Anne Niemiec authored the chart definitions.
// Nicole Lund authored the json retrieval and text updates.
// ####################################################

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
            build_page(detailed_data);
        });
        break;

    case "Spencer Canyon Campground":
        d3.json("api/spencer_canyon.json").then((detailed_data) => {
            console.log('Spencer Canyon Data');
            console.log(detailed_data);
            build_page(detailed_data);
        });
        break;

    default:
        d3.json("api/bog_springs.json").then((detailed_data) => {
            console.log('Bog Springs Data');
            console.log(detailed_data);
            build_page(detailed_data);
        });
};

function build_page(data) {
    // Add data update time
    d3.select("#update_time")
        .append("p")
        .text('Last update: ' + data[1].forecastTime_temperature[0])

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
        
    // Add charts to carousel
    add_charts(data);

    // Add google map to carousel
    d3.select("#google_map")
        .append("div")
        .html(data[0].map_code);

    // Add campground image to carousel
    d3.select("#campground_image")
        .append("div")
        .html("<img src='" + data[0].campsite_url +"'>");
};

function add_charts(data) {
    var temps = data[1].forecasted_temperature_degF;
    var temp_times = data[1].forecastTime_temperature;
    var windGust = data[1].forecasted_windGust_miles_per_h;
    var windGust_times = data[1].forecastTime_windGust;
    var windSpeed = data[1].forecasted_windSpeed_miles_per_h;
    var windSpeed_times = data[1].forecastTime_windSpeed;
    var precipitation = data[1].forecasted_probabilityOfPrecipitation;
    var precip_probability = []
    for (var i=0; i<precipitation.length; i++) {
        precip_probability.push(precipitation[i]/100);
    };
    var precipitation_times = data[1].forecastTime_probabilityOfPrecipitation;
    var quantityPrecipitation = data[1].forecasted_quantityOfPrecipitation_mm;
    var quantityPrecipitation_times = data[1].forecastTime_quantityOfPrecipitation;


    // Temperature Section
    var temp_trace = {
        x: temp_times,
        y: temps,
        name: "Temperature (F)",
        mode: 'lines+markers',
        type: 'scatter'
    };
    var temp_layout = {
        title: "Forecasted Temperature",
        xaxis: {
            title: 'Date/Time',
            visible: true,
            showticklabels: true
        },
        yaxis: {
            title: 'Temperature (F)',
            visible: true,
            showticklabels: true
        }
    };
    Plotly.newPlot('temp_chart', [temp_trace], temp_layout);


    // Precipitation Section
    var precip_quantity_trace = {
        x: quantityPrecipitation_times,
        y: quantityPrecipitation,
        name: "Rainfall Quantity (mm)",
        mode: 'lines+markers',
        type: 'scatter'
    };
    var precip_prob_trace = {
        x: precipitation_times,
        y: precip_probability,
        name: "Probability of Rainfall",
        mode: 'lines+markers',
        type: 'scatter'
    };
    var precip_layout = {
        title: "Forecasted Rainfall",
        xaxis: {
            title: 'Date/Time',
            visible: true,
            showticklabels: true
        },
        yaxis: {
            title: 'Rainfall',
            visible: true,
            showticklabels: true
        }
    };
    Plotly.newPlot("precip_chart", [precip_quantity_trace, precip_prob_trace], precip_layout);
    
    
    // Windspeed Section
    var windspeed_trace = {
        x: windSpeed_times,
        y: windSpeed,
        name: "Wind Speed (mph)",
        mode: 'lines+markers',
        type: 'scatter'
    };
    var windgust_trace = {
        x: windGust_times,
        y: windGust,
        name: "Wind Gust Speed (mph)",
        mode: 'lines+markers',
        type: 'scatter'
    };
    var windspeed_layout = {
        title: "Forecasted Wind Speed",
        xaxis: {
            title: 'Date/Time',
            visible: true,
            showticklabels: true
        },
        yaxis: {
            title: 'Speed (mph)',
            visible: true,
            showticklabels: true
        }
    };
    Plotly.newPlot('wind_chart', [windspeed_trace, windgust_trace], windspeed_layout);

};


