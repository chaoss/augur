function searchCity(){
    city = document.getElementById("cityArea").value;
    geocoder = new google.maps.Geocoder();
    console.log(city);
    geocoder.geocode( { 'address': city}, function(results, status) {
      if (status == google.maps.GeocoderStatus.OK) {
        //Got result, center the map and put it out there
        map.setCenter(results[0].geometry.location);
        map.setZoom(6);
      } else {
        alert("Geocode was not successful for the following reason: " + status);
      }
    });
    return map;
}

function codeAddress(map) {
    geocoder = new google.maps.Geocoder();
    zipCode = document.getElementById("ZIPArea").value;
    geocoder.geocode( { 'address': zipCode}, function(results, status) {
      if (status == google.maps.GeocoderStatus.OK) {
        //Got result, center the map and put it out there
        map.setCenter(results[0].geometry.location);
        map.setZoom(6);
      } else {
        alert("Geocode was not successful for the following reason: " + status);
      }
    });
    return map;
  }
