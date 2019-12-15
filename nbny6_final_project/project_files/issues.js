//http://augur.osshealth.io/api_docs/

function loadGraph() {
     
    var repoId = document.getElementById("repoId").value ; 
    var groupId = document.getElementById("groupId").value ;
     

    var dataPoints = [];

    var chart1 = new CanvasJS.Chart("chartContainer1",{
        title:{
            text:"Closed Issues by Repo Group"
        },
        axisX:{

            title: "Repo ID"
        },
        axisY:{

            title: "Closed Issue Count"

        },
            data: [{
            type: "spline",
            dataPoints : dataPoints


        }]
    });
    //http://augur.osshealth.io:5000/api/unstable/repo-groups/25151/closed-issues-count
    //http://augur.osshealth.io:5000/api/unstable/repo-groups/25151/repos/25179/contributors
        $.getJSON("http://augur.osshealth.io:5000/api/unstable/repo-groups/" + groupId + "/closed-issues-count", function(data) {
            $.each(data, function(key, value){
                chart1.options.title.text = "Closed Issues for " + value.repo_name;
                dataPoints.push({label: parseInt(value.repo_id), y: parseInt(value.closed_count)});
             
            });
            chart1.render();

        });

}

function loadGraph2() {
     
    var repoId = document.getElementById("repoId").value ; 
    var groupId = document.getElementById("groupId").value ;
   // var repoName = document.getElementById("repo_name").value;

    var dataPoints = [];

    var chart2 = new CanvasJS.Chart("chartContainer2",{
        title:{
            text:"Issues Active"
        },
        axisX:{

            title: repoId + "Active Issues Date"
        },
        axisY:{

            title: "Active Issues Count"

        },
            data: [{
            type: "bar",
            dataPoints : dataPoints


        }]
    });
                                             //   /repo-groups/:repo_group_id/repos/:repo_id/issues-active
    //http://augur.osshealth.io:5000/api/unstable/repo-groups/25151/repos/25179/contributors
    //http://augur.osshealth.io:5000/api/unstable/repo-groups/25151/repos/25179/issues-active"
        $.getJSON("http://augur.osshealth.io:5000/api/unstable/repo-groups/" + groupId + "/repos/" + repoId + "/issues-active", function(data) {
            $.each(data, function(key, value){
                chart2.options.title.text = "Active Issues By date for " + value.repo_name;
                dataPoints.push({label: parseInt(value.date), y: parseInt(value.issues)});
             
            });
            chart2.render();

        });

}

function loadGraph3() {
     
    var repoId = document.getElementById("repoId").value ; 
    var groupId = document.getElementById("groupId").value ;

    var dataPoints = [];

    var chart3 = new CanvasJS.Chart("chartContainer3",{
        title:{
            text:"Issue Backlog for Repo"
        },
        axisX:{

            title: repoId + "Repo"
        },
        axisY:{

            title: "Active Issues Count"

        },
            data: [{
            type: "pie",
            dataPoints : dataPoints


        }]
    });
                                             ///repo-groups/:repo_group_id/repos/:repo_id/issue-backlog

    //http://augur.osshealth.io:5000/api/unstable/repo-groups/25151/repos/25179/issues-active"
    //http://augur.osshealth.io:5000/api/unstable/repo-groups/25151/issue-backlog
        $.getJSON("http://augur.osshealth.io:5000/api/unstable/repo-groups/" + groupId + "/issue-backlog", function(data) {
            $.each(data, function(key, value){
                chart3.options.title.text = "Issues backlog for Repo " + value.repo_name;
                dataPoints.push({label: value.repo_name, y: parseInt(value.issue_backlog)});
             
            });
            chart3.render();

        });

}


