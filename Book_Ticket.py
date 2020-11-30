import sqlite3
bkt_connect=sqlite3.connect('airline.db')
bkt_cursor=bkt_connect.cursor()
names=['Airplane Name','froms','tos','Total Seats','Total Price']
merge_dict={}
class Book_Ticket:
    def __init__(self):
        print(100*"*")
        print("Welcome to Ticket Booking Page")
        print(100*"*")
        self.froms=input("Enter the Depature Place: ")
        print(100*"*")
        self.tos=input("Enter the Arrival Place: ")
        print(100*"*")
        self.date=input("Enter the Date of Depature: ")
        print(100*"*")
        self.choice=int(input("Choose the economies 1.economy 2.premium economy 3.business 4.first class :"))
        print(100*"*")
        if(self.choice==1):
            self.choice_total="economy_total"
            self.choice_price="eco_price"
        elif(self.choice==2):
            self.choice_total="premium_total"
            self.choice_price="premium_price"
        elif(self.choice==3):
            self.choice_total="business_total"
            self.choice_price="busi_price"
        else:
            self.choice_total="first_total"
            self.choice_price="first_price"

            
    def retrievalData(self,na,em,ph):
        bkt_search="SELECT air_name,froms,tos,{},{} from Vehicle_Info where tos=='{}' and froms=='{}';".format(self.choice_total,self.choice_price,self.tos,self.froms)
        bkt_cursor.execute(bkt_search)
        result=bkt_cursor.fetchone()
        merge_dict=dict(zip(names,result))
        for i in names:
            print("{}  :  {}".format(i,merge_dict[i]))
            print(100*"*")
        self.tpass=int(input("Enter the Total Passengers :"))
        print(100*"*")
        get_bkt=input("Are you Sure you want to book the Ticket (yes/no):")
        if(get_bkt=='yes'):
             self.update_data(self.tpass,merge_dict['Airplane Name'])
             self.cost=merge_dict['Total Price']*self.tpass
             print("Total Price :Rs.",self.cost)
             print(100*"*")
             self.save_ticket(merge_dict,self.tpass,self.cost,na,em,ph)
        else:
            return
    
    def update_data(self,get_pass,plane_name):
        update_query="UPDATE Vehicle_Info SET {}={}-{} where tos=='{}' and froms=='{}' and air_name=='{}';".format(self.choice_total,self.choice_total,get_pass,self.tos,self.froms,plane_name)
        bkt_cursor.execute(update_query)
        bkt_connect.commit()
        
    def save_ticket(self,m,total_seats,price,name,email,phone):
        bkt_cursor.execute('''INSERT INTO Booked_Ticket(Name,Email,Phone_no,Air_Name,froms,tos,Date,Total_pass,class,cost)values(?,?,?,?,?,?,?,?,?,?);''',(name,email,phone,m['Airplane Name'],m['froms'],m['tos'],self.date,total_seats,self.choice_total,price))
        bkt_connect.commit()
        
    
def tktBook(n,e,p):
    ibkt=Book_Ticket()
    ibkt.retrievalData(n,e,p)

