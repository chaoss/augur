var repos;
var previousFilter;

$(document).ready(function(){ 
    var initialUrl = "http://augur.osshealth.io:5000/api/unstable/repos";
    var repoGroups = "http://augur.osshealth.io:5000/api/unstable/repo-groups/";
    
    var repos = $.getJSON(initialUrl);
    var groups = $.getJSON(repoGroups);
    $.when(repos, groups).then(function(){
        var tester = JSON.parse(repos.responseText);
        var convertedGroups = JSON.parse(groups.responseText);
        
//        for(var x = 0; x < convertedGroups.length; x++){
//            $("#buttonBar").append("<button type='button' class='tester' onclick='filter(" + convertedGroups[x].rg_name + ")'>" + convertedGroups[x].rg_name + "</button>");
//        }
//        
        for(var x = 0; x < tester.length; x++){
            if(tester[x].commits_all_time != null && tester[x].issues_all_time != null){
                $("#container").append("<div id='testCSS'>" +
                                       "<div id='bBorder'><a class='link' href=https://" + tester[x].url +" target='_blank'>" + tester[x].repo_name + "</a></div>" +
                                       "<p>Total Commits: " + tester[x].commits_all_time + "</p>" +
                                       "<p>Repo Group: " + tester[x].rg_name + "</p>" +
                                       "<p>Repo Current Status: " + tester[x].repo_status + "</p>" +
                                       "</div>");
            }
        }
        
        $(".animation").remove();
        
        $(".tester").click(function(){
            console.log($(".tester").val());
        })
    });
});

function loadVisible(){
    $("#inform").css('visibility', 'visible');
}

function filter(name){
    console.log("Hello!");
}
