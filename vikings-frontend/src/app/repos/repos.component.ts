import { Component, OnInit,Input } from '@angular/core';
import { HttpHeaders } from '@angular/common/http';
import { HttpClient } from '@angular/common/http';
import { ActivatedRoute,Router } from '@angular/router';



@Component({
  selector: 'app-repos',
  templateUrl: './repos.component.html',
  styleUrls: ['./repos.component.css']
})
export class ReposComponent implements OnInit {



  public repo_group_id:any;


  //repos contains all repo data in json format
  //fields: rg_name, repo_name, repo_id, repo_git, issues_count, committers_count, commit_count 
  public repos:any;


  constructor(public http: HttpClient, private route: ActivatedRoute,private router: Router) { 


    this.repo_group_id=this.route.snapshot.paramMap.get('repo_group_id');

  }

  ngOnInit(): void {

  this.getRepo(this.repo_group_id);

  }



  //Pass rep_group_id and get repos that belong to repo group
  getRepo(repo_group_id){
    const customheaders= new HttpHeaders()
          .set('Content-Type', 'application/json');

      this.http.post("http://localhost:5000/getrepos",JSON.stringify(repo_group_id), {headers: customheaders}).subscribe(
      //this.http.get("http://localhost:5000/getrepos", {headers: customheaders}).subscribe(
      response=> {
        console.log(response)
        this.repos=response;
        console.log(this.repos)




      },
      error => {
        console.log(error)
      }
    )
    
  }
  


  getrepoID(index){


    console.log(this.repos[index].repo_id)
    this.router.navigate(['/analytics', {repo_id: this.repos[index].repo_id } ]);

  }



}
