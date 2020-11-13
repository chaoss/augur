import { Component, OnInit } from '@angular/core';

import { RepoInfoService } from 'src/app/repo-info.service'
import { RepoInfo } from 'src/app/reposInfo';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss']
})
export class DashboardComponent implements OnInit {

  repos: RepoInfo[];

  constructor(private repoInfoService: RepoInfoService) { }

  ngOnInit(): void {
    this.getRepoNames();
  }

  getRepoNames(): void {
    this.repoInfoService.getRepos().subscribe(data => this.repos = data);
  }

}
