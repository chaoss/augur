//FUNCTIONS FOR MAIN PAGE (PLACE PINS & DISPLAY STATISTICS INFO)
//PARSES THROUGH INPUT AND PROVIDES COUNT FOR "STATISTICS" REFERENCES ON MAIN PAGE


//function to parse data for repo group 10
var request = new XMLHttpRequest();
request.open('GET', 'http://129.114.104.67:5000/api/unstable/repo-groups/20/committers-locations', true);
var count = 0;

request.onload = function() {
    
    //parse
    var data = JSON.parse(this.response);

    //if you have a valid request
    if(request.status >= 200 && request.status < 400) {
        //for every repo
        data.forEach(repo => {
            //count the number of repos
            count++;
        });
    }
    //this is logging the number of repos not contributors
    console.log(count);
    document.getElementById("contributorText").textContent = "Repo Group 10: " + count + " contributors";
}
console.log(count);


//function to parse data for repo group 20
var count2 = 0;
var request2 = new XMLHttpRequest();
request2.open('GET', 'http://129.114.104.67:5000/api/unstable/repo-groups/10/committers-locations', true);

request2.onload = function() {

    //parse
    var data = JSON.parse(this.response);

    //if you have a valid request
    if(request2.status >= 200 && request2.status < 400) {
        //for every repo
        data.forEach(repo => {
            //count the number of repos
            count2++;
        });
    }
    //this is logging the number of repos not contributors
    console.log(count2);
    document.getElementById("contributorText2").textContent = "Repo Group 20: " + count2 + " contributors";
}

//document.getElementById("contributorText").textContent = count + count2;

request.send()
request2.send()






//PLACES THE PINS ON THE MAP FOR ENDPOINTS FOR REPO GROUP 10 AND GROUP 20
var markersArray = [];
var marker;

//pie chart variables
    var west = 0; 
    var midwest = 0; 
    var south = 0; 
    var northeast = 0; 

function placePinByRepo(mapInstance, value, infowindow){
    
    var xmlHttp = new XMLHttpRequest();
    var i=0;
    xmlHttp.onload = function(){
        if(xmlHttp.status == 200 && xmlHttp.readyState == 4){
              
            //parse through responses
            var response = xmlHttp.responseText;
            response = JSON.parse(response);
            
            var locationArray = JSON.parse(this.responseText);
			locationArray.forEach(function(contributor) {
                
                //save latitude and longitude into variables
                var latitude = contributor.cntrb_lat;
                var longitude = contributor.cntrb_long;
                var email = contributor.cntrb_email;
                var city = contributor.cntrb_city;
                var myLatLng = {lat: latitude, lng: longitude};
                var state = contributor.cntrb_state;
                
                
                //count repos in each region
                if(state=="AL" || state=="AZ" || state=="CA" || state=="CO" || state=="HI" || state=="ID" || state=="MT" || state=="NV" || state=="NM" || state=="OR" || state=="UT" || state=="WA" || state=="WY") {
                    west++;
                }
                
                if(state=="IL" || state=="IN" || state=="IA" || state=="KS" || state=="MI" || state=="MO" || state=="MN" || state=="NE" || state=="ND" || state=="OH" || state=="SD" || state=="WI") {
                    midwest++;
                }

                if(state=="AL" || state=="AR" || state=="DE" || state=="FL" || state=="GA" || state=="KY" || state=="LA" || state=="MD" || state=="MS" || state=="OK" || state=="NC" || state=="SC" || state=="TN" || state=="TX" || state=="VA" || state=="WV") {
                    south++;
                }
                
                if(state=="CT" || state=="ME" || state=="NH" || state=="MA" || state=="NJ" || state=="NY" || state=="PA" || state=="RI" || state=="VT") {
                    northeast++;
                }

                city = city.toString();
                email = email.toString();
                
                marker = new google.maps.Marker({
                    position: myLatLng,
                    map: mapInstance,
                    title: "title",
                    animation: google.maps.Animation.DROP,
                    email: email,
                    city: city
                });
                markersArray.push(marker);
                
                google.maps.event.addListener(marker, 'click', function(res){
                    latitude = res.latLng.lat();
                    longitude = res.latLng.lng();
                    for(i = 0; i < markersArray.length; i++){
                        currentMark = markersArray[i];
                        currentLat = currentMark.internalPosition.lat();
                        currentLon = currentMark.internalPosition.lng();
                        if(latitude == currentLat && longitude == currentLon){
                            console.log(currentMark);
                            infowindow.setContent("Email: " + currentMark.email + "<br/>" + "City: " + currentMark.city);
                            infowindow.open(mapInstance, this);
                        }
                    }
                });
			});
            
            
            
            google.charts.load('current', {'packages':['corechart']});
            google.charts.setOnLoadCallback(drawChart);

            // Draw the chart and set the chart values
            function drawChart() {
                var data = google.visualization.arrayToDataTable([
                    ['Region', 'Contributors'],
                    ['West', west],
                    ['Midwest', midwest],
                    ['South', south],
                    ['Northeast', northeast]
                ])

            // Optional; add a title and set the width and height of the chart
            var options = {
                title:'Contributor Statistics By Region For Group ' + value, 
                width: 775, 
                height:400,
                colors: ['lightblue', 'darkblue', 'green', 'lightgreen', 'darkblue', 'yellow'],
                is3D: true,
                slices: {  1: {offset: 0.05},
                    2: {offset: 0.05},
                    3: {offset: 0.05},
                    4: {offset: 0.05},
                },
            };

                //draw pie chart
                var chart = new google.visualization.PieChart(document.getElementById('piechart'));
                chart.draw(data, options);                
            }    
            
            //DO THESE PER REPO GROUP
            if(west > south && west > northeast && west > midwest) {
                document.getElementById("regionText").innerHTML = "West";
            }
            
            if(south > west && south > northeast && south > midwest) {
                document.getElementById("regionText").innerHTML = "South";
            }
            
            if(midwest > west && midwest > northeast && midwest > south) {
                document.getElementById("regionText").innerHTML = "Midwest";
            }
            
            if(northeast > south && northeast > west && northeast > midwest) {
                document.getElementById("regionText").innerHTML = "Northeast";
            }
            
            console.log(markersArray);
        }
    }
    
    var reqURL = "http://129.114.104.67:5000/api/unstable/repo-groups/" + value + "/committers-locations";
    xmlHttp.open("GET", reqURL, true);
    xmlHttp.send();
}


function placePinDropDown(mapInstance, value){
    var xmlHttp = new XMLHttpRequest();
    for (i = 0; i<markersArray.length; i++){
        var oldMarker = markersArray.pop();
        oldMarker.setMap(null);
    }
    xmlHttp.onload = function(){
        
        if(xmlHttp.status == 200 && xmlHttp.readyState == 4){
                        
            var response = xmlHttp.responseText;
            response = JSON.parse(response);
            
            var locationArray = JSON.parse(this.responseText);
			locationArray.forEach(function(contributor) {
                var latitude = contributor.cntrb_lat;
                var longitude = contributor.cntrb_long;
                
                var myLatLng = {lat: latitude, lng: longitude};
                
                marker = new google.maps.Marker({
                    position: myLatLng,
                    map: mapInstance,
                    title: "title",
                    animation: google.maps.Animation.DROP
                });	
                markersArray.push(marker);
			});
        }
        console.log(markersArray);

    }
    
    var reqURL = "http://129.114.104.67:5000/api/unstable/repo-groups/" + value + "/committers-locations";
    xmlHttp.open("GET", reqURL, true);
    xmlHttp.send();
}
