d3.json("api/box_plot.json").then((temp_data) => {
    console.log('Box Plot Data');
    console.log(temp_data);

//Create box plot
///Should these be in separate graphs due to the disparity in the ticker values?
    
    var y0 = temp_data[0].bog_springs_temp; 
    console.log(y0)
    var y1 = temp_data[0].rose_canyon_temp;
    console.log(y1)
    var y2 = temp_data[0].spencer_canyon_temp; 
    console.log(y2) 

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
    
    Plotly.newPlot('temp_summary', data);
    
    //  Labels and Ticks
    // boxplot(temp_summary)
    //     at = c(1,2,4,5),
    //     las = 2,
    //     col = c("orange","red"),
    //     border = "brown",
    //     horizontal = TRUE,

    //     notch = TRUE
    //     )
});