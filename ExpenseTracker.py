# Expense Tracker Project

expensesList=[] #List Of Ecpenses in form of Dictionary 
print(" Welcome to Expense Traker : Sabash|")

while True:
    print("====MENU====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Expense")
    print("4. Exit")

    choice=int(input("Plese Enter Your Choise: "))

#1. Add Expense
    if(choice==1):
        date=input("Enter Date when you incurred the expence? : ")
        category=input("Enter the Category (Food, Treval, Books, Makeup): ")
        description=input("Give More Details: ")
        amount=float(input("Enter the Amount: "))

        expense= {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expensesList.append(expense)
        print("\n DONE. Expenses is added successfully ")

#2. View All Expenses

    elif(choice == 2):
        if(len(expense)==0):
            print("No Expenses Added")
        else:
            print("This is your entire expense.")
            count=1
            for eachexpense in expensesList:
                print(f"Expense Number {count} -> {eachexpense["date"]}, {eachexpense["category"]}, {eachexpense["description"]}, {eachexpense["amount"]}")
                count=+1

#3. View Total Spending.

    elif(choice == 3):
        total=0
        for eachExp in expensesList:
            total=total+eachExp["amount"]

        print("Total Expense : ",total)

#4. Exit.

    elif(choice==4):
        print("ThankYou for using our System. ")
        break

    else:
        print("Invalid Choice. Try Again.")


