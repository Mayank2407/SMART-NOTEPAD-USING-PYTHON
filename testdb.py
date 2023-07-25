import cx_Oracle
import traceback # ye apn ko exception ki poori details dega
connect=None
try:
   conn=cx_Oracle.connect("c##mojo/123@127.0.0.1/orcl")
   print("Connected successfully to the db")
   print("db version:",conn.version)
   print("username:",conn.username)
except cx_Oracle.DatabaseError:
   print("sorry connection failed")
   print(traceback.format_exc())
finally:
   if conn is not None:
      conn.close()
      print("disconnected successfully with the db")


