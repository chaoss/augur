import { Component, OnInit, Input } from '@angular/core';
import { DataService } from '../../../data.service';

import { ChartOptions, ChartType, ChartDataSets } from 'chart.js';
import { Label, Color } from 'ng2-charts';

@Component({
  selector: 'app-commits-over-time',
  templateUrl: './commits-over-time.component.html',
  styleUrls: ['./commits-over-time.component.css']
})
export class CommitsOverTimeComponent implements OnInit {

  changes: any;

  @Input() urlGroupId: string;
  @Input() urlRepoId: string;

  public barChartData: ChartDataSets[];
  public barChartLabels: Label[];
  public barChartOptions: ChartOptions = {
    responsive: true,
    scales: {
      yAxes: [{ id: 'y-axis-1', type: 'linear', position: 'left', ticks: { min: 0 } }]
    }
  };
  public barChartColors: Color[] = [
    {
      borderColor: 'black',
      backgroundColor: 'rgba(255,0,0,1)',
    },
  ];
  public barChartLegend = false;
  public barChartType = 'bar';
  public barChartPlugins = [];

  constructor(private dataService: DataService) { }

  ngOnInit() {
    this.dataService.getInfo(this.urlGroupId, this.urlRepoId, 'code-changes').subscribe(data => {
      this.changes = data;

      this.barChartLabels = [];
      this.barChartData = [];

      for(let i = 0; i < this.changes.length; i++){
        this.barChartLabels.push(this.changes[i].date.slice(0,10));
        this.barChartData.push(this.changes[i].commit_count);
      }

    //   let date = [];
    //   let commit_count = [];
    //   let commit_rate =[];
    //   var i = 0;
      
    //   this.changes.forEach(commit => {
    //     commit_rate = commit.date
    //     date[i] = commit_rate.slice(0,10)
    //     commit_count[i] = commit.commit_count
    //     i++
    // })
    //   console.log(commit_count);
    //   this.lineChartData = [{ data: [commit_count[0], commit_count[1], commit_count[2]], label: 'Series A' }]
    //   this.lineChartLabels = [date[0], date[1], date[2]]
    }
    );
  }

}
