var sheet = false;

function logOut() {
    window.location.href='logOut.php';
}

function navBounce() {
//    Bounce effect from https://www.tutorialspoint.com/jquery/effect-bounce.htm
    $(document).ready(function() {
            $("#logoNav").click(function(){
               $("#logoNav").effect( "bounce", {times:3}, 300 );
            });
    });
}

function getRepoGroupInfo() {
    $.get("http://augur.osshealth.io:5000/api/unstable/repo-groups", function(repodata, status){
        if (status == "success") {
            var repoGroups = repodata;
            var repogr = repoGroups[0];
            //repogr.forEach((e) => {
            
            $.get("http://augur.osshealth.io:5000/api/unstable/repo-groups/" + repogr.repo_group_id + "/repos", function(committerData, status){

                    repos = committerData;
                    //e.committers.pop();

                    //e.totalCommits = 0;

                    repos.forEach((e) => {
                        $("#apacheDrop").append('<option>' + e.repo_name + '</option>');
                    });
                    
                    //$("#" + e.repo_group_id).append('<h1>' + e.rg_name + '</h1>');
                    //$("#" + e.repo_group_id).append('<canvas id="'+ e.repo_group_id +'-canvas"></canvas>');

                    //createGraph(repogr);

                });
            //});
        }

                $.get("http://augur.osshealth.io:5000/api/unstable/repo-groups/" + repogr.repo_group_id + "/top-committers?threshold=1", function(committerData, status){

                    repogr.committers = committerData;
                    repogr.committers.pop();

                    repogr.totalCommits = 0;

                    //$("#sectionList").append('<li><a href="#'+ repogr.repo_group_id + '">'+ repogr.rg_name + '</a></li>');

                    $("#sectionBody").append('<div id="'+ repogr.repo_group_id +'"></div>');
                    $("#" + repogr.repo_group_id).append('<h1>' + repogr.rg_name + '</h1>');
                    $("#" + repogr.repo_group_id).append('<canvas id="'+ repogr.repo_group_id +'-canvas"></canvas>');

                    createGraph(repogr);

                });
           // });
        }); 
    getRepoGroupNewContributors();
    getRepoGroupPullRate();
}

function getRepoGroupNewContributors() {
    $.get("http://augur.osshealth.io:5000/api/unstable/repo-groups", function(repodata, status){
        
        var repoGroups = repodata;
        monthsToSubtract = 2;
        e = repoGroups[0];
        
  //      repoGroups.forEach((e) => {
            
            var beginDate = new Date();
            var endDate = new Date();
            
            beginDate.setMonth(beginDate.getMonth() - monthsToSubtract);
            
            var newBeginDate = beginDate.getFullYear() + "-" + (beginDate.getMonth() + 1) + "-" + beginDate.getDate();
            
            var newEndDate = endDate.getFullYear() + "-" + (endDate.getMonth() + 1) + "-" + endDate.getDate();
            console.log(newBeginDate);
            
            $.get("http://augur.osshealth.io:5000/api/unstable/repo-groups/" + e.repo_group_id + "/contributors-new?period=week&begin_date="+ newBeginDate + "&end_date=" + newEndDate, function(newContributors) {
                
                if (newContributors.length > 1) { //we need at least 2 datapoints
                    var contCount = [];
                    var weekNums = [];
                    
                    console.log(newContributors);

                    //this nested loop will combine the counts from different repos on the same date
                    newContributors.forEach((f, index) => {      
                        
                        newContributors.forEach((g, i) => {
                            if (f.contribute_at === g.contribute_at && index != i) {
                                f.count += g.count;
                                newContributors.splice(i, 1);
                            }  
                        });
                        
                        contCount.push(f.count);
                        weekNums.push(index + 1);
                        newContributors.splice(index, 1);
                        
                    });

                    //$("#sectionList2").append('<li><a href="#'+ e.repo_group_id + '">'+ e.rg_name + '</a></li>');

                    $("#sectionBody2").append('<div id="'+ e.repo_group_id +'"></div>');
                    $("#" + e.repo_group_id).append('<h1>' + e.rg_name + '</h1>');
                    $("#" + e.repo_group_id).append('<canvas id="'+ e.repo_group_id +'-canvas2"></canvas>');

                    createGraphContribute(contCount, weekNums, e);
                }
                
            });
            
  //      });
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
    
    var numbers = [];
    var emails = [];
    var bgColors = [];
    var borderColors = [];
    
    committers.forEach(e => { //separate into two arrays
        
        if (e.commits > (totalCommits / 100) * .2) {
            numbers.push(e.commits);
            emails.push(e.email);
            
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
    
    if(otherCommits > 0){
        numbers.push(otherCommits);
        emails.push("Other Contributers");
    }
    
    var config = {
        type: 'doughnut',
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
					text: 'Contributions Per User (Total - '+ totalCommits +')'
				},
				animation: {
					animateScale: true,
					animateRotate: true
				}
        }
    };
    
    var ctx = document.getElementById(id + "-canvas");
    window.myChart = new Chart(ctx, config);   
}

function createGraphContribute(contributors, weeks, data) {
    var id = data.repo_group_id;
    var r = Math.floor(Math.random() * 255);
    var g = Math.floor(Math.random() * 255);
    var b = Math.floor(Math.random() * 255);
    
    var config = {
        type: 'line',
        data: {
            datasets: [{
                borderWidth: 1,
                borderColor: "rgba(" + r + "," + g + "," + b + ", 0.8)",
                backgroundColor : "rgba(" + r + "," + g + "," + b + ", 0.5)",
                data: contributors,
                label: data.rg_name
            }],
            labels: weeks
        },
        options: {
            responsive: true,
				legend: {
					display: false,
				},
				title: {
					display: true,
					text: 'Weekly New Contributors Over Last '+ monthsToSubtract +' Months'
				},
				animation: {
					animateScale: true,
					animateRotate: true
				}
        }
    };
    
    var ctx = document.getElementById(id + "-canvas2");
    window.myChart = new Chart(ctx, config);   
}

function getRepoGroupPullRate() {
    console.log("made it into the function");
    $.get("http://augur.osshealth.io:5000/api/unstable/repo-groups", function(repodata, status){
        
        var repoGroups = repodata;
        monthsToSubtract = 6;
        e = repoGroups[0];
 //       repoGroups.forEach((e) => {
            console.log(e.repo_group_id);
            var beginDate = new Date();
            var endDate = new Date();
            
            beginDate.setMonth(beginDate.getMonth() - monthsToSubtract);
            
            var newBeginDate = beginDate.getFullYear() + "-" + (beginDate.getMonth() + 1) + "-" + beginDate.getDate();
            
            var newEndDate = endDate.getFullYear() + "-" + (endDate.getMonth() + 1) + "-" + endDate.getDate();
            console.log(newBeginDate);
            
            $.get("http://augur.osshealth.io:5000/api/unstable/repo-groups/" + e.repo_group_id + "/pull-request-acceptance-rate?begin_date="+ newBeginDate + "&end_date=" + newEndDate, function(pullRate) {
                console.log(pullRate.length);
                if (pullRate.length > 1) { //we need at least 2 datapoints
                    var rates = [];
                    var weekNums = [];

                    pullRate.forEach((f, index) => {      
                        rates.push(f.rate);
                        weekNums.push(index + 1);
                    });

                    //$("#sectionList").append('<li><a href="#'+ e.repo_group_id + '">'+ e.rg_name + '</a></li>');

                    $("#sectionBody3").append('<div id="'+ e.repo_group_id +'"></div>');
                    $("#" + e.repo_group_id).append('<h1>' + e.rg_name + '</h1>');
                    $("#" + e.repo_group_id).append('<canvas id="'+ e.repo_group_id +'-canvas3"></canvas>');

                    createGraphPull(rates, weekNums, e);
                }
                
            });
            
//        });
    });   
}

function createGraphPull(rates, weeks, data) {
    var id = data.repo_group_id;
    
    var r = Math.floor(Math.random() * 255);
    var g = Math.floor(Math.random() * 255);
    var b = Math.floor(Math.random() * 255);
    
    var config = {
        type: 'line',
        data: {
            datasets: [{
                borderWidth: 1,
                borderColor: "rgba(" + r + "," + g + "," + b + ", 0.8)",
                backgroundColor : "rgba(" + r + "," + g + "," + b + ", 0.5)",
                data: rates,
                label: data.rg_name
            }],
            labels: weeks
        },
        options: {
            responsive: true,
				legend: {
					display: false,
				},
				title: {
					display: true,
					text: 'Weekly Pullrate Over Last '+ monthsToSubtract +' Months'
				},
				animation: {
					animateScale: true,
					animateRotate: true
				}
        }
    };
    
    var ctx = document.getElementById(id + "-canvas3");
    window.myChart = new Chart(ctx, config);   
}