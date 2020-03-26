'''Simple python script to interact with the apis'''

import requests

def main():
    res = requests.get("https://gitlab.com/api/v4/projects/17612426/repository/commits/master")
    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")
    data = res.json()
    print(res.text)
    commit_data = {"id":data['short_id'], "title":data['title'], "message":data['message'], "committer":data['committer_name'], "date":data['committed_date']}
    print(f"The latest commit was made by {commit_data['committer']} on {commit_data['date']} and has id: {commit_data['id']} and is titled {commit_data['title']}")
    
    

if __name__ == "__main__":
    main()


