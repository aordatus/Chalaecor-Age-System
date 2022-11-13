# --------- ESSENTIALS ---------
import time

class Day:
    def __init__(self, m, w, y, im, iy):
        self.whichMonth = m
        self.whichWeekday = w
        self.whichYear = y
        self.whichDayInMonth = im
        self.whichDayInYear = iy
    def display(self):
        print(f"Day {self.whichDayInYear} in Year {self.whichYear} | Day {self.whichDayInMonth} in {self.whichMonth} | {self.whichWeekday}")

# --------- CHALAECOR WORLD CALENDER SYSTEM ---------

months = ["Norvexus","Exerlym","Orylwen","Terxangth"] #There are 4 months in 1 year
weekdays = ["Elparday", "Aetherday", "Nuvirday", "Refelsenday"] #One week is 4 days long #Year 000 started from Elparday Year 001 started from Aetherday and so on...
numberOfDaysInOneYear = 180 #Every year is 180 days long
numberOfDaysInFourMonths = [80, 40, 20, 40] #Respective to months
calenderYears = {}

# --------- WAKE ---------

def Wake():
    for i in range(501):
        calenderYears[i] = Generate(i)

def Generate(year):
    allDays = []
    x = year%4 #weekDay tool
    y1 = 0 #month tool
    y2 = 1 #day tool
    
    for i in range(1,numberOfDaysInOneYear+1):
        day = Day(months[y1], weekdays[x], year, y2, i)
        allDays.append(day)
        if(x>=3):
            x=0
        else:
            x+=1

        if(y2 == numberOfDaysInFourMonths[y1]):
            y1 += 1
            y2 = 1
        else:
            y2 += 1
    return allDays
            
def DisplayGen(gen):
    for i in gen: #All Days
        i.display()

def FindDayFromNumberedDayInMonth(m, d, y):
    c = calenderYears[y]
    for i in c:
        if(i.whichMonth == m and i.whichDayInMonth == d):
            return i
def FindDayFromNumberedDayInYear(d, y):
    c = calenderYears[y]
    for i in c:
        if(i.whichDayInYear == d):
            return i
        
# --------- MENU ---------

def Menu():
    print("Task 1 => Give Numbered Day of Month & Get Day")
    print("Task 2 => Give 0th & 3rd Pull Get 1st Pull")
    print("Task 3 => Give 1st & 3rd Pull Get 0th Pull")
    print("Task 4 => Give 0th Pull & Current Day Get Accurate Age")
    print("Task 9 => Exit")

    inp = input("\nChoose Task")

    if(inp.isdigit()==False):
        print("\nFailed... Tip: If you want to choose 1st just enter 1... for 2nd enter 2... and so on...\n")
        Menu()

    if(int(inp) not in range(1,10)):
        print("\nFailed... Tip: If you want to Task 1 just enter 1... for Task 2 just enter 2... and so on...\n")
        Menu()

    if(int(inp)==1):
        print("\n")
        One()

    elif(int(inp)==2):
        print("\n")
        Two()

    elif(int(inp)==3):
        print("\n")
        Three()
    
    elif(int(inp)==4):
        print("\n")
        Four()
        
    elif(int(inp)==9):
        exit()
    
def One(): #Give Numbered Day of Month & Get Day
    foundIt = AskDay()
    foundIt.display()
    print("\n")
    Menu()

def Two(): #Give 0th & 3rd Pull Get 1st Pull
    print("0th Pull Day \n")
    ZeroPull = AskDay()
    print("3rd Pull Day \n")
    ThirdPull = AskDay()
    x = DaysInBetween(ZeroPull, ThirdPull, -1)
    y = round(x/4)
    FirstPull = TravelDays(y, ThirdPull, -1)
    print("1st Pull Day \n")
    FirstPull.display()
    print("\n")
    Menu()

def Three(): #Give 1st & 3rd Pull Get 0th Pull
    print("1st Pull Day \n")
    FirstPull = AskDay()
    print("3rd Pull Day \n")
    ThirdPull = AskDay()
    x = DaysInBetween(FirstPull, ThirdPull, -1)
    y = round(x*4)
    ZerothPull = TravelDays(y, ThirdPull, -1)
    print("0th Pull Day \n")
    ZerothPull.display()
    print("\n")
    Menu()

def Four(): #Give 0th Pull & Date Get Accurate Age
    print("0th Pull Day \n")
    ZerothPull = AskDay()
    print("Current Day \n")
    CurrentDay = AskDay()
    x = DaysInBetween(ZerothPull, CurrentDay, -1)
    print(f"{x} Days or {round(x/180,2)} Years")
    print("\n")
    Menu()

# --------- METHODS ---------
def DaysInBetween(fromDay, toDay, direction): #-1 direction means backward #+1 direction means forward
    x = fromDay.whichDayInYear + 180*fromDay.whichYear
    y = toDay.whichDayInYear + 180*toDay.whichYear
    return (x-y)*direction

def TravelDays(numberOfDays, fromDay, direction): #-1 direction means backward #+1 direction means forward
    x = fromDay.whichDayInYear + 180*fromDay.whichYear
    y = x+(numberOfDays)*direction
    q, r = divmod(y, 180)
    return FindDayFromNumberedDayInYear(r, q)

def AskDay():
    m = GetMonth()
    d = GetNumberedDay(m)
    y = GetYear()
    return FindDayFromNumberedDayInMonth(m, d, y)

def GetMonth():
    print("1. Norvexus\n2. Exerlym\n3. Orylwen\n4. Terxangth")
    inp = input("Choose Month")
    if(inp.isdigit()==False):
        print("\nFailed... Tip: If you want to choose Norvexus just enter 1... for Exerlym enter 2... and so on...\n")
        GetMonth()
    if(int(inp) not in [1,2,3,4]):
       print("\nFailed... Tip: If you want to choose Norvexus just enter 1... for Exerlym enter 2... and so on...\n")
       GetMonth()
    print("\n")
    return months[int(inp)-1]

def GetNumberedDay(m):
    inp = input("Enter Numbered Day In Month")
    if(inp.isdigit()==False):
        print("\nFailed... Tip: If you want to choose 1st just enter 1... for 2nd just enter 2... and so on...\n")
        GetNumberedDay(m)
    if(int(inp)>numberOfDaysInFourMonths[months.index(m)]):
        print(f"\nFailed... Month {m} range is 1 to {numberOfDaysInFourMonths[months.index(m)]}\n")
        GetNumberedDay(m)
    print("\n")
    return int(inp)
        
def GetYear():
    inp = input("Enter Year")
    if(inp.isdigit()==False):
        print("\nFailed... Tip: If you want to choose year 480 just enter 480... for year 004 just enter 4... and so on...\n")
    if(int(inp)>500):
        print(f"\nFailed... Don't go too far\n")
    print("\n")
    return int(inp)

# --------- RUN ---------

print("\n"*100) #Filler
Wake()
Menu()


