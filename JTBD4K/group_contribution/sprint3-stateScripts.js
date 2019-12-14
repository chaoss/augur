function moveToLocation(lat, lng, map){
    console.log("This is called!");
    center = new google.maps.LatLng(lat, lng);
    map.panTo(center);
    map.setZoom(6);
    return map;
}


function statePass(state, map){
    console.log(map);
    switch(state){
        case "Alabama":
            map = moveToLocation(32, -86, map);
            break;
        case "Alaska":
            map = moveToLocation(64, -152, map);
            break;
        case "Arizona":
            map = moveToLocation(34, -111, map);
            break;
        case "Arkansas":
            map = moveToLocation(35, -92, map);
            break;
        case "California":
            map = moveToLocation(38, -119, map);
            break;
        case "Colorado":
            map = moveToLocation(39, -105, map);
            break;
        case "Connecticut":
            map = moveToLocation(41.5, -72.7, map);
            break;
        case "Delaware":
            map = moveToLocation(39.3, -75.5, map);
            break;
        case "Florida":
            map = moveToLocation(27.7, -81.6, map);
            break;
        case "Georgia":
            map = moveToLocation(33.0, -83.6, map);
            break;
        case "Idaho":
            map = moveToLocation(44.2, -114.4, map);
            break;
        case "Illinois":
            map = moveToLocation(40.3, -88.9, map);
            break;
        case "Indiana":
            map = moveToLocation(39.8, -86.2, map);
            break;
        case "Iowa":
            map = moveToLocation(42.0, -93.2, map);
            break;
        case "Kansas":
            map = moveToLocation(38.5, -96.7, map);
            break;
        case "Kentucky":
            map = moveToLocation(37.6, -84.6)
            break;
        case "Louisiana":
            map = moveToLocation(31.1, -91.8, map);
            break;
        case "Maine":
            map = moveToLocation(44.7, -69.4, map);
            break;
        case "Maryland":
            map = moveToLocation(39.1, -76.8, map);
            break;
        case "Massachusetts":
            map = moveToLocation(42.2, -71.5, map);
            break;
        case "Michigan":
            map = moveToLocation(43.3, -84.5, map);
            break;
        case "Minnesota":
            map = moveToLocation(45.7, -93.9, map);
            break;
        case "Mississippi":
            map = moveToLocation(32.7, -89.7, map);
            break;
        case "Missouri":
            map = moveToLocation(38.5, -92.2, map);
            break;
        case "Montana":
            map = moveToLocation(46.9, -110.4, map);
            break;
        case "Nebraska":
            map = moveToLocation(41.1, -98.2, map);
            break;
        case "Nevada":
            map = moveToLocation(38.3, -117.1, map);
            break;
        case "New Hampshire":
            map = moveToLocation(43.5, -71.5, map);
            break;
        case "New Jersey":
            map = moveToLocation(40.3, -74.5, map);
            break;
        case "New Mexico":
            map = moveToLocation(34.8, -106.2, map);
            break;
        case "New York":
            map = moveToLocation(42.2, -74.9, map);
            break;
        case "North Carolina":
            map = moveToLocation(35.6, -79.8, map);
            break;
        case "North Dakota":
            map = moveToLocation(47.5, -99.7, map);
            break;
        case "Ohio":
            map = moveToLocation(40.4, -82.8, map);
            break;
        case "Oklahoma":
            map = moveToLocation(35.5, -96.9, map);
            break;
        case "Oregon":
            map = moveToLocation(44.5, -122.1, map);
            break;
        case "Pennsylvania":
            map = moveToLocation(40.6, -77.2, map);
            break;
        case "Rhode Island":
            map = moveToLocation(41.7, -71.5, map);
            break;
        case "South Carolina":
            map = moveToLocation(33.9, -80.9, map);
            break;
        case "South Dakota":
            map = moveToLocation(44.3, -99.4, map);
            break;
        case "Tennessee":
            map = moveToLocation(35.7, -86.7, map);
            break;
        case "Texas":
            map = moveToLocation(31.1, -97.6, map);
            break;
        case "Utah":
            map = moveToLocation(40.2, -111.9, map);
            break;
        case "Vermont":
            map = moveToLocation(44.0, -72.7, map);
            break;
        case "Virginia":
            map = moveToLocation(37.8, -78.2, map);
            break;
        case "Washington":
            map = moveToLocation(47.4, -121.5, map);
            break;
        case "West Virginia":
            map = moveToLocation(38.5, -81.0, map);
            break;
        case "Wisconsin":
            map = moveToLocation(44.3, -90.0, map);
            break;
        case "Wyoming":
            map = moveToLocation(42.8, -107.3, map);
            break;
        default: "That state doesnt exist!!"; 
    } 
    return map;   
}
