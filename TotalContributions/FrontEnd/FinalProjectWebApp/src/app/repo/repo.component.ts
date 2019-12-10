import { Component,ViewChild, OnInit } from '@angular/core';
import { ApiService } from '../api.service';
import { MatPaginator, MatTableDataSource, MatSort } from '@angular/material';

@Component({
  selector: 'repo',
  templateUrl: './repo.component.html',
  styleUrls: ['./repo.component.css']
})

export class RepoComponent implements OnInit {
  dataSource = new MatTableDataSource();
  displayedColumns = ['repo_name', 'repo_id', 'url', 'repo_group_id','commits_all_time','description'];
  @ViewChild(MatPaginator,{static: false}) paginator: MatPaginator;
  @ViewChild(MatSort,{static: false}) sort: MatSort;
  @ViewChild('canvas', {static: true}) private chartRef;
  erro:any;
  constructor(private apiService: ApiService) { 
    this.getter();
  }

  ngOnInit() {
  }
  getter() {
    this.apiService.getRepos().subscribe(data=>{
        this.dataSource = new MatTableDataSource(data);
        console.log(this.dataSource);
        this.dataSource.paginator = this.paginator;
        this.dataSource.sort= this.sort;
    },(error:any)=>{
        this.erro = error;
        console.error("Error:",error);
    });
 

  }

  onSearchClear(){
    this.dataSource.filter='';
  }

  
  applyFilter(filterValue: string){
    this.dataSource.filter = filterValue.trim().toLowerCase();
  }

  

}
