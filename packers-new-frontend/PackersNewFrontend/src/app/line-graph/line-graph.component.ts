import { Component, OnInit, Input } from '@angular/core';

import { RepoInfoService } from 'src/app/repo-info.service'
import { LineGraphService } from 'src/app/line-graph.service';
import { RepoCodeChanges, RepoPullRequests } from 'src/app/reposInfo';
import { LineGraphData } from 'src/app/lineGraphInterface';

import * as shape from 'd3';

@Component({
  selector: 'app-line-graph',
  templateUrl: './line-graph.component.html',
  styleUrls: ['./line-graph.component.scss']
})
export class LineGraphComponent implements OnInit {

  @Input() repoId: number;
  repoCodeChanges: RepoCodeChanges[];
  repoPullRequests: RepoPullRequests[];
  lineGraphData: LineGraphData[];
  view: any[] = [600, 400];

  // options
  legend: boolean = true;
  showLabels: boolean = true;
  animations: boolean = true;
  xAxis: boolean = true;
  yAxis: boolean = true;
  showYAxisLabel: boolean = true;
  showXAxisLabel: boolean = true;
  xAxisLabel: string = "Date";
  yAxisLabel: string = null;
  timeline: boolean = true;
  xAxisTickFormatting = this.lineGraphService.xAxisFormatMonth;
  curve = shape.curveMonotoneX; // curve makes graph look smooth

  colorScheme = {
    domain: ["#5AA454", "#E44D25", "#CFC0BB", "#7aa3e5", "#a8385d", "#aae3f5"]
  };

  constructor(private repoInfoService: RepoInfoService, private lineGraphService: LineGraphService) { }

  ngOnInit(): void {
    this.getRepoPullRequests();
  }

  /*******************************************************

    FUNCTION: getRepoCodeChanges(): void
  
    Once the repo code change data ( # of commits) 
    is recieved from the api, it formats it to be ready 
    to be graphed

    Currently using a hardcoded id in zephyr database

  *******************************************************/
  getRepoCodeChanges(): void { //west
    
    this.repoInfoService.getRepoCodeChanges(this.repoId).subscribe(data => {
      this.repoCodeChanges = data;

      console.log(data);

      var dates = this.repoCodeChanges.map(r => r.date);
      var counts = this.repoCodeChanges.map(r => r.commit_count);

      this.lineGraphData = new Array();


      /* inserts the series of points given by the api into the graph */
      // this.lineGraphData.push({
      //   name: "Commits",
      //   series: this.lineGraphService.formatLineGraphCounts(dates, counts)
      // });

      /* inserts a trailing average of the series of points by the given api into the graph */
      this.lineGraphData.push({
        name: "Commits",
        series: this.lineGraphService.formatLineGraphCountsAvg(dates, counts)
      });

      this.yAxisLabel = "Commits";

      console.log(this.lineGraphData);
      });
  }

  /*******************************************************

    FUNCTION: getRepoPullRequests(): void

    Once the repo code pull request data is recieved from the api, 
    it formats it to be ready to be graphed

    Currently using a hardcoded id in zephyr database

  *******************************************************/
  getRepoPullRequests(): void {
    
    this.repoInfoService.getRepoPullRequests(this.repoId).subscribe(data => {
      this.repoPullRequests = data;

      console.log(data);

      var dates = this.repoPullRequests.map(r => r.date);
      var counts = this.repoPullRequests.map(r => r.pull_requests);

      this.lineGraphData = new Array();

      /* inserts the series of points given by the api into the graph */
      // this.lineGraphData.push({
      //   name: "Commits",
      //   series: this.lineGraphService.formatLineGraphCounts(dates, counts)
      // });

      /* inserts a trailing average of the series of points by the given api into the graph */
      this.lineGraphData.push({
        name: "Pull Requests",
        series: this.lineGraphService.formatLineGraphCountsAvg(dates, counts)
      });

      this.yAxisLabel = "Pull Requests";

      console.log(this.lineGraphData);
      });
  }
}
