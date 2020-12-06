import { Component, OnInit } from '@angular/core';

export interface PeriodicElement {
  name: string;
  position: number;
  weight: number;
  symbol: number;
}

const ELEMENT_DATA: PeriodicElement[] = [
  {position: 1, name: 'Competitors', weight: 1.0079, symbol: 609},
  {position: 2, name: 'Competitors', weight: 4.0026, symbol: 500},
  {position: 3, name: 'Competitors', weight: 6.941, symbol: 456},
  {position: 4, name: 'Competitors', weight: 9.0122, symbol: 264},
  {position: 5, name: 'Competitors', weight: 10.811, symbol: 123},
  {position: 6, name: 'Competitors', weight: 12.0107, symbol: 647},
  {position: 7, name: 'Competitors', weight: 14.0067, symbol: 342},
  {position: 8, name: 'Competitors', weight: 15.9994, symbol: 856},
  {position: 9, name: 'Competitors', weight: 18.9984, symbol: 354},
  {position: 10, name: 'Competitors', weight: 20.1797, symbol: 264},
];

@Component({
  selector: 'app-repo-list',
  templateUrl: './repo-list.component.html',
  styleUrls: ['./repo-list.component.scss']
})
export class RepoListComponent implements OnInit {

  displayedColumns: string[] = ['position', 'name', 'weight', 'symbol'];
  dataSource = ELEMENT_DATA;

  constructor() { }

  ngOnInit(): void {
  }

}
