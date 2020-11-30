import sqlite3
cancel_connect=sqlite3.connect('airline.db')
cancel_cursor=cancel_connect.cursor()
class cancels:
    def __init__(self):
        print("Cancel Ticket's Page")
        print(150*"*")
    def retrieve(self,n):
        retrieve_query="SELECT * FROM Booked_Ticket where Name=='{}'".format(n)
        cancel_cursor.execute(retrieve_query)
        result=cancel_cursor.fetchall()
        if(result==[]):
            return False
        else:
           for one in result:
              for ones in one:
                 print(ones,end='  ')
              print('\n',150*"*")
           return True
    def cancel(self,opt):
        cancel_query="DELETE FROM Booked_Ticket where Sno=='{}'".format(opt)
        cancel_cursor.execute(cancel_query)
        cancel_connect.commit()
        print("Successfully Deleted")




def Cancels(n):
    ca=cancels()
    if(ca.retrieve(n)):
           choice=int(input("Enter a choice :"))
           ca.cancel(choice)
