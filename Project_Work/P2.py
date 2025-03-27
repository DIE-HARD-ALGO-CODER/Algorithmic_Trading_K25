# print("""Python Mini Project 2 :
# Scenario: Simulated Stock Trading Bot

# Objective: Create a Python script that simulates trading over a dataset containing historical stock prices. The bot will decide whether to buy, hold, or sell based on the momentum calculated as the difference between the current price and the average price of the last few days.

# Project Components:
# Data Structure:

# Use a list of tuples or dictionaries to simulate historical stock data with each element containing information about the stock price on a particular day.
# Momentum Calculation:

# Calculate the average price of the last N days and compare it with the current day's price to determine the momentum.
# Trading Decisions:

# Use if-else statements to make trading decisions based on the calculated momentum.
# Trading Simulation:

# Loop through the dataset and simulate trading decisions, updating the portfolio accordingly.
# Performance Evaluation:

# At the end of the simulation, calculate and print the final portfolio value and compare it with the initial value to gauge performance.
# Skills and Python Features Used:
# Python Operators: Use arithmetic operators to calculate averages, gains, and losses.
# Python if-else: Make conditional decisions based on momentum and other trading indicators.
# Python Modules: Use the datetime module for handling dates, matplotlib for plotting stock prices and portfolio value over time.
# Python While Loop: Could be used to allow the simulation to run until a certain condition is met, like a stop-loss limit.
# Python for loop: Iterate over each day in the stock dataset to simulate trading.""")



try:
    def simulation(symbol,N,current_price,days):
        stk=[]
        for i in range(N):
            stk.append(float(input(f"Enter the stock price of {symbol} on day {i+1}: ")))
        print(F"The entered stock prices of {symbol} are: {stk}")
        for i in range(N):
            if i<=(N-days):
                avg=sum(stk[i:i+days])/days
                if ( avg - current_price )>0:
                    print(f"The average price of the stock {symbol} is greater than the current price of the stock {symbol}. \nSo, the momentum is positive.\nThe shares of the stock {symbol} will be bought on day {i+1}.\n")    
                elif ( avg - current_price )<0:
                    print(f"The average price of the stock {symbol} is less than the current price of the stock {symbol}. \nSo, the momentum is negative.\nThe shares of the stock {symbol} will be sold on day {i+1}\n")
                else:
                    print(f"The average price of the stock {symbol} is equal to the current price of the stock {symbol}. \nSo, the momentum is neutral.\nThe shares of the stock {symbol} will remain on hold on day {i+1}\n")

                 
        pass
    def simulation_avg(symbol,N,current_price,days):
        stk=[]
        for i in range(N):
            stk.append(float(input(f"Enter the stock price of {symbol} on day {i+1}: ")))
        print(F"The entered stock prices of {symbol} are: {stk}")
        if ( stk.average() - current_price )>0:
            print(f"The average price of the stock {symbol} is greater than the current price of the stock {symbol}. \nSo, the momentum is positive.\nThe shares of the stock {symbol} will be bought.\n")    
        elif ( stk.average() - current_price )<0:
            print(f"The average price of the stock {symbol} is less than the current price of the stock {symbol}. \nSo, the momentum is negative.\nThe shares of the stock {symbol} will be sold.\n")
        else:
            print(f"The average price of the stock {symbol} is equal to the current price of the stock {symbol}. \nSo, the momentum is neutral.\nThe shares of the stock {symbol} will be hold.\n")

        

    def if_else_comparision(N,days,current_price):
        if days > N:
            print(f"The number of days you want to take as a base for calculating the average price is more than the number of days you have entered. Please enter the correct values.")
        else:
            if days == N:
                print(f"The number of days you want to take as a base for calculating the average price is equal to the number of days you have entered.\n So we are doing an average moving comparision.\nHere Every stock value will be compared with the average of all the stock values.\n")
                simulation_avg(symbol,N,current_price,days)
            else:
                if days <2:
                    print(f"The number of days you want to take as a base for calculating the average price is less than 2, which is not possible. \nPlease enter the correct values.")
                else:
                    simulation(symbol,N,current_price,days)    



    def if_else_comparision_NoOfStokes(N,days):
        if a<1:
                print("The number of stocks you have entered is less than 1. Please enter the correct value.")
        elif a==1:
                symbol=input("Enter the symbol of the stock: ")
                current_price=float(input(f"Enter the current price of the stock {symbol}: ")) 
                if_else_comparision(N,days,current_price)
        else:
              print("under working")

    
    symbol,compare_price,N,days,a="","",0,0,0
    
    N=int(input("Enter the value of N(as the total number of days): "))
    days=int(input("Enter the number of days you want to take as a base for calculating the average price: "))
    
    a=int(input("Enter the number of differnet stock you have in your portfolio and which you want to compare:-  "))
    if_else_comparision_NoOfStokes(N,days)

    
      
except Exception as e:
    print(f"Their is an error in the input given by you. \n The error is {e}")
