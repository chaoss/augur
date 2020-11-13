import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { RepoInfo } from './reposInfo';

@Injectable({
  providedIn: 'root'
})
export class RepoInfoService {

  url = "http://zephyr.osshealth.io:5222/api/unstable/repos";

  constructor(
    private http: HttpClient
  ) { }

  getRepos(): Observable<RepoInfo[]> {
    return this.http.get<RepoInfo[]>(this.url);
  }
}
