d3.json("api/box_plot.json").then((temp_data) => {
    console.log('Box Plot Data');
    console.log(temp_data);

    var temp_summary = d3.select("#temp_summary")
    temp_summary.append("div")
        .html("<img src='https://images.squarespace-cdn.com/content/v1/558412b1e4b02581df4f2488/1530706717745-LAH7ZGN79KD01RNQUR11/box+plot+compare.png'>");
});