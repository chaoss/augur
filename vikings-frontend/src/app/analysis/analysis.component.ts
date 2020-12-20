import { Component, OnInit,Input } from '@angular/core';
import { HttpHeaders } from '@angular/common/http';
import { HttpClient } from '@angular/common/http';
import { ActivatedRoute } from '@angular/router';


declare var Plotly: any


@Component({
  selector: 'app-analysis',
  templateUrl: './analysis.component.html',
  styleUrls: ['./analysis.component.css']
})
export class AnalysisComponent implements OnInit {

  public repo_id:any;

  //commit plot
  public commit_dates:any;
  public commit_nums:any;


  constructor(public http: HttpClient, private route: ActivatedRoute) { }

  ngOnInit(): void {
    //get repo ID from user selection from repos component
    this.repo_id=this.route.snapshot.paramMap.get('repo_id');
    console.log(this.repo_id)


    //pull data needed to display commits per day
    this.getCommitData(this.repo_id)
  }





  getCommitData(repo_id){
      const customheaders= new HttpHeaders()
            .set('Content-Type', 'application/json');
  
        this.http.post("http://localhost:5000/getcommits",JSON.stringify(repo_id), {headers: customheaders}).subscribe(

        response=> {
          console.log(response)

          //x and y axis variables for chart
          this.commit_dates=response[0];
          this.commit_nums=response[1]; 
  
          //create chart
          this.commitsPlot()
  
  
  
        },
        error => {
          console.log(error)
        }
      )
      
    }
  
  commitsPlot(){
    //create div 
    var commits = document.getElementById('commits');

    //set x and y axis with commit data
    var trace1 = {
      x: this.commit_dates,
      y: this.commit_nums,
      type: 'scatter'
    };
    var data = [trace1];
    
    var layout = {
      xaxis:{
        rangeslider: {range: ['2020-01-01', '2021-01-01']},
        type: 'date'
      },
      yaxis: {
        title: {
          text: 'Number of Commits'
        }
      },
      margin:{
        l:50, 
        r:20, 
        t:40, 
        b:30, 
        pad:0
      }
      
    };
    
    Plotly.newPlot(commits, data, layout);


  }
  





  

}
