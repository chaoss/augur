import { Component, OnInit } from '@angular/core';

interface Repo {
  value: string;
}

export interface PeriodicElement {
  name: string;
  url: number;
  totalCommit: number;
  totalIssue: number;
}

const ELEMENT_DATA: PeriodicElement[] = [
  {url: 1, name: 'Competitors', totalCommit: 1.0079, totalIssue: 609},
  {url: 2, name: 'Competitors', totalCommit: 4.0026, totalIssue: 500},
  {url: 3, name: 'Competitors', totalCommit: 6.941, totalIssue: 456},
  {url: 4, name: 'Competitors', totalCommit: 9.0122, totalIssue: 264},
  {url: 5, name: 'Competitors', totalCommit: 10.811, totalIssue: 123},
  {url: 6, name: 'Competitors', totalCommit: 12.0107, totalIssue: 647},
  {url: 7, name: 'Competitors', totalCommit: 14.0067, totalIssue: 342},
  {url: 8, name: 'Competitors', totalCommit: 15.9994, totalIssue: 856},
  {url: 9, name: 'Competitors', totalCommit: 18.9984, totalIssue: 354},
  {url: 10, name: 'Competitors', totalCommit: 20.1797, totalIssue: 264},
];

@Component({
  selector: 'app-repo-list',
  templateUrl: './repo-list.component.html',
  styleUrls: ['./repo-list.component.scss']
})
export class RepoListComponent implements OnInit {

  repos: Repo[] = [
    {value: 'Competitors'},
    {value: 'Zephyr-RTOS'}
  ];

  displayedColumns: string[] = ['url', 'name', 'totalCommit', 'totalIssue'];
  dataSource = ELEMENT_DATA;

  constructor() { }

  ngOnInit(): void {
  }

}
