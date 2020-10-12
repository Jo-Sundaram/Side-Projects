import gspread,datetime
from oauth2client.service_account import ServiceAccountCredentials
from datetime import date
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('sheets_tester.json', scope)
client = gspread.authorize(creds)
sheet = client.open('Money').sheet1



money = sheet.get_all_records()
payday = sheet.col_values(1)
income = sheet.col_values(2)
months = sheet.col_values(3)
expenses = sheet.col_values(4)
RESP = sheet.col_values(6)

# The following two loops convert the income and expense values
for num in range(len(expenses)):
    expenses[num] = expenses[num].replace("$","")

for num in range(len(income)):
    income[num] = income[num].replace("$","")



def get_months():
    '''Prints all months in column 3'''
    months = sheet.col_values(3)
    # count = 0
    # for month in months:
    #     print(count,end = ". ")
    #     print(month)
    

    for i in range(2):
        print(months[i])
    
    for i in range(2,len(months)):
        print(i-2, end = ". ")
        print(months[i])



def update_expenses(date,amount):
    '''Updates the expenses column with the given date and expense amount'''

    if date == "Today": # If the given date is today, converts into same format as sheets
        today = datetime.datetime.today()
        date = today.strftime("%b %Y")
          
    elif date.isdigit():    

        # if date in months: # updates already existing month expenses
        #     index = months.index(date)

        #     newExpense = float(expenses[index])+amount
        #     sheet.update_cell(index+1,4,newExpense)
        #     return

        if int(date) < len(months):
            newExpense = float(expenses[int(date)+2])+amount
            sheet.update_cell(int(date)+3,4,newExpense)
            return



    # If new date is entered, adds new date and amount into sheets columns
    months.append(date)
    expenses.append(amount)
    sheet.update_cell(len(months),3,months[-1])
    sheet.update_cell(len(expenses),4,amount)


def update_income(date,amount):
    '''Updates the expenses column with the given date and expense amount'''

    if date == "Today": # If given date is today, converts into same format as sheets
        today = datetime.datetime.today()
        date = today.strftime("%b %d %Y")

    elif date.isdigit(): # updates already existing date with new income
        
        if int(date) < len(payday):  
            index = payday.index(date)
            newIncome = float(income[index])+amount

            sheet.update_cell(index+1,2,newIncome)

            return
            # newIncome = float(income[int(date)+2])+amount
            # sheet.update_cell(int(date)+3,2,newIncome)
            # return


    # if new date is entered, adds date and amount to sheets column
    income.append(amount)
    payday.append(date)
    sheet.update_cell(len(payday),1,f"=TEXT(\"{date}\",\"mmm d yyyy\")")
    sheet.update_cell(len(income),2,amount)


def main():

    # Ask if user wants to add an expense or income
    user = int(input("Select option: \n 1. Expense \n 2. Income \n "))

    # Valid input checking
    while(user <1 or user >2):
        user = int(input("Select option: \n 1. Expense \n 2. Income \n "))


    if user == 1: # If user chooses Expense
        get_months()  # Displays existing months
        date = input("Select month or enter 'Today': ")
        amount = float(input("Enter expense amount: $ "))
        update_expenses(date,amount)


    elif user == 2: # If user chooses Income
        date = input("Enter date (Jan 01 2020) or enter 'Today': ")
        user = float(input("Enter amount: $ "))
        update_income(date,user)

    


main()
