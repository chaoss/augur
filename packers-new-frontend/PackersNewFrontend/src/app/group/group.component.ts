import { Component, OnInit } from '@angular/core';

import { ActivatedRoute } from '@angular/router';
import { Router } from '@angular/router';

import { RepoInfoService } from 'src/app/repo-info.service';
import { RepoGroupInfo, RepoInfo } from 'src/app/reposInfo';

@Component({
  selector: 'app-group',
  templateUrl: './group.component.html',
  styleUrls: ['./group.component.scss']
})
export class GroupComponent implements OnInit {

  repoGroupId;
  repoGroupName;
  repoList;

  constructor(private activatedRoute: ActivatedRoute, private repoInfoService: RepoInfoService, private router: Router) { 
    this.repoGroupId = this.activatedRoute.snapshot.params['rgId'];
  }

  ngOnInit(): void {
    this.getReposInGroup();
  }

  getReposInGroup(): void {
    this.repoInfoService.getReposInGroup(this.repoGroupId).subscribe(data => {
      this.repoList = data;

      if(data.length == 0){
        this.router.navigate(["pagenotfound"]);
      }
      this.repoInfoService.getGroups().subscribe(data => {
        for(let i=0;i<data.length;i++){
          if(data[i].repo_group_id == this.repoGroupId){
            this.repoGroupName = data[i].rg_name;
            break;
          }
        }
      });
    });
  }
}
