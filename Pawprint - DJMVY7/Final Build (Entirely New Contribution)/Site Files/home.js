var numbers = [];
var emails = [];
var sheet = false;

function logOut() {
    window.location.href='logOut.php';
}

function toggleDarkLight() {
  var body = document.getElementById("body");
  var currentClass = body.className;
  body.className = currentClass == "dark-mode" ? "light-mode" : "dark-mode";
}

function getRepoGroupInfo() {
    $.get("http://augur.osshealth.io:5000/api/unstable/repo-groups", function(repodata, status){
        if (status == "success") {
            var repoGroups = repodata;
            //var repogr = repoGroups[3];
            repoGroups.forEach((e) => {

                $.get("http://augur.osshealth.io:5000/api/unstable/repo-groups/" + e.repo_group_id + "/top-committers?threshold=1", function(committerData, status){

                    e.committers = committerData;
                    e.committers.pop();

                    e.totalCommits = 0;

                    //$("#sectionList").append('<li><a href="#'+ repogr.repo_group_id + '">'+ repogr.rg_name + '</a></li>');

                    //$("#sectionBody").append('<div id="'+ e.repo_group_id +'"></div>');
                    //$("#" + e.repo_group_id).append('<h1>' + e.rg_name + '</h1>');
                    //$("#" + e.repo_group_id).append('<canvas id="'+ e.repo_group_id +'-canvas"></canvas>');
                    $("#" + e.repo_group_id).append('<canvas id="canvas"></canvas>');
                    var committers = e.committers;
                    var f = committers[0];
                    numbers.push(f.commits);
                    console.log(numbers);
                    emails.push(f.repo_group_name);
                    createGraph(e);
                });
            });
        }
    }); 

}

function createGraph(data) {
    var id = data.repo_group_id;
    var committers = data.committers;
    var otherCommits = 0; //this accounts for any commit
    var totalCommits = 0;
    
    committers.forEach(e => {
        totalCommits += e.commits;
    });
    
    //var numbers = [];
    //var emails = [];
    var bgColors = [];
    var borderColors = [];
    var numbers2 = [];
    var emails2 = [];
    var e = committers[0];
    committers.forEach(e => { //separate into two arrays
        
        if (e.commits > (totalCommits / 100) * .2) {
            //numbers.push(e.commits);
            //emails.push(e.email);
            
            var r = Math.floor(Math.random() * 255);
            var g = Math.floor(Math.random() * 255);
            var b = Math.floor(Math.random() * 255);
            bgColors.push("rgba(" + r + "," + g + "," + b + ", 0.5)");
            borderColors.push("rgba(" + r + "," + g + "," + b + ", 0.7)");
        }
        else {
            otherCommits += e.commits;
        }
        
    });


    console.log(numbers);
    if(numbers.length == 8){
    var config = {
        type: 'bar',
        data: {
            datasets: [{
                borderWidth: 1,
                data: numbers,
                label: data.rg_name,
                backgroundColor: bgColors,
                borderColor: borderColors
            }],
            labels: emails
        },
        options: {
            responsive: true,
				legend: {
					display: false,
				},
				title: {
					display: true,
					text: 'Contributors for Each Repo Group'
				},
				animation: {
					animateScale: true,
					animateRotate: true
				}
        }
    };
    
    var ctx = document.getElementById("canvas");
    window.myChart = new Chart(ctx, config);
    }
}