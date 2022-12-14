
#Patrick Conroy
#CIS261
#Course Project Part 3: Using Files to Store and Retrieve Data

from datetime import datetime

def display_title():
    print("Welcome to Payroll Database")


def get_emp_name():
    empname = input("Enter Employee name (type END to terminate program): ")
    return empname

def get_hours_worked():
    hours = float(input("Enter number of hours worked: "))
    return float(hours)

def get_hourly_rate():
    hourlyrate = float(input("Enter employee's hourly rate: "))
    return float(hourlyrate)

def get_tax_rate():
    tax = float(input("Enter tax rate: ")) #enter as decimal
    return float(tax)


def CalcTaxNetPay(hours, hourlyrate, tax):
    grosspay = float(hours) * float(hourlyrate)
    incometax = grosspay * tax
    netpay = grosspay - incometax
    return float(grosspay), float(incometax), float(netpay)

def get_dates_worked():
    fromdate = input("Enter Start Date (mm/dd/yyyy): ")
    todate = input("Enter End Date (mm/dd/yyyy): ")
    return fromdate, todate

    

#def get_emp_info(empname, hours, hourlyrate, grosspay, tax, incometax, netpay):
#    print(empname, f"{hours:,.2f}", f"{hourlyrate:,.2f}", f"{grosspay:,.2f}", f"{tax:,.1%}", f"{incometax:,.2f}", f"{netpay:,.2f}")

def printinfo(EmpDetailList):
    TotalEmployees = 0
    TotalHours = 0.00
    TotalGrossPay = 0.00
    TotalTax = 0.00
    TotalNetPay = 0.00
    EmpFile = open("Employees.txt", "r")
    while True:
        rundate = input("Enter start date for report (MM/DD/YYYY) or All for all data in file: ")
        if (rundate.upper() == "ALL"):
            break
        try:
            rundate = datetime.strptime(rundate, "%m/%d/%Y")
            break
        except ValueError:
            print("Invalid date format. Please try again.")
            print()
            continue
    while True:
        EmpDetail = EmpFile.readline()
        if not EmpDetail:
            break
        EmpDetail = EmpDetail.replace("\n", "")
        EmpList = EmpDetail.split("|")
        fromdate = EmpList[0]
        if (str(rundate).upper() != "ALL"):
            checkdate = datetime.strptime(fromdate, "%m/%d/%Y")
            if (checkdate < rundate):
                continue
        todate = EmpList[1]
        empname = EmpList[2]
        hours = float(EmpList[3])
        hourlyrate = float(EmpList[4])
        tax = float(EmpList[5])       
        grosspay, incometax, netpay = CalcTaxNetPay(hours, hourlyrate, tax)
        print(fromdate, todate, empname, f"{hours:,.2f}", f"{hourlyrate:,.2f}", f"{grosspay:,.2f}", f"{tax:,.1%}", f"{incometax:,.2f}", f"{netpay:,.2f}")
        TotalEmployees += 1
        TotalHours += float(hours)
        TotalGrossPay += grosspay
        TotalTax += incometax
        TotalNetPay += netpay
        EmpTotals["TotalEmployees"] = TotalEmployees
        EmpTotals["TotalHours"] = TotalHours
        EmpTotals["TotalGrossPay"] = TotalGrossPay
        EmpTotals["TotalTax"] = TotalTax
        EmpTotals["TotalNetPay"] = TotalNetPay
        EmpDetailList = True
    if (EmpDetailList):
        PrintTotal(EmpTotals)
    else:
        print("No details to print.")

#def Totals(TotalEmployees, TotalHours, TotalGrossPay, TotalTax, TotalNetPay):

#    print(f"Total Number of Employees: {TotalEmployees}")
#    print(f"Total Hours Worked: {TotalHours:,.2f}")
#    print(f"Total Gross Pay: {TotalGrossPay:,.2f}")
#    print(f"Total Income Tax: {TotalTax:,.2f}")
#    print(f"Total Net Pay: {TotalNetPay:,.2f}")

def PrintTotal(EmpTotals):
    print()
    print(f'Total Number of Employees: {EmpTotals["TotalEmployees"]}')
    print(f'Total Hours Worked: {EmpTotals["TotalHours"]:,.2f}')
    print(f'Total Gross Pay: {EmpTotals["TotalGrossPay"]:,.2f}')
    print(f'Total Income Tax: {EmpTotals["TotalTax"]:,.2f}')
    print(f'Total Net Pay: {EmpTotals["TotalNetPay"]:,.2f}')


if __name__ == "__main__":
    
    print()
    display_title()
     
    DetailsPrinted = False  
    EmpTotals = {} 
    
    #print(UserName," is invalid.")
    EmpFile = open("Employees.txt", "a+")
    while True:
            empname = get_emp_name()
            if (empname.upper()== "END"):
                break
            fromdate, todate = get_dates_worked()
            hours = get_hours_worked()
            hourlyrate = get_hourly_rate()
            tax = get_tax_rate()
            EmpDetail = fromdate + "|" + todate  + "|" + empname  + "|" + str(hours)  + "|" + str(hourlyrate)  + "|" + str(tax) + "\n"
            EmpFile.write(EmpDetail)
    EmpFile.close()
    printinfo(DetailsPrinted)
        
   