// ####################################################
// box_plot.js
// ----
// Anne Niemiec authored the temperature chart.
// Nicole Lund authored the precip chart.
// ####################################################

d3.json("api/box_plot.json").then((data) => {
    console.log('Box Plot Data');
    console.log(data);

    //Create temperature box plot
    var y0 = data[0].bog_springs_temp; 
    // console.log(y0)
    var y1 = data[0].rose_canyon_temp;
    // console.log(y1)
    var y2 = data[0].spencer_canyon_temp; 
    // console.log(y2) 

    var trace1 = {
      y: y0,
      name: "Bog Springs",
      type: 'box'
    };
    var trace2 = {
        y: y1,
        name: "Rose Canyon",
        type: 'box'
    };
      var trace3 = {
        y: y2,
        name: "Spencer Canyon",
        type: 'box'
    };
    var temp_data = [trace1,trace2,trace3];

    var temp_layout = {
      title: '3-Day Forecasted Temperature Range',
      showlegend: false,
      yaxis: {
        title: 'Temperature (F)',
        range: [30,100]
      },
      shapes: [
        {
          type: 'line',
          xref: 'paper',
          x0: 0,
          y0: 40,
          x1: 1,
          y1: 40,
          line: {
            color: 'blue',
            width: 2
          }
        },
        {
          type: 'line',
          xref: 'paper',
          x0: 0,
          y0: 90,
          x1: 1,
          y1: 90,
          line: {
            color: 'red',
            width: 2
          }
        }
      ]
    }
    
    Plotly.newPlot('temp_summary', temp_data, temp_layout);
  

    // Create Precip Summary Plot
    var bg_forecast_precip = data[0].bog_springs_precip;
    var bg_total_precip = 0;
    for (var i=0; i<bg_forecast_precip.length; i++) {
      bg_total_precip += bg_forecast_precip[i];
    };

    var rc_forecast_precip = data[0].rose_canyon_precip;
    var rc_total_precip = 0;
    for (var i=0; i<rc_forecast_precip.length; i++) {
      rc_total_precip += rc_forecast_precip[i];
    };
    
    var sc_forecast_precip = data[0].spencer_canyon_precip;
    var sc_total_precip = 0;
    for (var i=0; i<sc_forecast_precip.length; i++) {
      sc_total_precip += sc_forecast_precip[i];
    };

    var rain_total = [bg_total_precip, rc_total_precip, sc_total_precip];
    var campground_name = ['Bog Springs', 'Rose Canyon', 'Spencer Canyon'];

    var rain_trace = {
      x: campground_name,
      y: rain_total,
      type: 'bar'
    }

    var rain_layout = {
      title: "Predicted 3-day Rainfall Amount",
      yaxis: {
        title: 'Rainfall (mm)',
        range: [0, Math.max(...rain_total) + 20]
      },
      shapes: [
        {
          type: 'line',
          xref: 'paper',
          x0: 0,
          y0: 10,
          x1: 1,
          y1: 10,
          line: {
            color: 'red',
            width: 2
          }
        }
      ]
    }

    Plotly.newPlot('precip_summary', [rain_trace], rain_layout);

});