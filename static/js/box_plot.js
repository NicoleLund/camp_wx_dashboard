d3.json("api/box_plot.json").then((temp_data) => {
    console.log('Box Plot Data');
    console.log(temp_data);

    var temp_summary = d3.select("#temp_summary")
    temp_summary.append("div")
        .html("<img src='http://www.stat.yale.edu/Courses/1997-98/101/boxplot.gif'>");
});