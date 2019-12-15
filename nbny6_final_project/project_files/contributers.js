//http://augur.osshealth.io/api_docs/

function loadGraph() {
     
    var repoId = document.getElementById("repoId").value ; 
    var groupId = document.getElementById("groupId").value ;
     

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
            });
            chart1.render();

        });

}

function loadGraph2() {
     
    var repoId = document.getElementById("repoId").value ; 
    var groupId = document.getElementById("groupId").value ;
     

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
                console.log(value);
            });
            chart1.render();

        });

}