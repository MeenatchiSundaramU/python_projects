import sqlite3
cancel_connect=sqlite3.connect('airline.db')
cancel_cursor=cancel_connect.cursor()
class Status:
    def __init__(self):
        print("Check the status of the flight")
        print('\n',150*"*")
    def retrieve(self):
        ret_query="SELECT * FROM Vehicle_Info"
        cancel_cursor.execute(ret_query)
        result=cancel_cursor.fetchall()
        for one in result:
              for ones in one:
                 print(ones,end='  ')
              print('\n',150*"*")

def ft_status():
    st=Status()
    st.retrieve()

