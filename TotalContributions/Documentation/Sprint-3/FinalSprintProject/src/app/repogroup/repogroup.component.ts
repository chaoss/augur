import { Component,ViewChild,OnInit } from '@angular/core';
import { ApiService } from '../api.service';
import { MatPaginator, MatTableDataSource, MatSort } from '@angular/material';


@Component({
  selector: 'app-repogroup',
  templateUrl: './repogroup.component.html',
  styleUrls: ['./repogroup.component.css']
})
export class RepogroupComponent implements OnInit {
  dataSource = new MatTableDataSource();
  displayedColumns = ['repo_group_id', 'rg_name', 'rg_last_modified','data_source','data_collection_date'];
  @ViewChild(MatPaginator,{static: false}) paginator: MatPaginator;
  @ViewChild(MatSort,{static: false}) sort: MatSort;
  erro:any;

  constructor(private apiService: ApiService) { 
    this.getter();
  }
  ngOnInit() {


  }

  getter() {
    this.apiService.getGroups().subscribe(data=>{
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
