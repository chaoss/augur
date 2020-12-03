import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

import { RepoInfo, RepoCodeChanges, RepoPullRequests } from './reposInfo';

@Injectable({
  providedIn: 'root'
})
export class RepoInfoService {

  url: string = "http://zephyr.osshealth.io:5222/api/unstable";

  constructor(
    private http: HttpClient
  ) { }

  /* TODO: add error checking */
  getRepos(): Observable<RepoInfo[]> {
    return this.http.get<RepoInfo[]>(this.url + "/repos");
  }

  getRepoCodeChanges(repo_id: number): Observable<RepoCodeChanges[]> {
    return this.http.get<RepoCodeChanges[]>(this.url + `/repos/${repo_id}/code-changes`);
  }

  getRepoPullRequests(repo_id: number): Observable<RepoPullRequests[]> {
    return this.http.get<RepoPullRequests[]>(this.url + `/repos/${repo_id}/reviews`);
  }
}
