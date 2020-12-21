import psycopg2
import os
import json
def connectToDb():

    conn = psycopg2.connect(host="vikings.sociallycompute.io", port = 5433, 
                            database="vikings_demo", 
                            user="augur", 
                            password="covidparty")
    return conn
