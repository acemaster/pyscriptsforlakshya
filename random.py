# import MySQLdb

# txt=open('file.txt')
# ufid=txt.read()

# roll_number=raw_input("Enter the rollno: ")


# connection=MySQLdb.connect(host="",user="",passwd="",db="")
# cursor=connection.cursor()
# sql="insert into map values(" +"'"+ str(roll_number)+"'"+ "," + "'"+str(ufid)+"')"
# cursor.execute("""INSERT INTO map VALUES (%s,%s)""",(str(roll_number),ufid))
# connection.commit()
# cursor.close()
# connection.close()


import MySQLdb

txt=open('file.txt')
ufid=txt.read()

print ufid
roll_number=raw_input("Enter the rollno: ")
connection=MySQLdb.connect(host="",user="",passwd="",db="")
cursor=connection.cursor()
sql2="SELECT COUNT(*) FROM map WHERE roll_number="+str(roll_number)
cursor.execute(sql2)
row=cursor.fetchone()
if str(row[0])=='0':
    cursor.execute("""INSERT INTO map VALUES (%s,%s)""",(str(roll_number),ufid))
    connection.commit()
    cursor.close()
else:
    print "Student already registered"
connection.close()
