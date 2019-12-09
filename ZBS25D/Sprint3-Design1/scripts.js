var rg_id = [];
var rg_name = [];

var rp_id = [];
var rp_name = [];
var rp_tot_commits = [];

var con_email = [];
var con_commits = [];

var date = [];
var pull_rate = [];

function chartCommits(){
    document.getElementById('committers').innerHTML = "Number of commits made by each contributor"
    const ctx = document.getElementById('secondChart');
    const chart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: con_email,
            datasets: [{
                label: "Number of Commits",
                data: con_commits,
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
                ],
            }]
        },
        options: { 
            scales: {
                    ticks: {
                        beginAtZero: true,
                        display: true
                    }
            }
        }
    });
}

function chartTotalCommits(){
    var name = [];
    var tot_commits = [];
    
    name = rp_name;
    tot_commits = rp_tot_commits;

    top_ten_name = name.slice(3,13);
    top_ten_commits = tot_commits.slice(3,13);
    
    console.log(name);
    console.log(tot_commits);

    document.getElementById('totCommits').innerHTML = "Top 10 repo total commits"
    var ctx = document.getElementById('firstChart');
    var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: top_ten_name,
            datasets: [{
                label: 'Total Commits',
                data: top_ten_commits,
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
                    
                    'rgba(205, 99, 132)',
                    'rgba(54, 62, 235)',
                    'rgba(155, 206, 86)',
                    'rgba(75, 12, 192)',
                    'rgba(153, 102, 25)',
                    'rgba(255, 159, 6)',
                    
                    'rgba(100, 99, 12)',
                    'rgba(15, 162, 24)',
                    'rgba(155, 206, 1)',
                    'rgba(75, 13, 19)',
                    'rgba(100, 160, 255)',
                    'rgba(255, 14, 125)'
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
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });
}

function chartPull(){
    document.getElementById('pull').innerHTML = "Pull request acceptance rate"
    var ctx = document.getElementById('thirdChart');
    var myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: date,
            datasets: [{
                label: "Pull request acceptance rate over time",
                data: pull_rate,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
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
            elements: {
                line:{ tension: 0.1,
                    ticks: {
                        beginAtZero: true,
                    }
                }
            }
        }
    });
}

var request = new XMLHttpRequest()
request.open('GET', 'http://augur.osshealth.io:5000/api/unstable/repo-groups', true)
request.onload = function() {
    // Begin accessing JSON data here
    var data = JSON.parse(this.response)
    console.log(data)

    if (request.status >= 200 && request.status < 400) {
        document.getElementById('repo-group-select').innerHTML = ''
        
        var i = 0;
        data.forEach(repo => {
            //console.log(repo.rg_description)
            document.getElementById('repo-group-select').innerHTML += 
                '<option value="' + 
                repo.repo_group_id +
                '">' +
                repo.rg_name +
                '</option>'
            
            rg_id[i] = repo.repo_group_id;
            rg_name[i] = repo.rg_name;
            i++;
        })
    } else {
        console.log('error')
    }

    console.log(rg_id);
    console.log(rg_name);
}

// Send request
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
            document.getElementById('repos').innerHTML = ''
            document.getElementById('repos').data = repo_group_id
            
            rp_id = [];
            rp_name = [];
            rp_tot_commits = [];
            
            var i = 0
            data.forEach(repo => {
                //console.log(repo.rg_description)
                document.getElementById('repos').innerHTML += 
                    '<option id="op' +
                    i +
                    '" data-commits="' + 
                    repo.commits_all_time + 
                    '" value="' + 
                    repo.repo_id +
                    '">' +
                    repo.repo_name +
                    '</option>'
                
                rp_id[i] = repo.repo_id;
                rp_name[i] = repo.repo_name;
                rp_tot_commits[i] = repo.commits_all_time;
                i++
            })
        } else {
            console.log('error')
        }
        console.log(rp_id)
        console.log(rp_name)
        console.log(rp_tot_commits)
        chartTotalCommits()
    }
    
    repo_request.send()
}

function get_contributors(option) {
    var contributor_request = new XMLHttpRequest()
    var url = 'http://augur.osshealth.io:5000/api/unstable/repo-groups/' + rg_id[document.getElementById('repo-group-select').selectedIndex] + '/repos/' + rp_id[document.getElementById('repos').selectedIndex] + '/top-committers'
    
    commits_all_time = rp_tot_commits[document.getElementById('repos').selectedIndex]
    
    console.log(commits_all_time + ' ' + url)
    
    contributor_request.open('GET', url, true)
    
    contributor_request.onload = function() {
        // Begin accessing JSON data here
        var data = JSON.parse(this.response)
        console.log(data)

        if (request.status >= 200 && request.status < 400) {

            con_email = [];
            con_commits = [];
            
            var i = 0;
            data.forEach(contributor => {
                con_email[i] = contributor.email
                con_commits[i] = contributor.commits
                i++
            })
        } else {
            console.log('error')
        }
        console.log(con_email)
        console.log(con_commits)
        chartCommits()
        pull(option)
    }
    
    contributor_request.send()
}

function pull(option) {
    var pull_request = new XMLHttpRequest()
    var url = 'http://augur.osshealth.io:5000/api/unstable/repo-groups/' + rg_id[document.getElementById('repo-group-select').selectedIndex] + '/repos/' + rp_id[document.getElementById('repos').selectedIndex] + '/pull-request-acceptance-rate'
    
    pull_request.open('GET', url, true)
    
    pull_request.onload = function() {
        // Begin accessing JSON data here
        var data = JSON.parse(this.response)
        console.log(data)

        if (request.status >= 200 && request.status < 400) {

            date = [];
            pull_rate = [];
            var cut_rate;
            
            var i = 0;
            data.forEach(pull => {
                cut_rate = pull.date
                date[i] = cut_rate.slice(0,10)
                pull_rate[i] = pull.rate
                i++
            })
        } else {
            console.log('error')
        }
        console.log(date)
        console.log(pull_rate)
        chartPull()
    }
    
    pull_request.send()
}