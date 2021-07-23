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
    d3.select("#line_chart")
        .append("div")
        .html("<img src='https://pandas.pydata.org/pandas-docs/stable/_images/frame_plot_subplots.png'>");
        
    // Add google map to carousel
    d3.select("#google_map")
        .append("div")
        .html(data[0].map_code);
};