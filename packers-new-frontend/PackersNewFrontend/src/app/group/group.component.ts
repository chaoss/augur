import { Component, OnInit } from '@angular/core';

import { ActivatedRoute } from '@angular/router';
import { Router } from '@angular/router';

@Component({
  selector: 'app-group',
  templateUrl: './group.component.html',
  styleUrls: ['./group.component.scss']
})
export class GroupComponent implements OnInit {

  repoGroupId;
  repoList;

  constructor(private activatedRoute: ActivatedRoute) { 
    this.repoGroupId = this.activatedRoute.snapshot.params['rgId'];
  }

  ngOnInit(): void {
  }

}
