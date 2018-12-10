import pymysql

db = pymysql.connect("localhost","root","secret","notifier" )


cursor = db.cursor()


cursor.execute("SELECT VERSION()")

data = cursor.fetchone()
print("Database version : %s " % data)

db.close()