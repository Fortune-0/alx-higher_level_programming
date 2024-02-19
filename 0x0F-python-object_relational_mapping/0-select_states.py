#!/usr/bin/python3
"""Module that lists all states from MySQl database.
"""
import sys
import MySQLdb

def list_states(username, password, database):
    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port= 3306, user=username, passwd=password, db=database)
    c=db.cursor()
    
    #execute the SQL query to fetch all states
    c.execute(r'SELECT state FROM states')
    
    # Fetch all the rows in a list of lists
    rows = c.fetchall()
    
    # print the results 
    for row in rows:
        print(row),
        
    # close the database and connection
    db.close()
    
# Example usage
if __name__ == "__main__":
    username = sys.argv[1]
    password  = sys.argv[2]
    database = sys.argv[3]
    
    list_states(username, password, database)