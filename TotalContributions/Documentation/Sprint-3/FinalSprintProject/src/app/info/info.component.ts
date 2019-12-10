import { Component,ViewChild, OnInit } from '@angular/core';
import { ApiService } from '../api.service';
import { MatPaginator, MatTableDataSource, MatSort } from '@angular/material';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-info',
  templateUrl: './info.component.html',
  styleUrls: ['./info.component.css']
})
export class InfoComponent implements OnInit {

  dataSource = new MatTableDataSource();
  displayedColumns = ['repo_id', 'repo_name', 'email', 'commits'];
  
  @ViewChild(MatPaginator,{static: false}) paginator: MatPaginator;
  @ViewChild(MatSort,{static: false}) sort: MatSort;
  erro:any;

  urlGroupId: string = this.route.snapshot.paramMap.get('groupId');

  urlRepoId: string = this.route.snapshot.paramMap.get('repoId');

  constructor(private route: ActivatedRoute, private apiService: ApiService) { 

  }
  ngOnInit() {
    this.apiService.getCommits(this.urlGroupId,this.urlRepoId).subscribe(data=>{
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
