function getTestData(group) {
        
    var group = group;
    console.log(group);
    
    var xhttp = new XMLHttpRequest();

    xhttp.open("GET", "http://129.114.16.76:5000/api/unstable/repo-groups/" + group + "/testing-coverage/", true);
    
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var data = JSON.parse(this.responseText);
            console.log(data);
            
            let subT = data[0].file_subroutines_tested;
            let subC = data[0].file_subroutine_count;
            let statT = data[0].file_statements_tested;
            let statC = data[0].file_statement_count;
            
            let sub = 100*subT/subC;
            console.log(sub);
            let stat = 100*statT/statC;
            console.log(stat);
            
            document.getElementById('subMeter').value = sub;
            document.getElementById('statMeter').value = stat;
            document.getElementById('subLabel').innerHTML = parseFloat(sub).toFixed(2.2)+"%";
            document.getElementById('statLabel').innerHTML = parseFloat(stat).toFixed(2.2)+"%";
            
        } 
    };

    xhttp.send();
    
}
