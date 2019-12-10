import { Component,ViewChild, OnInit } from '@angular/core';
import { ApiService } from '../api.service';
import { MatPaginator, MatTableDataSource, MatSort } from '@angular/material';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-messages',
  templateUrl: './messages.component.html',
  styleUrls: ['./messages.component.css']
})
export class MessagesComponent implements OnInit {
  dataSource = new MatTableDataSource();
  displayedColumns = ['cntrb_id','messages'];
  
  @ViewChild(MatPaginator,{static: false}) paginator: MatPaginator;
  @ViewChild(MatSort,{static: false}) sort: MatSort;
  erro:any;

  urlGroupId: string = this.route.snapshot.paramMap.get('groupId');


  constructor(private route: ActivatedRoute, private apiService: ApiService) { 

  }

  ngOnInit() {

    this.apiService.getMessages(this.urlGroupId).subscribe(data=>{
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
