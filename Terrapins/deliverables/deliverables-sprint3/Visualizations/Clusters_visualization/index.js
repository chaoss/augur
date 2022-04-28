// BASE CODE WAS CREATED BY ASHLEYSTEVENS, I JUST USED IT FOR LEARNING PURPOSES
//REFERENCE CODE used for figuring out how google charts works:
    // https://codepen.io/ashleystevens/pen/ZEWGyjR 
// Load Google's charting functions
google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);

// Put the JSON array into a variable

const json = [
    {
      "repo_id": 25437,
      "repo_name": "grimoirelab-sirmordred",
      "cluster_content": 1,
      "max": "15/4/2022 19:26:59"
    },
    {
      "repo_id": 25435,
      "repo_name": "grimoirelab-cereslib",
      "cluster_content": 3,
      "max": "15/4/2022 19:26:55"
    },
    {
      "repo_id": 25451,
      "repo_name": "wg-diversity-inclusion",
      "cluster_content": 0,
      "max": "15/4/2022 19:28:11"
    },
    {
      "repo_id": 25447,
      "repo_name": "metrics",
      "cluster_content": 0,
      "max": "15/4/2022 19:27:30"
    },
    {
      "repo_id": 25558,
      "repo_name": "community-reports",
      "cluster_content": 0,
      "max": "15/4/2022 19:23:38"
    },
    {
      "repo_id": 25460,
      "repo_name": "augur-license",
      "cluster_content": 0,
      "max": "15/4/2022 19:29:41"
    },
    {
      "repo_id": 25208,
      "repo_name": "react",
      "cluster_content": 2,
      "max": "15/4/2022 19:25:58"
    },
    {
      "repo_id": 25438,
      "repo_name": "grimoirelab-tutorial",
      "cluster_content": 3,
      "max": "15/4/2022 19:27:02"
    },
    {
      "repo_id": 25442,
      "repo_name": "grimoirelab-manuscripts",
      "cluster_content": 1,
      "max": "15/4/2022 19:27:09"
    },
    {
      "repo_id": 25448,
      "repo_name": "grimoirelab",
      "cluster_content": 3,
      "max": "15/4/2022 19:27:43"
    },
    {
      "repo_id": 25436,
      "repo_name": "grimoirelab-sigils",
      "cluster_content": 3,
      "max": "15/4/2022 19:26:56"
    },
    {
      "repo_id": 25450,
      "repo_name": "grimoirelab-hatstall",
      "cluster_content": 3,
      "max": "15/4/2022 19:28:00"
    },
    {
      "repo_id": 25205,
      "repo_name": "express",
      "cluster_content": 2,
      "max": "15/4/2022 19:24:24"
    },
    {
      "repo_id": 25440,
      "repo_name": "augur",
      "cluster_content": 0,
      "max": "15/4/2022 19:27:06"
    },
    {
      "repo_id": 25441,
      "repo_name": "grimoirelab-perceval-puppet",
      "cluster_content": 1,
      "max": "15/4/2022 19:27:08"
    },
    {
      "repo_id": 25457,
      "repo_name": "wg-value",
      "cluster_content": 0,
      "max": "15/4/2022 19:29:11"
    },
    {
      "repo_id": 25456,
      "repo_name": "grimoirelab-graal",
      "cluster_content": 3,
      "max": "15/4/2022 19:29:01"
    },
    {
      "repo_id": 25434,
      "repo_name": "grimoirelab-kingarthur",
      "cluster_content": 1,
      "max": "15/4/2022 19:26:53"
    },
    {
      "repo_id": 25206,
      "repo_name": "jquery",
      "cluster_content": 2,
      "max": "15/4/2022 19:24:57"
    },
    {
      "repo_id": 25445,
      "repo_name": "grimoirelab-perceval-opnfv",
      "cluster_content": 1,
      "max": "15/4/2022 19:27:11"
    },
    {
      "repo_id": 25461,
      "repo_name": "wg-app-ecosystem",
      "cluster_content": 0,
      "max": "15/4/2022 19:23:28"
    },
    {
      "repo_id": 25433,
      "repo_name": "grimoirelab-kibiter",
      "cluster_content": 3,
      "max": "15/4/2022 19:26:53"
    },
    {
      "repo_id": 25458,
      "repo_name": "wg-risk",
      "cluster_content": 0,
      "max": "15/4/2022 19:29:21"
    },
    {
      "repo_id": 25432,
      "repo_name": "grimoirelab-perceval",
      "cluster_content": 1,
      "max": "15/4/2022 19:26:49"
    },
    {
      "repo_id": 25449,
      "repo_name": "governance",
      "cluster_content": 0,
      "max": "15/4/2022 19:27:47"
    },
    {
      "repo_id": 25453,
      "repo_name": "website",
      "cluster_content": 0,
      "max": "15/4/2022 19:28:31"
    },
    {
      "repo_id": 25459,
      "repo_name": "wg-common",
      "cluster_content": 0,
      "max": "15/4/2022 19:29:31"
    },
    {
      "repo_id": 25454,
      "repo_name": "grimoirelab-kidash",
      "cluster_content": 3,
      "max": "15/4/2022 19:28:41"
    },
    {
      "repo_id": 25444,
      "repo_name": "grimoirelab-toolkit",
      "cluster_content": 1,
      "max": "15/4/2022 19:27:11"
    },
    {
      "repo_id": 25204,
      "repo_name": "lodash",
      "cluster_content": 2,
      "max": "15/4/2022 19:23:58"
    },
    {
      "repo_id": 25443,
      "repo_name": "grimoirelab-bestiary",
      "cluster_content": 3,
      "max": "15/4/2022 19:27:10"
    },
    {
      "repo_id": 25430,
      "repo_name": "grimoirelab-sortinghat",
      "cluster_content": 3,
      "max": "15/4/2022 19:26:37"
    },
    {
      "repo_id": 25455,
      "repo_name": "wg-evolution",
      "cluster_content": 0,
      "max": "15/4/2022 19:28:52"
    },
    {
      "repo_id": 25439,
      "repo_name": "grimoirelab-perceval-mozilla",
      "cluster_content": 1,
      "max": "15/4/2022 19:27:03"
    },
    {
      "repo_id": 25207,
      "repo_name": "body-parser",
      "cluster_content": 2,
      "max": "15/4/2022 19:25:16"
    },
    {
      "repo_id": 25446,
      "repo_name": "prospector",
      "cluster_content": 0,
      "max": "15/4/2022 19:27:15"
    },
    {
      "repo_id": 25431,
      "repo_name": "grimoirelab-elk",
      "cluster_content": 1,
      "max": "15/4/2022 19:26:42"
    }
  ]

// Draw the chart and set the chart values
function drawChart() {
  
  // Set the columns for the Google Chart in the first line of the array
  var messagesArray = [['RepoName', 'ClusterContent']]; 
  // Loop through the JSON array, set up the value pair & push to the end of messagesArray
  for(i=0; i<json.length; i++) {
    messagesArray.push([json[i].repo_name, json[i].cluster_content]);
  }
 
  // Set the Google Chart options (title, width, height, and colors can be set)
  var options = {
    title: 'Clustering',
    'width': 700,
    'height': 700
  };
  
  // Convert messagesArray into the DataTable that Google Charts needs and put it in a var
  var data = google.visualization.arrayToDataTable(messagesArray)

  // Display chart inside of the empty div element using the DataTable and Options set
  var chart = new google.visualization.BarChart(document.getElementById('piechart'));
  chart.draw(data, options);
}