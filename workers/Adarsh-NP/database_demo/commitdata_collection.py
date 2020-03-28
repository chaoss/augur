import os, json, requests
from commits import *
from flask import Flask
# from sqlalchemy import create_engine
# from sqlalchemy.orm import scoped_session, sessionmaker



app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://adarsh:adarsh@localhost:5432/commits"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


def main():
    res = requests.get("https://gitlab.com/api/v4/projects/17612426/repository/commits/master")
    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")
    data = res.json()
    
    Commits = commits(short_id=data['short_id'], created_at=data['committed_date'], title=data['title'], message=data['message'], author_name=data['author_name'],
                author_email=data['author_email'], committer_name=data['committer_name'], committer_email=data['committer_email'])
    db.session.add(Commits)
    db.session.commit()

print("latest data retrieved")
print("added the data to the table commits")



if __name__ == "__main__":
    with app.app_context():
        main()