import { Component, OnInit } from '@angular/core';

import { ActivatedRoute } from '@angular/router';

import { RepoInfoService } from 'src/app/repo-info.service'
import { Metric } from 'src/app/reposInfo';
import { Router } from '@angular/router';

@Component({
  selector: 'app-repo',
  templateUrl: './repo.component.html',
  styleUrls: ['./repo.component.scss']
})
export class RepoComponent implements OnInit {

  repoId: number;
  repoName: string;

  commitMetric: Metric = Metric.commits;
  pullRequestMetric: Metric = Metric.pullRequests;
  committersMetric: Metric = Metric.committers;
  linesAddedMetric: Metric = Metric.linesAdded;


  constructor(private activatedRoute: ActivatedRoute, private repoInfoService: RepoInfoService, private router: Router) {
   }

   ngOnInit(): void {
    this.repoId = this.activatedRoute.snapshot.params['repoId'];
    this.repoInfoService.getRepoCodeChanges(this.repoId)
    .subscribe(res => {
      if(res.length == 0){
        this.router.navigate(["pagenotfound"]);
      }
      this.repoName = res[0].repo_name;
    });
  }

}
