import requests
import json
from urllib.parse import urlparse
from copy import copy, deepcopy
from pandas.io.json import json_normalize
import pandas as pd
import psycopg2
import sqlalchemy as s


def json_req(url):
  #replace this with your token
  token="c7c7e3457f79ab8b40e585fc30f10b492ee0aea6"
  response=requests.get(url,headers={'Authorization': 'token %s' % token})
  json_data=response.json()
  return(json_data)
def con_info(url):
#helper function to run all api calls
  usr_id=[]
  usr_login=[]
  json_data=json_req(url)
  df=json_normalize(json_data)
  for product in json_data:
    usr_id.append(product['id'])
    usr_login.append(product['login'])
  r=zip(usr_login,usr_id)
  x=list(r)
  return(usr_login)


def update_sql(contributor,repo_id,contributor_id,cursor):
  i=0
  #checks to see if this contributor has already been passed through, if it has it will return a 1 which states that it already exists so there is no need to update or insert this data
  for x in contributor_id:
    if contributor_id[i]==contributor['login']:
      return(1)
    i+=1
  cntrb = {
           "cntrb_login": contributor['login'],
            "cntrb_created_at": contributor['created_at'],
            "cntrb_email": contributor['email'],
            "cntrb_company": contributor['company'],
            "cntrb_location": contributor['location'],
            # "cntrb_type": , dont have a use for this as of now ... let it default to null
         #   "cntrb_canonical": contributor['canonical_email'], could not find this data from contributors api response
            "gh_user_id": contributor['id'],
            "gh_login": contributor['login'],
            "gh_url": contributor['url'],
            "gh_html_url": contributor['html_url'],
            "gh_node_id": contributor['node_id'],
            "gh_avatar_url": contributor['avatar_url'],
            "gh_gravatar_id": contributor['gravatar_id'],
            "gh_followers_url": contributor['followers_url'],
            "gh_following_url": contributor['following_url'],
            "gh_gists_url": contributor['gists_url'],
            "gh_starred_url": contributor['starred_url'],
            "gh_subscriptions_url": contributor['subscriptions_url'],
            "gh_organizations_url": contributor['organizations_url'],
            "gh_repos_url": contributor['repos_url'],
            "gh_events_url": contributor['events_url'],
            "gh_received_events_url": contributor['received_events_url'],
            "gh_type": contributor['type'],
            "gh_site_admin": contributor['site_admin'],

            }
  table=pd.DataFrame(list(cntrb.items()))
#since the my sql functions arent working. If you print the table it will show you what would have been updated and or inserted into your database. Basically just prints each contributor of all your repos once

#this is where the update/insert function would be but I couldn't get it to work
 # insert_statement = postgresql.insert(my_table).values(df.to_dict(orient='records'))
  #upsert_statement = insert_statement.on_conflict_do_update(
  #  index_elements=['id'],
  #  set_={c.key: c for c in insert_statement.excluded if c.key != 'id'})
#conn.execute(upsert_statement)

  #cursor.execute


repoURL= "https://api.github.com/users/gabe-heim"+"/repos"
json_data = json_req(repoURL)
contributorsURL="https://api.github.com/users/"
contributor_id=[]
repo_url=[]
repo_name=[]
hold=[]
x=0
i=0
j=0
#establish connection to database
try:
  #Replace user with your databases username,dbname with the name of the database,host with your databases host,and password with the password to the database
  conn = psycopg2.connect("dbname='DATABASE_NAME' user='USER_NAME' host='localhost' password='DATABASE_PASSWORD'")
except:
    print "I am unable to connect to the database"
cur = conn.cursor()

for product in json_data:
 #grab repo name and contributors urls
  repo_url.append(product['contributors_url'])
  repo_name.append(product['name'])


for contributors in repo_url:
#break data down to first get repo name and then it should pass all the contributors info into a function that will update or insert it into the database
  con=copy(con_info(repo_url[i]))
  for h in con:

    hold=json_req(contributorsURL+con[j])

    x=update_sql(hold,repo_name[i],contributor_id,cur)
    if x !=1:
      contributor_id.append(hold['login'])

    hold=None


    j+=1

  j=0
  i+=1
