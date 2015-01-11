import serial
import MySQLdb
import time
import datetime
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=0)
while 1:
    try:
        t=ser.readline()
        if t != '':
            t = t[:-1]
            print t
            connection=MySQLdb.connect(host="",user="",passwd="",db="")
            cursor=connection.cursor()
            sql1="SELECT roll_number FROM map WHERE ufid="+str(t)
            cursor.execute(sql1)
            row=cursor.fetchone()
            print row[0]
            roll_number=row[0]
            sql2="SELECT COUNT(*) FROM mess WHERE roll_number="+str(row[0])
            cursor.execute(sql2)
            row=cursor.fetchone()
            print row[0]

            if str(row[0])=='0':
                print "Executed: "
                cursor.execute("SELECT HOUR(SYSDATE()),SYSDATE() FROM dual")
                row=cursor.fetchone()
                hour=row[0]
                date=row[1]
                streak=0
                print hour
                bf=0
                lch=0
                dn=0
                guest=0
                if hour>4 and hour<12:
                    bf=1
                elif hour<16:
                    lch=1
                else:
                    dn=1
                print "Executed"
               # sql5="insert into mess values('"+str(roll_number)+"', "+bf+", "+lch+", "+dn+", "+1+", "+date+", "+streak+", "+hour+", "+guest+");"
                #print sql5
                cursor.execute("""INSERT INTO mess VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)""",(str(roll_number),bf,lch,dn,1,date,streak,hour,guest))
                connection.commit()

            else:
                sql4="SELECT attendance FROM mess WHERE roll_number="+str(roll_number)
                print "Else"
                cursor.execute(sql4)
                row=cursor.fetchone()
                attendance=row[0]
                cursor.execute("SELECT HOUR(SYSDATE()),SYSDATE() FROM dual")
                row=cursor.fetchone()
                hour=row[0]
                date=row[1]
                cursor.execute("SELECT bf,lh,dnr,DATEDIFF(SYSDATE(),date),streak,hours,guest FROM mess WHERE roll_number="+str(roll_number))
                row=cursor.fetchone()
                counter=row[3]
                streak=row[4]
                hour2=row[5]
                guest=row[6]
                if counter==1:
                    streak=streak+1
                else:
                    streak=0
                print hour
                bf=row[0]
                lch=row[1]
                dn=row[2]
                if hour>6 and hour<12:
                    bf=bf+1
                elif hour<16:
                    lch=lch+1
                else:
                    dn=dn+1
                
                if hour-hour2<2:
                    guest=guest+1
                else:
                    attendance=attendance+1


                print type(attendance)
                print attendance
                #sql3="UPDATE mess SET attendance=%s,bf=%s,lch=%s,dn=%s,date=%s,streak=%s WHERE roll_number=%s",(attendance,bf,,)
                cursor.execute("""UPDATE mess SET attendance=%s,bf=%s,lh=%s,dnr=%s,date=%s,streak=%s,hours=%s,guest=%s WHERE roll_number=%s""",(attendance,bf,lch,dn,date,streak,hour2,guest,str(roll_number),))
                connection.commit()
            cursor.close()
            connection.close()

            time.sleep(1)
    except ser.SerialTimeoutException:
        print('Data could not be read')
        print t
    time.sleep(1)
