import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class ApiService {

constructor(private http: HttpClient) { }
private repourl ='http://augur.osshealth.io:5000/api/unstable/repos';

  getRepos(): Observable<any> {
    console.log("called getRepos"); 
    return this.http.get(this.repourl);
  }
  public getGroups(): Observable<any>{
    console.log("called getGroups");
    return this.http.get('http://augur.osshealth.io:5000/api/unstable/repo-groups')
  }

  public getCommits(rgid, rpid): Observable<any> {
      return this.http.get("http://augur.osshealth.io:5000/api/unstable/repo-groups/" + rgid + "/repos/" + rpid + "/top-committers")
    } 
  public getContributors(rgid): Observable<any> {
        return this.http.get("http://129.114.104.142:5000/api/unstable/repo-groups/"+rgid+"/contributors-by-company")

  }

  public getMessages(rgid): Observable<any> {
    return this.http.get("http://129.114.104.142:5000/api/unstable/repo-groups/"+rgid+"/messages-by-contributor")

}
}

