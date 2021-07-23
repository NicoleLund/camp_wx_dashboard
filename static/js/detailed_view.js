var location_display = d3.select("#selected_campground").text();

switch(location_display) {
    case "Bog Springs Campground":
        d3.json("api/bog_springs.json").then((detailed_data) => {
            console.log('Bog Springs Data')
            console.log(detailed_data);


        });
        break;
    
    case "Rose Canyon Campground":
        d3.json("api/rose_canyon.json").then((detailed_data) => {
            console.log('Rose Canyon Data')
            console.log(detailed_data);


        });
        break;

    case "Spencer Canyon Campground":
        d3.json("api/spencer_canyon.json").then((detailed_data) => {
            console.log('Spencer Canyon Data')
            console.log(detailed_data);


        });
        break;

    default:
        d3.json("api/bog_springs.json").then((detailed_data) => {
            console.log('Bog Springs Data')
            console.log(detailed_data);


        });
};