import Book_Ticket
import Cancel_Ticket
import Flight_status
class Home:
    def __init__(self):
        print("WELCOME TO HOME PAGE")
    def book_ticket(self,na,em,ph):
        print("Book Ticket")
        Book_Ticket.tktBook(na,em,ph)
        return
    def cancel_ticket(self,n):
        print("Cancel Ticket")
        Cancel_Ticket.Cancels(n)
        return
    def flight_status(self):
        print("Flight Status")
        Flight_status.ft_status()
        return

def home(n,e,p):
       h=Home()
       while(1):
           choice=int(input("1.BOOK TICKET\n2.CANCEL TICKET\n3.FLIGHT STATUS\n4.Exit: "))
           if(choice==1):
               h.book_ticket(n,e,p)
           elif(choice==2):
               h.cancel_ticket(n)
           elif(choice==3):
               h.flight_status()
           else:
               break
