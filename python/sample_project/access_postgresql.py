#!/usr/bin/python3
import psycopg2




try:
    connect_str = "dbname='template1' user='dbuser' host='localhost' " + \
                  "password='dbpass'"
    conn = psycopg2.connect(connect_str)
except:
    print ("I am unable to connect to the database")

cur = conn.cursor()

sql='SELECT name FROM users' 
try:
    cur.execute(sql)
    for row in cur:
        print(row)
except:
    print ("I can't SELECT from users")

for row in cur:
    print(row)
