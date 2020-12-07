import { Component, OnInit } from '@angular/core';

import { ActivatedRoute } from '@angular/router';
import { Router } from '@angular/router';

import { RepoInfoService } from 'src/app/repo-info.service'
import { RepoGroupInfo, RepoInfo } from 'src/app/reposInfo';


@Component({
  selector: 'app-repo',
  templateUrl: './repo.component.html',
  styleUrls: ['./repo.component.scss']
})
export class RepoComponent implements OnInit {

  repoId;

  constructor(private activatedRoute: ActivatedRoute, private repoInfoService: RepoInfoService) {
    this.repoId = this.activatedRoute.snapshot.params['repoId'];
   }

   ngOnInit(): void {
    
  }

}
