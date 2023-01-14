import mysql.connector as mysql

# Connect to MySQL server
HOST = ""
DATABASE = ""
USER = ""
PASSWORD = ""

db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
cursor_db_connection = db_connection.cursor()
print("Connected to:", db_connection.get_server_info())

Table=""

cursor_db_connection.execute("Select * from "+Table)
recordsNotes = cursor_db_connection.fetchall()

alreadyInserted=False;
with open('input.txt') as f:
    lines = f.readlines()
    for line in lines:
        line=line.replace("\r","").replace("\n","").replace("\t","")
        if(line!="\n" and line!="\r" and line!=" " and line.__len__()>0):
            for notes in recordsNotes:
                if(notes[1]==line):
                    print("Already inserted")
                    alreadyInserted=True
                    continue
            if(not(alreadyInserted)):
                cursor_db_connection.execute("INSERT INTO "+Table+" (Content) VALUES ('"+line.replace("'", "''" )+"')")
                db_connection.commit()
                print("Inserted")
            alreadyInserted=False

print("Operation completed")
print()

