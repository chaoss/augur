import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

import { RepoInfo, RepoCodeChanges, RepoPullRequests, RepoGroupInfo, RepoCommitters, RepolinesAdded } from './reposInfo';

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

  getGroups(): Observable<RepoGroupInfo[]> {
    return this.http.get<RepoGroupInfo[]>(this.url + '/repo-groups');
  }

  getReposInGroup(repo_group_id: number): Observable<RepoGroupInfo[]> {
    return this.http.get<RepoGroupInfo[]>(this.url + `/repo-groups/${repo_group_id}/repos`);
  }

  getRepoCodeChanges(repo_id: number): Observable<RepoCodeChanges[]> {
    return this.http.get<RepoCodeChanges[]>(this.url + `/repos/${repo_id}/code-changes`);
  }

  getRepoPullRequests(repo_id: number): Observable<RepoPullRequests[]> {
    return this.http.get<RepoPullRequests[]>(this.url + `/repos/${repo_id}/reviews`);
  }

  getRepoCommitters(repo_id: number): Observable<RepoCommitters[]> {
    return this.http.get<RepoCommitters[]>(this.url + `/repos/${repo_id}/committers`); 
  }

  getlinesAdded(repo_id: number): Observable<RepolinesAdded[]> {
    return this.http.get<RepolinesAdded[]>(this.url + `/repos/${repo_id}/code-changes-lines`);
  }
}
