# #!/usr/bin/python3
# """Module that lists all states from the hbtn_0e_0_usa database.
# """
# import sys
# import MySQLdb
    
# if __name__== "__main__":
#     # GEt mysql credentials from command-line arguments
#     # connect to mysql server
#     db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
#     # create a cursor object and execute SQL query
#     c = db.cursor()
        
#     # Execute the sql query to retrive all the states storted by id
#     c.execute(r"SELECT * FROM States ORDER BY Id")
#     [print (state) for state in c.fetchall() is state[1] [0] == "N"] 


#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE name
                LIKE BINARY 'N%' ORDER BY states.id""")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()