google.charts.load('current', {'packages':['corechart', 'scatter']});
google.charts.setOnLoadCallback(drawChart);

const json = [
  {
    "repo_name": "grimoirelab-sortinghat",
    "repo_git": "https://github.com/chaoss/grimoirelab-sortinghat",
    "repo_id": 25430,
    "cluster_content": 0,
    "message_count": 1600,
    "issue_event_count": 3487,
    "pull_request_event_count": 2220,
    "msg_cluster_id": 3302
  },
  {
    "repo_name": "grimoirelab-kibiter",
    "repo_git": "https://github.com/chaoss/grimoirelab-kibiter",
    "repo_id": 25433,
    "cluster_content": 0,
    "message_count": 143,
    "issue_event_count": 666,
    "pull_request_event_count": 558,
    "msg_cluster_id": 3305
  },
  {
    "repo_name": "grimoirelab-cereslib",
    "repo_git": "https://github.com/chaoss/grimoirelab-cereslib",
    "repo_id": 25435,
    "cluster_content": 0,
    "message_count": 43,
    "issue_event_count": 193,
    "pull_request_event_count": 157,
    "msg_cluster_id": 3307
  },
  {
    "repo_name": "grimoirelab-sigils",
    "repo_git": "https://github.com/chaoss/grimoirelab-sigils",
    "repo_id": 25436,
    "cluster_content": 0,
    "message_count": 724,
    "issue_event_count": 2452,
    "pull_request_event_count": 1974,
    "msg_cluster_id": 3308
  },
  {
    "repo_name": "grimoirelab-tutorial",
    "repo_git": "https://github.com/chaoss/grimoirelab-tutorial",
    "repo_id": 25438,
    "cluster_content": 0,
    "message_count": 547,
    "issue_event_count": 1257,
    "pull_request_event_count": 830,
    "msg_cluster_id": 3310
  },
  {
    "repo_name": "grimoirelab-bestiary",
    "repo_git": "https://github.com/chaoss/grimoirelab-bestiary",
    "repo_id": 25443,
    "cluster_content": 0,
    "message_count": 304,
    "issue_event_count": 546,
    "pull_request_event_count": 448,
    "msg_cluster_id": 3315
  },
  {
    "repo_name": "grimoirelab",
    "repo_git": "https://github.com/chaoss/grimoirelab",
    "repo_id": 25448,
    "cluster_content": 0,
    "message_count": 2445,
    "issue_event_count": 4924,
    "pull_request_event_count": 1072,
    "msg_cluster_id": 3283
  },
  {
    "repo_name": "grimoirelab-hatstall",
    "repo_git": "https://github.com/chaoss/grimoirelab-hatstall",
    "repo_id": 25450,
    "cluster_content": 0,
    "message_count": 154,
    "issue_event_count": 594,
    "pull_request_event_count": 448,
    "msg_cluster_id": 3285
  },
  {
    "repo_name": "grimoirelab-kidash",
    "repo_git": "https://github.com/chaoss/grimoirelab-kidash",
    "repo_id": 25454,
    "cluster_content": 0,
    "message_count": 100,
    "issue_event_count": 263,
    "pull_request_event_count": 154,
    "msg_cluster_id": 3288
  },
  {
    "repo_name": "grimoirelab-graal",
    "repo_git": "https://github.com/chaoss/grimoirelab-graal",
    "repo_id": 25456,
    "cluster_content": 0,
    "message_count": 380,
    "issue_event_count": 1013,
    "pull_request_event_count": 655,
    "msg_cluster_id": 3290
  },
  {
    "repo_name": "prospector",
    "repo_git": "https://github.com/chaoss/prospector",
    "repo_id": 25446,
    "cluster_content": 1,
    "message_count": 11,
    "issue_event_count": 14,
    "pull_request_event_count": 6,
    "msg_cluster_id": 3281
  },
  {
    "repo_name": "metrics",
    "repo_git": "https://github.com/chaoss/metrics",
    "repo_id": 25447,
    "cluster_content": 1,
    "message_count": 642,
    "issue_event_count": null,
    "pull_request_event_count": null,
    "msg_cluster_id": 3282
  },
  {
    "repo_name": "governance",
    "repo_git": "https://github.com/chaoss/governance",
    "repo_id": 25449,
    "cluster_content": 1,
    "message_count": 908,
    "issue_event_count": 2200,
    "pull_request_event_count": 1397,
    "msg_cluster_id": 3284
  },
  {
    "repo_name": "wg-diversity-inclusion",
    "repo_git": "https://github.com/chaoss/wg-diversity-inclusion",
    "repo_id": 25451,
    "cluster_content": 1,
    "message_count": 1102,
    "issue_event_count": 2552,
    "pull_request_event_count": 273,
    "msg_cluster_id": 3286
  },
  {
    "repo_name": "website",
    "repo_git": "https://github.com/chaoss/website",
    "repo_id": 25453,
    "cluster_content": 1,
    "message_count": 1660,
    "issue_event_count": 4136,
    "pull_request_event_count": 2384,
    "msg_cluster_id": 3287
  },
  {
    "repo_name": "wg-evolution",
    "repo_git": "https://github.com/chaoss/wg-evolution",
    "repo_id": 25455,
    "cluster_content": 1,
    "message_count": 1691,
    "issue_event_count": 3376,
    "pull_request_event_count": 2025,
    "msg_cluster_id": 3289
  },
  {
    "repo_name": "wg-value",
    "repo_git": "https://github.com/chaoss/wg-value",
    "repo_id": 25457,
    "cluster_content": 1,
    "message_count": 492,
    "issue_event_count": 999,
    "pull_request_event_count": 545,
    "msg_cluster_id": 3291
  },
  {
    "repo_name": "wg-risk",
    "repo_git": "https://github.com/chaoss/wg-risk",
    "repo_id": 25458,
    "cluster_content": 1,
    "message_count": 310,
    "issue_event_count": 735,
    "pull_request_event_count": 371,
    "msg_cluster_id": 3292
  },
  {
    "repo_name": "wg-common",
    "repo_git": "https://github.com/chaoss/wg-common",
    "repo_id": 25459,
    "cluster_content": 1,
    "message_count": 363,
    "issue_event_count": 813,
    "pull_request_event_count": 395,
    "msg_cluster_id": 3293
  },
  {
    "repo_name": "wg-app-ecosystem",
    "repo_git": "https://github.com/chaoss/wg-app-ecosystem",
    "repo_id": 25461,
    "cluster_content": 1,
    "message_count": 11,
    "issue_event_count": 59,
    "pull_request_event_count": 54,
    "msg_cluster_id": 3295
  },
  {
    "repo_name": "community-reports",
    "repo_git": "https://github.com/chaoss/community-reports",
    "repo_id": 25558,
    "cluster_content": 1,
    "message_count": 12,
    "issue_event_count": 37,
    "pull_request_event_count": 25,
    "msg_cluster_id": 3296
  },
  {
    "repo_name": "express",
    "repo_git": "https://github.com/expressjs/express.git",
    "repo_id": 25205,
    "cluster_content": 2,
    "message_count": 21841,
    "issue_event_count": 68,
    "pull_request_event_count": null,
    "msg_cluster_id": 3298
  },
  {
    "repo_name": "jquery",
    "repo_git": "https://github.com/jquery/jquery.git",
    "repo_id": 25206,
    "cluster_content": 2,
    "message_count": 26248,
    "issue_event_count": null,
    "pull_request_event_count": null,
    "msg_cluster_id": 3299
  },
  {
    "repo_name": "body-parser",
    "repo_git": "https://github.com/expressjs/body-parser.git",
    "repo_id": 25207,
    "cluster_content": 2,
    "message_count": 2293,
    "issue_event_count": 2800,
    "pull_request_event_count": 90,
    "msg_cluster_id": 3300
  },
  {
    "repo_name": "react",
    "repo_git": "https://github.com/facebook/react.git",
    "repo_id": 25208,
    "cluster_content": 2,
    "message_count": 65366,
    "issue_event_count": null,
    "pull_request_event_count": null,
    "msg_cluster_id": 3301
  },
  {
    "repo_name": "grimoirelab-elk",
    "repo_git": "https://github.com/chaoss/grimoirelab-elk",
    "repo_id": 25431,
    "cluster_content": 3,
    "message_count": 2738,
    "issue_event_count": 6040,
    "pull_request_event_count": 4793,
    "msg_cluster_id": 3303
  },
  {
    "repo_name": "grimoirelab-perceval",
    "repo_git": "https://github.com/chaoss/grimoirelab-perceval",
    "repo_id": 25432,
    "cluster_content": 3,
    "message_count": 4233,
    "issue_event_count": 5692,
    "pull_request_event_count": 3736,
    "msg_cluster_id": 3304
  },
  {
    "repo_name": "grimoirelab-kingarthur",
    "repo_git": "https://github.com/chaoss/grimoirelab-kingarthur",
    "repo_id": 25434,
    "cluster_content": 3,
    "message_count": 274,
    "issue_event_count": 577,
    "pull_request_event_count": 399,
    "msg_cluster_id": 3306
  },
  {
    "repo_name": "grimoirelab-sirmordred",
    "repo_git": "https://github.com/chaoss/grimoirelab-sirmordred",
    "repo_id": 25437,
    "cluster_content": 3,
    "message_count": 1366,
    "issue_event_count": null,
    "pull_request_event_count": 2230,
    "msg_cluster_id": 3309
  },
  {
    "repo_name": "grimoirelab-perceval-mozilla",
    "repo_git": "https://github.com/chaoss/grimoirelab-perceval-mozilla",
    "repo_id": 25439,
    "cluster_content": 3,
    "message_count": 157,
    "issue_event_count": 310,
    "pull_request_event_count": 230,
    "msg_cluster_id": 3311
  },
  {
    "repo_name": "grimoirelab-perceval-puppet",
    "repo_git": "https://github.com/chaoss/grimoirelab-perceval-puppet",
    "repo_id": 25441,
    "cluster_content": 3,
    "message_count": 53,
    "issue_event_count": 159,
    "pull_request_event_count": 142,
    "msg_cluster_id": 3313
  },
  {
    "repo_name": "grimoirelab-manuscripts",
    "repo_git": "https://github.com/chaoss/grimoirelab-manuscripts",
    "repo_id": 25442,
    "cluster_content": 3,
    "message_count": 538,
    "issue_event_count": 1120,
    "pull_request_event_count": 756,
    "msg_cluster_id": 3314
  },
  {
    "repo_name": "grimoirelab-toolkit",
    "repo_git": "https://github.com/chaoss/grimoirelab-toolkit",
    "repo_id": 25444,
    "cluster_content": 3,
    "message_count": 140,
    "issue_event_count": 271,
    "pull_request_event_count": 187,
    "msg_cluster_id": 3279
  },
  {
    "repo_name": "grimoirelab-perceval-opnfv",
    "repo_git": "https://github.com/chaoss/grimoirelab-perceval-opnfv",
    "repo_id": 25445,
    "cluster_content": 3,
    "message_count": 58,
    "issue_event_count": 169,
    "pull_request_event_count": 147,
    "msg_cluster_id": 3280
  },
  {
    "repo_name": "lodash",
    "repo_git": "https://github.com/lodash/lodash.git",
    "repo_id": 25204,
    "cluster_content": 4,
    "message_count": 19160,
    "issue_event_count": null,
    "pull_request_event_count": null,
    "msg_cluster_id": 3297
  },
  {
    "repo_name": "augur",
    "repo_git": "https://github.com/chaoss/augur",
    "repo_id": 25440,
    "cluster_content": 5,
    "message_count": 2681,
    "issue_event_count": 12794,
    "pull_request_event_count": 1300,
    "msg_cluster_id": 3312
  },
  {
    "repo_name": "augur-license",
    "repo_git": "https://github.com/chaoss/augur-license",
    "repo_id": 25460,
    "cluster_content": 5,
    "message_count": 6,
    "issue_event_count": 61,
    "pull_request_event_count": 53,
    "msg_cluster_id": 3294
  }
]

function drawChart () {

  
  // Set the columns for the Google Chart in the first line of the array
//   var messagesArray = [['cluster_content','message_count' ]]; 
//   // Loop through the JSON array, set up the value pair & push to the end of messagesArray
//   for(i=0; i<json.length; i++) {
//     messagesArray.push([json[i].cluster_content, json[i].message_count]);
//   }
var messagesArray = [['cluster_content','message_count','activity-level' ]]; 
  // Loop through the JSON array, set up the value pair & push to the end of messagesArray
  for(i=0; i<json.length; i++) {
    console.log(i);
    messagesArray.push([json[i].cluster_content, json[i].message_count, json[i].issue_event_count + json[i].pull_request_event_count ]);
  }
 
  // Set the Google Chart options (title, width, height, and colors can be set)
  var options = {
    width: 900,
    series: {
      0: {targetAxisIndex: 0},
      1: {targetAxisIndex: 1}
    },
    title: 'Cluster-Content Activity Level',

    vAxes: {
      // Adds titles to each axis.
      0: {title: 'Activity Level'},
      1: {title: 'pull_request events issue_event'},
      
    },
    hAxes: {
      0: {title: 'Cluster Ordinal'}
    }

  };
  
  // Convert messagesArray into the DataTable that Google Charts needs and put it in a var
  var data = google.visualization.arrayToDataTable(messagesArray)

  //var chart = new google.charts.ScatterChart(document.getElementById('scatterchart_material'));

  var chart = new google.visualization.ScatterChart(document.getElementById('scatterchart_material'));
  chart.draw(data, options);
  //chart.draw(data, google.charts.convertOptions(options));
}