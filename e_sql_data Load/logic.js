// var queryUrl = "https://api.weather.gov/gridpoints/TWC/91,26"

// d3.json(queryUrl).then(function(data) {
//     console.log(data.geometry.coordinates[0]);
//     console.log(data.features[0].properties.time);
//     console.log(data.features[0].properties.mag);
//     // Using the features array sent back in the API data, create a GeoJSON layer and add it to the map
//     var earthquake = []
//   });

var queryUrl = "https://api.weather.gov/gridpoints/TWC/91,26";

// Perform a GET request to the query URL This is the correct formula
d3.json(queryUrl).then(function(data) {
  console.log(data.geometry.coordinates[0]);
  console.log(data.properties.elevation.value)

  // Using the features array sent back in the API data, create a GeoJSON layer and add it to the map
  
});