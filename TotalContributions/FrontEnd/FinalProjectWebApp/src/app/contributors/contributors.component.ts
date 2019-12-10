import { Component,ViewChild, OnInit } from '@angular/core';
import { ApiService } from '../api.service';
import { MatPaginator, MatTableDataSource, MatSort } from '@angular/material';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-contributors',
  templateUrl: './contributors.component.html',
  styleUrls: ['./contributors.component.css']
})
export class ContributorsComponent implements OnInit {
  dataSource = new MatTableDataSource();
  displayedColumns = ['cntrb_company', 'counter'];
  
  @ViewChild(MatPaginator,{static: false}) paginator: MatPaginator;
  @ViewChild(MatSort,{static: false}) sort: MatSort;
  message = new MatTableDataSource();
  erro:any;

  urlGroupId: string = this.route.snapshot.paramMap.get('groupId');


  constructor(private route: ActivatedRoute, private apiService: ApiService) { 

  }

  ngOnInit() {
    this.apiService.getContributors(this.urlGroupId).subscribe(data=>{
      this.dataSource = new MatTableDataSource(data);
      console.log(this.dataSource);
      this.dataSource.paginator = this.paginator;
      this.dataSource.sort= this.sort;
  
  },(error:any)=>{
      this.erro = error;
      console.error("Error:",error);
  });
  
  }


}


