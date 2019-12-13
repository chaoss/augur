function getCommData(group) {
        
    var group = group;
    console.log(group);
    
    var xhttp = new XMLHttpRequest();

    xhttp.open("GET", "http://129.114.16.76:5000/api/unstable/repo-groups/" + group + "/committer-data/", true);
    
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var data = JSON.parse(this.responseText);
            console.log(data);
            
            let male = 0
            let female = 0
            let gOther = 0
            let w = 0
            let hl = 0
            let b = 0
            let a = 0
            let eOther = 0
            var people = []
            
            // ITERATE THROUGH JSON RESPONSE
            for (let i = 0; i < data.length; i++) {
                let gender = data[i].gender
                let genderProb = Math.abs(data[i].genderProb)
                let eth = data[i].eth
                let ethProb = Math.abs(data[i].ethProb)
                let name = data[i].cmt_author_name
                
                
                if (genderProb > .8){
                    if (gender  == "male"){
                        male += 1
                    } else if (gender  == "female"){
                        female += 1
                    } 
                } else {
                    gOther += 1
                    gender = "unknown"
                }
                
                if (ethProb > .5){
                    if (eth  == "W_NL"){
                        w += 1
                    } else if (eth  == "HL"){
                        hl += 1
                    } else if (eth  == "B_NL"){
                        b += 1
                    } else if (eth  == "A"){
                        a += 1
                    } 
                } else {
                    eOther += 1
                    eth = "unknown"
                }
                
                if (eth != "unknown" || gender != "unknown"){
                    people.push([eth, gender, name])
                }
            }
            
            
            // CONSTRUCT DATA TABLES
            var genderData = google.visualization.arrayToDataTable([
                ['Gender', 'Percentage'],
                ['Male', male],
                ['Female', female],
                ['Unknown', gOther]
            ]);
            
            var ethnicityData = google.visualization.arrayToDataTable([
                ['Ethnicity', 'Percentage'],
                ['White', w],
                ['Hispanic/Latino', hl],
                ['Black', b],
                ['Asian', a],
                ['Unknown', eOther]
            ]);
            
            
            // CREATE CHARTS
            var options = {
                is3D: true
            };
            
            document.getElementById('load').innerHTML = '';
            var gender = new google.visualization.PieChart(document.getElementById('gender'));
            gender.draw(genderData, options);
            var ethnicity = new google.visualization.PieChart(document.getElementById('ethnicity'));
            ethnicity.draw(ethnicityData, options);
            
            
            // CREATE TABLE WITH NAMES AND ETHNICITIES
            tableRef = document.getElementById('table').getElementsByTagName('tbody')[0];
            
            for (let i = 0; i < people.length; i++) {
                var newRow   = tableRef.insertRow(tableRef.rows.length);

              // Insert a cell in the row at index 0
                var nameCell  = newRow.insertCell(0);
                nameCell.innerHTML = people[i][0];
                var genderCell  = newRow.insertCell(0);
                genderCell.innerHTML = people[i][1];
                var ethCell  = newRow.insertCell(0);
                ethCell.innerHTML = people[i][2];
            } 
        }
    };

    xhttp.send();
    
}

