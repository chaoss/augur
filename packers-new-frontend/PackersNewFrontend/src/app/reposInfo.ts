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