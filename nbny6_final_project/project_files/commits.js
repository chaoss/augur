// use 24 and 3rd one down for error
// 25150 - 25151
    
function loadGraph() {
      let repoId = document.getElementById("repoId").value ; 
        let groupId = document.getElementById("groupId").value ;
     
 $.ajax({
    url: "http://augur.osshealth.io:5000/api/unstable/repo-groups/"+ groupId +"/repos/"+repoId+"/top-committers",
    statusCode: {
        500: function() {
            alert(" 500 Error Was returned for the Top Commiters API Endpoint");
            console.log('500 ');
        }
    }
    }); 

var dataPoints = [];

var chart = new CanvasJS.Chart("chartContainer",{
    title:{
        text:"Representation of top commiters"
    },
    axisX:{
        
        title: "emails of commiters"
    },
    axisY:{
        
        title: "total commits"
        
    },
        data: [{
        type: "pie",
        dataPoints : dataPoints
    
        
    }]
});
   
       
    $.getJSON("http://augur.osshealth.io:5000/api/unstable/repo-groups/"+ groupId +"/repos/"+repoId+"/top-committers", function(data) {  
    $.each(data, function(key, value){
         console.log(value.email);
        chart.options.title.text="Representation of Top Commiters in " + value.repo_name;
        //chartContainer.options.title.text = "Representation of top committers of" + value.repo_name;
        
        
        dataPoints.push({label: value.email, y: parseInt(value.commits)});
        console.log(value);
    });
    chart.render();
  
        
        
        
});
      
}

function loadSecondGraph(){
    
     let repoId = document.getElementById("repoId").value ; 
        let groupId = document.getElementById("groupId").value ;
    
    
      $.ajax({
    url: "http://augur.osshealth.io:5000/api/unstable/repo-groups/"+groupId+"/repos/"+repoId+"/committers",
    statusCode: {
        500: function() {
            alert(" 500 Error was returned from the commiters API Endpoint");
            console.log('500 ');
        }
    }
}); 
    
    
var dataPoints = [];

var chart = new CanvasJS.Chart("chartContainer2",{
    
    
    
    title:{
        text:"Commits in Repo Over Time"
    },
    axisX:{
        
        title: "Date"
    },
    axisY:{
        
        title: "Total Commits"
        
    },
        data: [{
        type: "line",
        dataPoints : dataPoints
    
        
    }]
});
   //$.getJSON("http://augur.osshealth.io:5000/api/unstable/repo-groups/"+ groupId +"/repos/"+repoId+"/committers", function(data) {  
    
     $.getJSON("http://augur.osshealth.io:5000/api/unstable/repo-groups/"+groupId+"/repos/"+repoId+"/committers", function(data) {  
    $.each(data, function(key, value){
        chart.options.title.text="Commits in Repo Over Time in " + value.repo_name;
        dataPoints.push({label: value.date, y: parseInt(value.count)});
  
    });
    chart.render();
         
   
});
    
      
    
    
}


function loadThirdGraph() {
      let repoId = document.getElementById("repoId").value ; 
        let groupId = document.getElementById("groupId").value ;
     
 $.ajax({
    url: "http://augur.osshealth.io:5000/api/unstable/repo-groups/"+ groupId +"/repos/"+repoId+"/pull-requests-merge-contributor-new",
    statusCode: {
        500: function() {
            alert(" 500 Error Was returned for the new contributors API Endpoint");
            console.log('500 ');
        }
    }
    }); 

var dataPoints = [];

var chart = new CanvasJS.Chart("chartContainer3",{
    title:{
        text:"Representation of top commiters"
    },
    axisX:{
        
        title: "Commit Date"
    },
    axisY:{
        
        title: "Count of Commits"
        
    },
        data: [{
        type: "line",
        dataPoints : dataPoints
    
        
    }]
});
   
       
    $.getJSON("http://augur.osshealth.io:5000/api/unstable/repo-groups/"+ groupId +"/repos/"+repoId+"/pull-requests-merge-contributor-new", function(data) {  
    $.each(data, function(key, value){
         console.log(value.commit_date);
        chart.options.title.text="Representation of commits of New Contributors from " + value.repo_name;
        //chartContainer.options.title.text = "Representation of top committers of" + value.repo_name;
        
        
        dataPoints.push({label: value.commit_date, y: parseInt(value.count)});
        console.log(value);
    });
    chart.render();
  
        
        
        
});
      
}


