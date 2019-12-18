function getContrData(group) {
        
    var group = group;
    console.log(group);
    
    var xhttp = new XMLHttpRequest();

    xhttp.open("GET", "http://129.114.16.76:5000/api/unstable/repo-groups/" + group + "/contributor-affiliation/", true);
    
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var data = JSON.parse(this.responseText);
            console.log(data);
            
            var locations = [];
            var contributors = [];
            
            for(let i = 0; i < data.length; i++) {
                var username = data[i].gh_login;
                var url = data[i].gh_html_url;
                var created = data[i].cntrb_created_at;
                var company = data[i].cntrb_company;
                var location = data[i].cntrb_location;
                if(data[i].lat && data[i].lng) {
                    var latitude = data[i].lat;
                    var longitude = data[i].lng;
                    var coordinates = {
                        lat: latitude,
                        lng: longitude
                    };
                    console.log(coordinates);
                    locations.push(coordinates);
                }
                contributors.push([username, url, created, company, location]);
            }
            console.log(locations);
            console.log(contributors);
            
            document.getElementById('load').innerHTML = '';
            
            tableRef = document.getElementById('table'+group).getElementsByTagName('tbody')[0];
        
            
            for(let i = 0; i < contributors.length; i++) {
                var newRow = tableRef.insertRow(tableRef.rows.length);
                var username = newRow.insertCell(0);
                username.innerHTML = contributors[i][4];
                var url = newRow.insertCell(0);
                url.innerHTML = contributors[i][3];
                var created = newRow.insertCell(0);
                created.innerHTML = contributors[i][2];
                var company = newRow.insertCell(0);
                company.innerHTML = contributors[i][1];
                var location = newRow.insertCell(0);
                location.innerHTML = contributors[i][0];
            } 
            return locations;
        } 
    };
    
    xhttp.send();
    
}