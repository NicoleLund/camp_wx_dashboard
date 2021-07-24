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
        name: "Wind Speed (mph)",
        mode: 'lines+markers',
        type: 'scatter',
        scene: "scene1"
    };
      
    var trace2 = {
        x: windGust_times,
        y: windGust,
        name: "Windgust (mph)",
        xaxis: 'x2',
        yaxis: 'y2',
        mode: 'lines+markers',
        type: 'scatter',
        scene: "scene2"
    };
      
    var trace3 = {
        x: temp_times,
        y: temps,
        name: "Temperature (F)",
        xaxis: 'x3',
        yaxis: 'y3',
        mode: 'lines+markers',
        type: 'scatter',
        scene: "scene3"
    };

    var trace4 = {
        x: precipitation_times,
        y: precipitation,
        name: "Probability of Rain (%)",
        xaxis: 'x4',
        yaxis: 'y4',
        mode: 'lines+markers',
        type: 'scatter',
        scene: "scene4"
    };
      
    var trace5 = {
        x: quantityPrecipitation_times,
        y: quantityPrecipitation,
        name: "Predicted Rainfall Amount (mm)",
        xaxis: 'x5',
        yaxis: 'y5',
        mode: 'lines+markers',
        type: 'scatter',
        scene: "scene5"
        
    };

    //Formatting
       
    var data_traces = [trace1, trace2,trace3,trace4,trace5];
      
    var layout = {
        // grid: {
        //   rows: 5,
        //   columns: 1,
        //   pattern: 'independent',
        //   roworder: 'bottom to top'},
        // title: "ABC",
        scene1: {
            domain: {
                x: [0.0, 1.0],
                y: [0.8,1.0]
            },
            xaxis: {
                title: 'x-label',
                visible: true,
                showticklabels: false
            },
            yaxis: {
                title: 'y-label',
                visible: true,
                showticklabels: true
            }
        },
        scene2: {
            domain: {
                x: [0.0, 1.0],
                y: [0.6,0.8]
            },
            xaxis: {
                title: 'x-label',
                visible: true,
                showticklabels: false
            },
            yaxis: {
                title: 'y-label',
                visible: true,
                showticklabels: true
            }
        },
        scene3: {
            domain: {
                x: [0.0, 1.0],
                y: [0.4,0.6]
            },
            xaxis: {
                title: 'x-label',
                visible: true,
                showticklabels: false
            },
            yaxis: {
                title: 'y-label',
                visible: true,
                showticklabels: true
            }
        },
        scene4: {
            domain: {
                x: [0.0, 1.0],
                y: [0.2,0.4]
            },
            xaxis: {
                title: 'x-label',
                visible: true,
                showticklabels: false
            },
            yaxis: {
                title: 'y-label',
                visible: true,
                showticklabels: true
            }
        },
        scene5: {
            domain: {
                x: [0.0, 1.0],
                y: [0.0,0.2]
            },
            xaxis: {
                title: 'x-label',
                visible: true,
                showticklabels: false
            },
            yaxis: {
                title: 'y-label',
                visible: true,
                showticklabels: true
            }
        }
        // xaxis: {
        //     nticks: 20,
        //     title: "Shared Date"
        // },
        // yaxis1: {
        //     // scaleanchor: "x",
        //     legendtitle: "Windspeed (mph)"
        // },
        // yaxis2: {
        //     // scaleanchor: "x",
        //     legendtitle: "Windgust (mph)"
        // },
        // yaxis3: {
        //     // scaleanchor: "x",
        //     legendtitle: "Temperature (F)"
        // },
        // yaxis4:{
        //     // scaleanchor: "x",
        //     legendtitle: "Probability of Rain (%)"
        // },
        // yaxis5:{
        //     // scaleanchor: "x",
        //     legendtitle: "Predicted Rainfall Amount (mm)"
        // }
        // showlegend: true
    }
    // fig = go.Figure(data=data, layout=layout)
    // // plotly.offline.plot(fig, filename=str(DateDebut) +" a "+ str(DateFin) + ".csv", auto_open=true)
    // fig = plotly.tools.make_subplots(rows=5, cols=1, shared_xaxes=true)

    // Plot traces 
    Plotly.newPlot('line_chart', data_traces, layout);
};


