import { Component, OnInit,Input } from '@angular/core';
import { HttpHeaders } from '@angular/common/http';
import { HttpClient } from '@angular/common/http';
import { ActivatedRoute } from '@angular/router';


@Component({
  selector: 'app-analysis',
  templateUrl: './analysis.component.html',
  styleUrls: ['./analysis.component.css']
})
export class AnalysisComponent implements OnInit {

  public repo_id:any;


  constructor(public http: HttpClient, private route: ActivatedRoute) { }

  ngOnInit(): void {

    this.repo_id=this.route.snapshot.paramMap.get('repo_id');
    console.log("MADE IT")
    console.log(this.repo_id)
  }

}
