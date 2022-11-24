
#Patrick Conroy
#CIS261
#Course Project Part 3: Using Files to Store and Retrieve Data

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
    for EmpList in EmpDetailList:
        fromdate = EmpList[0]
        todate = EmpList[1]
        empname = EmpList[2]
        hours = EmpList[3]
        hourlyrate = EmpList[4]
        taxrate = EmpList[5]


        #write code to assign values to todate, empname, hours, hourlyrate, and taxrate from EmpList
        
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
        #write code to assign Totalhours, TotalGrossPay, TotalTax, and TotalNetPay to corresponding dictionary item
    

#def Totals(TotalEmployees, TotalHours, TotalGrossPay, TotalTax, TotalNetPay):

#    print(f"Total Number of Employees: {TotalEmployees}")
#    print(f"Total Hours Worked: {TotalHours:,.2f}")
#    print(f"Total Gross Pay: {TotalGrossPay:,.2f}")
#    print(f"Total Income Tax: {TotalTax:,.2f}")
#    print(f"Total Net Pay: {TotalNetPay:,.2f}")

def PrintTotal(EmpTotals):
    print()
    #use dictionary to print totals
    print(f'Total Number of Employees: {EmpTotals["TotalEmployees"]}')
    print(f'Total Hours Worked: {EmpTotals["TotalHours"]:,.2f}')
    print(f'Total Gross Pay: {EmpTotals["TotalGrossPay"]:,.2f}')
    print(f'Total Income Tax: {EmpTotals["TotalTax"]:,.2f}')
    print(f'Total Net Pay: {EmpTotals["TotalNetPay"]:,.2f}')
    #write code to print TotalHours, TotalGrossPay, TotalTax, and TotalNetPay from dictionary
              


if __name__ == "__main__":
#    TotalEmployees = 0
#    TotalHours = 0.00
#    TotalGrossPay = 0.00
#    TotalTax = 0.00
#    TotalNetPay = 0.00

    EmpDetailList = []
    EmpTotals = {}
    while True:
        display_title()
        empname = get_emp_name()
        if (empname.upper() == "END"):
            break

        fromdate, todate = get_dates_worked()
        hours = get_hours_worked()
        hourlyrate = get_hourly_rate()
        tax = get_tax_rate()
        #grosspay, incometax, netpay = CalcTaxNetPay(hours, hourlyrate, tax)
        #get_emp_info(empname, hours, hourlyrate, grosspay, tax, incometax, netpay)

        #write code to insert fromdate, todate, empname, hours, hourlyrate, and taxrate into list EmpDetail
        EmpList = [fromdate, todate, empname, hours, hourlyrate, tax]

        EmpDetailList.append(EmpList)

        #TotalEmployees += 1
        #TotalHours += hours
        #TotalGrossPay += grosspay
        #TotalTax += incometax
        #TotalNetPay += netpay

    printinfo(EmpDetailList)
    PrintTotal(EmpTotals)
