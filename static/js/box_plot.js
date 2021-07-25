// ####################################################
// box_plot.js
// ----
// Anne Niemiec authored the chart definitions.
// Nicole Lund authored the json retrieval and text updates.
// ####################################################

d3.json("api/box_plot.json").then((temp_data) => {
    console.log('Box Plot Data');
    console.log(temp_data);

    //Create temperature box plot
    var y0 = temp_data[0].bog_springs_temp; 
    // console.log(y0)
    var y1 = temp_data[0].rose_canyon_temp;
    // console.log(y1)
    var y2 = temp_data[0].spencer_canyon_temp; 
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
    var data = [trace1,trace2,trace3];

    var layout = {
      title: '3-Day Forecasted Temperature Range',
      showlegend: false,
      xaxis: {
        title: 'Campground'
      },
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
    
    Plotly.newPlot('temp_summary', data, layout);
  
});