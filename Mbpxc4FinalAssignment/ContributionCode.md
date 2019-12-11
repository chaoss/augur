//ALONG WITH SOME HELP WITH THE ENDPOINTS, THIS IS THE CODE THAT I CONTRIBUTED TO THE GROUP.  THIS INVOLVES THE FUNCTION TO DROP THE PINS ON THE GOOGLE MAPS MAP AS WELL AS DISPLAYING THE NUMBER OF CONTRIBUTORS, ISSUERS, AND PULL REQUESTS FOR EACH REPO GROUP.

//FUNCTIONS FOR MAIN PAGE (PLACE PINS & DISPLAY STATISTICS INFO)

//PARSES THROUGH INPUT AND PROVIDES COUNT FOR "STATISTICS" REFERENCES ON MAIN PAGE
//calls endpoints
//gathers the count for the TOTAL COMMITTERS in GROUP 20
var request20Committers = new XMLHttpRequest();
request20Committers.open('GET', 'http://129.114.104.67:5000/api/unstable/repo-groups/20/committers-locations', true);
var group20CommittersCount = 0;

//function to parse data
request20Committers.onload = function() {
    
    //parse
    var data = JSON.parse(this.response);

    //if you have a valid request
    if(request20Committers.status >= 200 && request20Committers.status < 400) {
        //for every repo
        data.forEach(repo => {
            //count the number of repos
            group20CommittersCount++;
        });
    }
    //this is logging the number of repos not contributors
    console.log(group20CommittersCount);
    document.getElementById("contributorTextGroup20").textContent = "Repo Group 20: " + group20CommittersCount + " contributors";
}
console.log(group20CommittersCount);

//gathers the count for the TOTAL COMMITTERS in GROUP 10
var group10CommittersCount = 0;
var request10Committers = new XMLHttpRequest();
request10Committers.open('GET', 'http://129.114.104.67:5000/api/unstable/repo-groups/10/committers-locations', true);

//function to parse data
request10Committers.onload = function() {

    //parse
    var data = JSON.parse(this.response);

    //if you have a valid request
    if(request10Committers.status >= 200 && request10Committers.status < 400) {
        //for every repo
        data.forEach(repo => {
            //count the number of repos
            group10CommittersCount++;
        });
    }
    //this is logging the number of repos not contributors
    console.log(group10CommittersCount);
    document.getElementById("contributorTextGroup10").textContent = "Repo Group 10: " + group10CommittersCount + " contributors";
}

//document.getElementById("contributorText").textContent = count + count2;

request20Committers.send()
request10Committers.send()



//gathers the count for the TOTAL ISSUERS in GROUP 20
var request20Issue = new XMLHttpRequest();
request20Issue.open('GET', 'http://129.114.104.67:5000/api/unstable/repo-groups/20/issue-locations', true);
var group20IssueCount = 0;

//function to parse data
request20Issue.onload = function() {
    
    //parse
    var data = JSON.parse(this.response);

    //if you have a valid request
    if(request20Issue.status >= 200 && request20Issue.status < 400) {
        //for every repo
        data.forEach(repo => {
            //count the number of repos
            group20IssueCount++;
        });
    }
    //this is logging the number of repos not contributors
    console.log(group20IssueCount);
    document.getElementById("issuerTextGroup20").textContent = "Repo Group 20: " + group20IssueCount + " issuers";
}
console.log(group20IssueCount);


//gathers the count for the TOTAL ISSUERS in GROUP 10
var request10Issue = new XMLHttpRequest();
request10Issue.open('GET', 'http://129.114.104.67:5000/api/unstable/repo-groups/10/issue-locations', true);
var group10IssueCount = 0;

//function to parse data
request10Issue.onload = function() {
    
    //parse
    var data = JSON.parse(this.response);

    //if you have a valid request
    if(request10Issue.status >= 200 && request10Issue.status < 400) {
        //for every repo
        data.forEach(repo => {
            //count the number of repos
            group10IssueCount++;
        });
    }
    //this is logging the number of repos not contributors
    console.log(group10IssueCount);
    document.getElementById("issuerTextGroup10").textContent = "Repo Group 10: " + group10IssueCount + " issuers";
}
console.log(group10IssueCount);

request20Issue.send();
request10Issue.send();

//gathers the count for the TOTAL PULL REQUESTS in GROUP 20
var request20PullRequests = new XMLHttpRequest();
request20PullRequests.open('GET', 'http://129.114.104.67:5000/api/unstable/repo-groups/20/pull-request-locations', true);
var group20PullRequestCount = 0;

//function to parse data
request20PullRequests.onload = function() {
    
    //parse
    var data = JSON.parse(this.response);

    //if you have a valid request
    if(request20PullRequests.status >= 200 && request20PullRequests.status < 400) {
        //for every repo
        data.forEach(repo => {
            //count the number of repos
            group20PullRequestCount++;
        });
    }
    //this is logging the number of repos not contributors
    console.log(group20PullRequestCount);
    document.getElementById("pullRequestsTextGroup20").textContent = "Repo Group 20: " + group20PullRequestCount + " pull requests";
}
console.log(group20PullRequestCount);

//gathers the count for the TOTAL PULL REQUESTS in GROUP 10
var request10PullRequests = new XMLHttpRequest();
request10PullRequests.open('GET', 'http://129.114.104.67:5000/api/unstable/repo-groups/10/pull-request-locations', true);
var group10PullRequestCount = 0;

//function to parse data
request10PullRequests.onload = function() {
    
    //parse
    var data = JSON.parse(this.response);

    //if you have a valid request
    if(request10PullRequests.status >= 200 && request10PullRequests.status < 400) {
        //for every repo
        data.forEach(repo => {
            //count the number of repos
            group10PullRequestCount++;
        });
    }
    //this is logging the number of repos not contributors
    console.log(group10PullRequestCount);
    document.getElementById("pullRequestsTextGroup10").textContent = "Repo Group 10: " + group10PullRequestCount + " pull requests";
}
console.log(group10PullRequestCount);

request20PullRequests.send();
request10PullRequests.send();




//PLACES THE PINS ON THE MAP FOR ENDPOINTS FOR REPO GROUP 10 AND GROUP 20
var markersArray = [];
var marker;


function placePinByRepo(mapInstance, value){
    var xmlHttp = new XMLHttpRequest();
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