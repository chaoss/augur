export enum Metric {
    pullRequests,
    commits,
    committers,
    linesAdded
}

export interface RepoInfo {
    base64_url: string;
    commits_all_time: string;
    description: string;
    issues_all_time: string;
    repo_id: number;
    repo_name: string;
    repo_status: string;
    rg_name: string;
    url: string;
}

export interface RepoGroupInfo {
    data_collection_date: string,
    data_source: string,
    repo_group_id: number,
    rg_description: string,
    rg_last_modified: string,
    rg_name: string,
    rg_recache: number,
    rg_type: string,
    rg_website: string,
    tool_source: string,
    tool_version: string 
}

export interface RepoCodeChanges {
    commit_count: number;
    date: string;
    repo_name: string;
    week: number;
    year: number;
}

export interface RepoPullRequests {
    date: string;
    pull_requests: number;
    repo_name: string;
}

export interface RepoCommitters {
    count: number;
    date: string;
    repo_name: string;
    rg_name: string;
}

export interface RepolinesAdded {
    added: number;
    date: string;
    removed: number;
    repo_name: string;
}