import { Component, OnInit } from '@angular/core';

import { DataService } from '../data.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-detail-page',
  templateUrl: './detail-page.component.html',
  styleUrls: ['./detail-page.component.css']
})
export class DetailPageComponent implements OnInit {

  contributors: any;

  urlGroupId: string = this.route.snapshot.paramMap.get('groupId');

  urlRepoId: string = this.route.snapshot.paramMap.get('repoId');

  selectedInfo: string = '';

  constructor(private route: ActivatedRoute, private dataService: DataService) { }

  ngOnInit() {

    this.dataService.getInfo(this.urlGroupId, this.urlRepoId, 'contributors').subscribe(data => {
      this.contributors = data;
  
    }
    );

  }

}