#!/usr/bin/python3
"""Module that list all the states from the hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Get MySQL credentials search name from command-line arguments
    # and connect to MySQL servers
    
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    
    # execute the SQL query to retrive the specific name
    c.execute(*SELECT * \
        FROM `states` \
            WHERE BINARY `name` = '{}'".format(sys.argv[4]))
    # Fetch all rows and print the states
    [print(state) for state in c.fetchall()]