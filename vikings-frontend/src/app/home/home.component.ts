import { Component, OnInit } from '@angular/core';
import { HttpHeaders } from '@angular/common/http';
import { HttpClient } from '@angular/common/http';

//this works instead of an import statement, I don't know why
declare var Plotly: any

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  public repogroups:any;


  constructor(public http: HttpClient) { }

  ngOnInit(): void {

    this.getRepoGroups();

    //graph plotting
    var TESTER = document.getElementById('tester');
    var month = ['Jan', 'Feb', 'Mar', 'Apr', 'May','Jun','Jul','Aug','Sept','Oct','Nov','dec'];

    var base = {
      x: month,
      y: [0,0,0,0,0,0,0,0,0,0,0,0],
      name: '',
      type: 'bar',
      showlegend: false
    }

    var trace1 = {
      x: [month[0], month[1], month[2],month[5]],
      y: [20, 14, 23,12],
      name: 'Contributor1',
      type: 'bar'
    };
    
    var trace2 = {
      x: [month[2], month[3], month[5],month[7]],
      y: [12, 18, 29,30],
      name: 'Contributor2',
      type: 'bar'
    };
    
    var trace3 = {
      x: [month[8], month[9], month[10],month[11]],
      y: [20, 40,10,15],
      name: 'Contributor3',
      type: 'bar'
    };
    
    var data = [base, trace1, trace2, trace3];
    
    var layout = {barmode: 'stack'};
    
    Plotly.newPlot(TESTER, data, layout);
  }


  getRepoGroups(){
    const customheaders= new HttpHeaders()
          .set('Content-Type', 'application/json');

    this.http.get("http://zephyr.osshealth.io:5222/api/unstable/repo-groups", {headers: customheaders}).subscribe(
      response=> {
        console.log(response)
        this.repogroups=response;




      },
      error => {
        console.log(error)
      }
    )
    
  }
  




}
