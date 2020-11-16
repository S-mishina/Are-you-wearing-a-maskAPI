from urllib.parse import urlparse
import mysql.connector as mydb
import time
import datetime
def sqlok():
 day = datetime.date.today()
 time1 = datetime.datetime.now()
 conn = mydb.connect(
        host='127.0.0.1',
        port='3306',
        user='testadmin',
        password='admin',
        database='mask'
    )
 # コネクションが切れた時に再接続してくれるよう設定
 conn.ping(reconnect=True)
 # 接続できているかどうか確認
 print(conn.is_connected())
 cur = conn.cursor()
 time2=str(time1.hour)+":"+str(time1.minute)+":"+str(time1.second)
 print(day)
 print(time2)
 cur.execute("INSERT INTO `mask-ok-or-ng1` (`day`, `time`, `ok-or-ng`)"+ "VALUES"+ "("+"'"+str(day)+"'"+","+"'"+str(time1)+"'"+","+"'OK')")
 conn.commit()
 cur.close()
 conn.close()

def sqlng():
 day = datetime.date.today()
 time1 = datetime.datetime.now()
 conn = mydb.connect(
        host='127.0.0.1',
        port='3306',
        user='testadmin',
        password='admin',
        database='mask'
    )
 # コネクションが切れた時に再接続してくれるよう設定
 conn.ping(reconnect=True)
 # 接続できているかどうか確認
 print(conn.is_connected())
 cur = conn.cursor()
 time2=str(time1.hour)+":"+str(time1.minute)+":"+str(time1.second)
 print(day)
 print(time2)
 cur.execute("INSERT INTO `mask-ok-or-ng1` (`day`, `time`, `ok-or-ng`)"+ "VALUES"+ "("+"'"+str(day)+"'"+","+"'"+str(time1)+"'"+","+"'NG')")
 conn.commit()
 cur.close()
 conn.close()
sqlok()
sqlng()