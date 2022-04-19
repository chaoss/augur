// BASE CODE WAS CREATED BY ASHLEYSTEVENS, I JUST USED IT FOR LEARNING PURPOSES
//REFERENCE CODE used for figuring out how google charts works:
    // https://codepen.io/ashleystevens/pen/ZEWGyjR 
// Load Google's charting functions
google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);

// Put the JSON array into a variable

const json = [
    {
      "average_sentiment": 0.0,
      "count": 1,
      "repo_id": 25436,
      "repo_name": "grimoirelab-sigils"
    },
    {
      "average_sentiment": 0.021040981635451318,
      "count": 12,
      "repo_id": 25558,
      "repo_name": "community-reports"
    },
    {
      "average_sentiment": 0.059897683560848239,
      "count": 20514,
      "repo_id": 25206,
      "repo_name": "jquery"
    },
    {
      "average_sentiment": 0.0616486519575119,
      "count": 20631,
      "repo_id": 25205,
      "repo_name": "express"
    },
    {
      "average_sentiment": 0.08402722328901291,
      "count": 2134,
      "repo_id": 25207,
      "repo_name": "body-parser"
    },
    {
      "average_sentiment": 0.09375377744436264,
      "count": 40000,
      "repo_id": 25208,
      "repo_name": "react"
    },
    {
      "average_sentiment": 0.1043178141117096,
      "count": 18475,
      "repo_id": 25204,
      "repo_name": "lodash"
    },
    {
      "average_sentiment": 0.10644396394491196,
      "count": 87,
      "repo_id": 25439,
      "repo_name": "grimoirelab-perceval-mozilla"
    },
    {
      "average_sentiment": 0.133072167634964,
      "count": 7,
      "repo_id": 25449,
      "repo_name": "governance"
    },
    {
      "average_sentiment": 0.3078271448612213,
      "count": 9,
      "repo_id": 25461,
      "repo_name": "wg-app-ecosystem"
    },
    {
      "average_sentiment": 0.4673786163330078,
      "count": 16,
      "repo_id": 25447,
      "repo_name": "metrics"
    }
  ]

// Draw the chart and set the chart values
function drawChart() {
  
  // Set the columns for the Google Chart in the first line of the array
  var messagesArray = [['RepoID', 'AvgSentiment']]; 
  // Loop through the JSON array, set up the value pair & push to the end of messagesArray
  for(i=0; i<json.length; i++) {
    messagesArray.push([json[i].repo_name, json[i].average_sentiment]);
  }
 
  // Set the Google Chart options (title, width, height, and colors can be set)
  var options = {
    title: 'Sentiment Averages',
    'width': 550,
    'height': 400
  };
  
  // Convert messagesArray into the DataTable that Google Charts needs and put it in a var
  var data = google.visualization.arrayToDataTable(messagesArray)

  // Display chart inside of the empty div element using the DataTable and Options set
  var chart = new google.visualization.BarChart(document.getElementById('piechart'));
  chart.draw(data, options);
}
