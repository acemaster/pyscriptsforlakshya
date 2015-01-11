import serial
import MySQLdb
import time
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=0)
while 1:
    try:
        t=ser.readline()
        if t != '':
            t = t[:-1]
            print t
            roll_number=raw_input("Enter the rollno: ")
            connection=MySQLdb.connect(host="",user="",passwd="",db="")
            cursor=connection.cursor()
            sql2="SELECT COUNT(*) FROM map WHERE roll_number="+str(roll_number)
            cursor.execute(sql2)
            row=cursor.fetchone()
            if str(row[0])=='0':
                cursor.execute("""INSERT INTO map VALUES (%s,%s)""",(str(roll_number),t))
                connection.commit()
                cursor.close()
            else:
                print "Student already registered"
            connection.close()

            time.sleep(1)
    except ser.SerialTimeoutException:
        print('Data could not be read')
        print t
    time.sleep(1)
