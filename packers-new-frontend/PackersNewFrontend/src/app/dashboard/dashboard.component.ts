import { Component, OnInit } from '@angular/core';

import { RepoInfoService } from 'src/app/repo-info.service'
import { RepoGroupInfo, RepoInfo } from 'src/app/reposInfo';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss']
})
export class DashboardComponent implements OnInit {

  repoGroups: RepoGroupInfo[];

  constructor(private repoInfoService: RepoInfoService) { }

  ngOnInit(): void {
    this.getRepoGroups();
  }

  getRepoGroups(): void {
    this.repoInfoService.getGroups().subscribe(data => this.repoGroups = data);
  }

}
