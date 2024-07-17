def SingleTon(arg):
    d = {}
    def Inner():
        if(arg not in d):
            d[arg] = arg()
        return d[arg]
    return Inner
@SingleTon
class Jailer():
    def __init__(self):
        self.MT = 100
    def Booking(self,n):
        if (self.MT>=n):
            print("Tickets Booked Successfully")
            self.MT-=n
            print(f"Available Tickets:{self.MT}")
        else:
            print(f"{n} no.of Tickets not available.")
@SingleTon
class Kalki():
    def __init__(self):
        self.MT = 150
    def Booking(self,n):
        if (self.MT>=n):
            print("Tickets Booked Successfully.")
            self.MT-=n
            print(f"Available Tickets:{self.MT}")
        else:
            print(f"{n} no.of Tickets not available.")
def bms():
    print("1.Jailer /n 2.Kalki")
    choice = int(input("Select Your Movie: "))
    if (choice==1):
        n = int(input("Enter the no.of tickets: "))
        ob = Jailer()
        ob.Booking(n)
    elif (choice==2):
        n = int(input("Enter the no.of tickets: "))
        ob = Kalki()
        ob.Booking(n)

bms()