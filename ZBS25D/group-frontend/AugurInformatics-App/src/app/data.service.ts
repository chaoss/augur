import { Injectable } from '@angular/core';
import {HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class DataService {

  constructor(private http: HttpClient) { }

  getGroups(){
    return this.http.get('https://cors-anywhere.herokuapp.com/http://augur.osshealth.io:5000/api/unstable/repo-groups/');
  }

  getRepos(groupId: string){
    return this.http.get('https://cors-anywhere.herokuapp.com/http://augur.osshealth.io:5000/api/unstable/repo-groups/' + groupId + '/repos/' );
  }

  //You can pass the url id to this function as a string a receive the data, so we don't have to write
  //a function for every endpoint
  getInfo(groupId: string, repoId: string, endpoint: string){
    return this.http.get('https://cors-anywhere.herokuapp.com/http://augur.osshealth.io:5000/api/unstable/repo-groups/'
     + groupId + '/repos/' + repoId + '/' + endpoint + '/' );
  } 

  //'pull-request-acceptance-rate' for that endpoint in getInfo

  //'issues-active' for that endpoint in getInfo




  

  // getIssues(){
  //   return this.http.get('http://augur.osshealth.io:5000/api/unstable/repo-groups/24/repos/25151/issues-active');
  // }
}
