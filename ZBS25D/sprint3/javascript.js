var group_id = [];
var group_name = [];

var repo_issues_backlog = [];
var iss_backlog = [];
var repo_total_commits = [];

var repo_id = [];
var rp_name = [];
var rp_id = [];
var date = [];
var comment_rate =[];

var com_count = []
var mrge_count = []
var frk_count = []
var strs_count = []


function summaryChart() {
    document.getElementById('summary').innerHTML = "Aggregate Summary of repo group"
    var ctx = document.getElementById('graph');
    var chart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: group_id,
            datasets: [{
                label: "Merge Count",
                data: mrge_count
            },{
                label: "Commit Count",
                data: com_count
            },{
                label: "Fork Count",
                data: frk_count
            },{
                label: "Stars Count",
                data: strs_count
            }],
            backgroundColor: [
                    'rgba(255, 99, 132)',
                    'rgba(54, 162, 235)',
                    'rgba(255, 206, 86)',
                    'rgba(75, 192, 192)',
                    'rgba(153, 102, 255)',
                    'rgba(255, 159, 64)',
                    
                    'rgba(100, 99, 132)',
                    'rgba(54, 162, 24)',
                    'rgba(255, 206, 1)',
                    'rgba(75, 13, 192)',
                    'rgba(100, 102, 255)',
                    'rgba(255, 14, 64)',
                    
                    'rgba(100, 99, 12)',
                    'rgba(15, 162, 24)',
                    'rgba(155, 206, 1)',
                    'rgba(75, 13, 19)',
                    'rgba(100, 160, 255)',
                    'rgba(255, 14, 125)'
                ]
        },
        options:  {
            scales: {
                    ticks: {
                        beginAtZero: true,
                        display: true
                    }
            }
        }
    });
}


function meanCommentsChart(){
    document.getElementById('comments').innerHTML = "Mean Comments per day"
    var ctx = document.getElementById('graph2');
    var myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: date,
            datasets: [{
                label: "Mean Comments per day",
                data: comment_rate,
                backgroundColor: [
                    'rgba(255, 99, 132, .2)',
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)',
                    
                    'rgba(100, 99, 132, 1)',
                    'rgba(54, 162, 24, 1)',
                    'rgba(255, 206, 1, 1)',
                    'rgba(75, 13, 192, 1)',
                    'rgba(100, 102, 255, 1)',
                    'rgba(255, 14, 64, 1)',
                    
                    'rgba(100, 99, 12, 1)',
                    'rgba(15, 162, 24, 1)',
                    'rgba(155, 206, 1, 1)',
                    'rgba(75, 13, 19, 1)',
                    'rgba(100, 160, 255, 1)',
                    'rgba(255, 14, 125, 1)'
                ],
                borderWidth: 2,
                fill: false
            }]
        },
        options: {
            scales: {
                  yAxes: [{
                        ticks: {
                            min: 0,
                            max: 15,
                            stepSize: 0.5
                        }
                    }]
            }
        }
    });
}



var request = new XMLHttpRequest()
request.open('GET', 'http://augur.osshealth.io:5000/api/unstable/repo-groups', true)
request.onload = function() {
    var data = JSON.parse(this.response)
    console.log(data)

    if (request.status >= 200 && request.status < 400) {
        document.getElementById('groupSelect').innerHTML = ''
        
        var i = 0;
        data.forEach(repo => {
            document.getElementById('groupSelect').innerHTML += 
                '<option value="' + 
                repo.repo_group_id +
                '">' +
                repo.group_name +
                '</option>'
            
            group_id[i] = repo.repo_group_id;
            group_name[i] = repo.group_name;
            i++;
        })
    } else {
        console.log('error')
    }

    console.log(group_id)
    console.log(group_name)
}
request.send()

function get_repos(repo_group_id) {
    console.log(repo_group_id)
    var repo_request = new XMLHttpRequest()
    var url = 'http://augur.osshealth.io:5000/api/unstable/repo-groups/' + repo_group_id + '/repos'
    console.log(url)
    repo_request.open('GET', url, true)
    
    repo_request.onload = function() {
        // Begin accessing JSON data here
        var data = JSON.parse(this.response)
        console.log(data)

        if (request.status >= 200 && request.status < 400) {
            document.getElementById('repoSelect').innerHTML = ''
            document.getElementById('repoSelect').data = repo_group_id
            
            repo_id = [];
            rp_name = [];
            
            var i = 0
            data.forEach(repo => {
                document.getElementById('repoSelect').innerHTML += 
                    '<option id="op' +
                    i +
                    '" data-commits="' + 
                    repo.commits_all_time +
                    '" value="' + 
                    repo.repo_id +
                    '">' +
                    repo.repo_name +
                    '</option>'
                
                repo_id[i] = repo.repo_id;
                rp_name[i] = repo.repo_name;
                repo_total_commits[i] = repo.commits_all_time;
                i++
            })
        } else {
            console.log('error')
        }
        console.log(repo_id)
        console.log(rp_name)
        console.log(repo_total_commits)
    }
    
    repo_request.send()
}


function get_comments(option) {
    var comments_request = new XMLHttpRequest()
    var url = 'http://augur.osshealth.io:5000/api/unstable/repo-groups/' + group_id[document.getElementById('groupSelect').selectedIndex] + '/repos/' + repo_id[document.getElementById('repoSelect').selectedIndex] + '/issue-comments-mean'
     
    console.log(url)
    
    comments_request.open('GET', url, true)
    
    comments_request.onload = function() {
        // Begin accessing JSON data here
        var data = JSON.parse(this.response)
        console.log(data)

        if (request.status >= 200 && request.status < 400) {

            date = [];
            comment_mean = [];
            comment_rate =[];
            
            var i = 0;
            
    
            data.forEach(repo => {
                comment_rate = repo.date
                date[i] = comment_rate.slice(0,10)
                comment_mean[i] = repo.mean
                i++
            })
        } else {
            console.log('error')
        }
        console.log(date)
        console.log(comment_mean)
        meanCommentsChart()
    }
    
    comments_request.send()
}


function get_summary(repo_group_id) {
    console.log(repo_group_id)
    var sumamry_request = new XMLHttpRequest()
    var url = 'http://augur.osshealth.io:5000/api/unstable/repo-groups/' + repo_group_id + '/repos'
    console.log(url)
    sumamry_request.open('GET', url, true)
    
    sumamry_request.onload = function() {
        // Begin accessing JSON data here
        var data = JSON.parse(this.response)
        console.log(data)

        if (request.status >= 200 && request.status < 400) {
    
            com_count = []
            mrge_count = []
            frk_count = []
            strs_count = []
            
            var i = 0
            data.forEach(repo => {
               
                commit_count[i] = repo.commit_count
                mrge_count[i] = repo.merged_count
                frk_count[i] = repo.fork_count
                strs_count[i] = repo.stars_count
                i++
                
            })
        } else {
            console.log('error')
        }
        console.log(com_count)
        console.log(mrge_count)
        console.log(frk_count)
        console.log(strs_count)
        summaryChart()
    }
    
    sumamry_request.send()
}

