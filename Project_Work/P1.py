print("""Python Mini Project 1 :
Scenario: Stock Data Entry and Analysis Tool

Objective: Create a Python script that will involve taking manual input for stock prices over a week
           and will calculate the average price. It should also demonstrate variable declaration, user input,
           and basic arithmetic using Python types.""")
try :
    def stock_analysis_tool(days):
        a=[]
        for i in range(days):
            a.append(int(input(f"Enter the stock price for day {i+1} : ")))
        print(f"Stock Prices for the week : {a}\nThe average stock price for the week is : {sum(a)/days}")
    days=int(input("Enter the number of days for which you want to enter the stock prices : "))

    stock_analysis_tool(days)

                     

except:
    print("Please Give a correct Input")