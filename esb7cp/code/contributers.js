//http://augur.osshealth.io/api_docs/

function loadGraph() {
     
    var repoId = document.getElementById("repoId").value ; 
    var groupId = document.getElementById("groupId").value ;
     
     $.ajax({
    url: "http://augur.osshealth.io:5000/api/unstable/repo-groups/"+ groupId +"/repos/"+repoId+"/contributors",
    statusCode: {
        500: function() {
            alert(" 500 Error Was returned for the Contributors API Endpoint");
            console.log('500 ');
        }
    }
    }); 
    
    var dataPoints = [];

    var chart1 = new CanvasJS.Chart("chartContainer1",{
        title:{
            text:"Representation of contributers for "
        },
        axisX:{

            title: "Contributer number"
        },
        axisY:{

            title: "total contributions (commits + issues + comments)"

        },
            data: [{
            type: "column",
            dataPoints : dataPoints


        }]
    });
        $.getJSON("http://augur.osshealth.io:5000/api/unstable/repo-groups/" + groupId + "/repos/" + repoId + "/contributors", function(data) {
            $.each(data, function(key, value){
                chart1.options.title.text = "Representation of contributers for " + value.repo_name;
                dataPoints.push({label: parseInt(value.user_id), y: parseInt(value.total)});
                console.log(value);
                if (value == null){
                    alert("Error. Data is NULL");
                    console.log("null");
                    break;
                }
            });
            chart1.render();
         

        });
}

function loadGraph2() {
     
    var repoId = document.getElementById("repoId").value ; 
    var groupId = document.getElementById("groupId").value ;
     
         $.ajax({
    url: "http://augur.osshealth.io:5000/api/unstable/repo-groups/"+ groupId +"/repos/"+repoId+"/contributors-new",
    statusCode: {
        500: function() {
            alert(" 500 Error Was returned for the Contributors-New API Endpoint");
            console.log('500 ');
        }
    }
    }); 
    
    
    var dataPoints = [];

    var chart1 = new CanvasJS.Chart("chartContainer2",{
        title:{
            text:"Representation of new contributions for "
        },
        axisX:{

            title: "Date"
        },
        axisY:{

            title: "total contributions"

        },
            data: [{
            type: "column",
            dataPoints : dataPoints


        }]
    });
    ///repo-groups/:repo_group_id/repos/:repo_id/contributors-new
        $.getJSON("http://augur.osshealth.io:5000/api/unstable/repo-groups/" + groupId + "/repos/" + repoId + "/contributors-new", function(data) {
            $.each(data, function(key, value){
                chart1.options.title.text = "Representation of new contributions for " + value.repo_name;
                dataPoints.push({label: value.contribute_at, y: value.count});
                console.log(value);
            });
            chart1.render();

        });

}

function loadGraph3() {
     
    var repoId = document.getElementById("repoId").value ; 
    var groupId = document.getElementById("groupId").value ;
     
             $.ajax({
    url: "http://augur.osshealth.io:5000/api/unstable/repo-groups/"+ groupId +"/repos/"+repoId+"/pull-requests-merge-contributor-new",
    statusCode: {
        500: function() {
            alert(" 500 Error Was returned for the New Contributors of Commits API Endpoint");
            console.log('500 ');
        }
    }
    }); 

    var dataPoints = [];

    var chart1 = new CanvasJS.Chart("chartContainer3",{
        title:{
            text:"Representation of new contributions for "
        },
        axisX:{

            title: "Date"
        },
        axisY:{

            title: "total commits"

        },
            data: [{
            type: "column",
            dataPoints : dataPoints


        }]
    });
    ///repo-groups/:repo_group_id/repos/:repo_id/pull-requests-merge-contributor-new
        $.getJSON("http://augur.osshealth.io:5000/api/unstable/repo-groups/" + groupId + "/repos/" + repoId + "/pull-requests-merge-contributor-new", function(data) {
            $.each(data, function(key, value){
                chart1.options.title.text = "Representation of new contributions of commits for " + value.repo_name;
                dataPoints.push({label: value.commit_date, y: value.count});
                //console.log(value);
            });
            chart1.render();

        });

}