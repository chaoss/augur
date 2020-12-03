import { Component, OnInit } from '@angular/core';
import { HttpHeaders } from '@angular/common/http';
import { HttpClient } from '@angular/common/http';


@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  public repogroups:any;

  constructor(public http: HttpClient) { }

  ngOnInit(): void {

    this.getRepoGroups();
  }


  getRepoGroups(){
    const customheaders= new HttpHeaders()
          .set('Content-Type', 'application/json');

    this.http.get("http://zephyr.osshealth.io:5222/api/unstable/repo-groups", {headers: customheaders}).subscribe(
      response=> {
        console.log(response)
        this.repogroups=response;




      },
      error => {
        console.log(error)
      }
    )
    
	}




}
