import { Component, OnInit } from '@angular/core';
import { HttpHeaders } from '@angular/common/http';
import { HttpClient } from '@angular/common/http';


@Component({
  selector: 'app-repos',
  templateUrl: './repos.component.html',
  styleUrls: ['./repos.component.css']
})
export class ReposComponent implements OnInit {



  public selected_group:any;


  constructor(public http: HttpClient) { }

  ngOnInit(): void {



  }




  getRepos(group){
    this.selected_group=group;
  }

}
