
print("""ENTER THE NUMBER OF THE QUESTION WHICH YOU WANT TO RUN AS PER THE GIVEN BELOW OPTIONS:
      1.Write a Python print statement that shows a message saying, "Starting the trading session."
      2.Create a variable stock_price that stores the current price of a stock as a floating-point number.
      3.Assign the symbol AAPL to a variable named stock_symbol.
      4.Add a comment explaining that the following code will initialize a trading balance variable with 10000.
      5.Identify and fix the syntax error in the following code snippet: total_return = final_price - initial_price print(total_return)
      6.Write a program that asks the user for the quantity of a stock to buy and prints "Buying X shares," where X is the input quantity.
      7.Convert a string variable price_str holding the value "89.50" into a floating-point number.
      8.Define a list literal containing the stock symbols "AAPL", "TSLA", and "GOOGL".
      9.Write a print statement that outputs "Stock XYZ is trading at $PRICE", where XYZ is a variable symbol, and PRICE is a floating-point variable price.
      10.Write a Python Program print_trade_summary(symbol, quantity, price) that accepts a stock symbol, the number of shares, and the price per share. It should print out a formatted summary of the total trade cost.
      11. Calculate the Daily Return on Investment (ROI)

    Objective: Prompt the user to enter the purchase price and the selling price of a stock, and calculate the ROI.
    12. Determine the Average Price from User Inputs

    Objective: Ask the user to input three different prices of a stock throughout the day and compute the average.
    13. Compare Two Stock Prices

Objective: Ask the user for the prices of two stocks and print which one is higher.
14. Break-Even Price Calculator

Objective: Calculate the break-even price after buying a stock and spending money on fees.
15. Display Stock Price Change

Objective: Ask the user to enter yesterday's and today's stock prices, then print the change in price.
16. Calculate Required Margin

Objective: Calculate the required margin for a trade based on user inputs for trade size and margin rate.
17. Convert Currency from User Input

Objective: Ask the user for an amount in USD and a conversion rate, then convert it to another currency.
18. Calculate the Weighted Average Price

Objective: Calculate the weighted average price based on user inputs for different prices and their respective weights.
19. User Input to Adjust Stock Quantity

Objective: Prompt the user for the current number of stocks, how many to buy, and how many to sell, then calculate the new total.

""")

# def Q_1 

try:
    n=int(input("Enter your Choise: - "))
    match n:
        case 1:
            print("Starting the trading session.")
        case 2:
            try:
                a=float(input("Enter the current price of the stock: - "))
                print(f"Current price of the stock is {a}")
            except:
                print("Please enter the correct input")
        case 3:
            stock_symbol=input("Enter the stock symbol: - ")
            print(f"Stock Symbol is {stock_symbol}")
        case 4:
            # This code will initialize a trading balance variable with 10000.
            print("This code will initialize a trading balance variable with 10000.")
        case 5:
            try:
                total_return = 0
                initial_price = float(input("Enter the initial price: - "))
                final_price = float(input("Enter the final price: - "))
                total_return = final_price - initial_price
                print(total_return)
            except:
                print("Please enter the correct input")
        case 6:
            try:
                quantity = int(input("Enter the quantity of stock to buy: - "))
                print(f"Buying {quantity} shares")
            except:
                print("Please enter the correct input")
        case 7:
            print(float("89.50"))
        case 8:
            try:
                n=int(input("Enter the number of stock symbols you want to enter: - "))
                b=[]
                for i in range(n):
                    stock_symbols = input("Enter the stock symbol: - ")
                    b.append(stock_symbols)
                print(b)
            except:
                print("Please enter the correct input")
        case 9:
            try:
                stoks_name= input("Enter the stock name: - ")
                price = float(input("Enter the price of the stock: - "))
                print(f"Stock {stoks_name} is trading at ${price}")
            except:
                print("Please enter the correct input")
        case 10:
            try:
                def print_trade_summary(symbol, quantity, price):
                    print(f"Stock {symbol} is trading at ${price} and you have bought {quantity} shares")
                
                symbol = input("Enter the stock symbol: - ")
                quantity = int(input("Enter the quantity of stock to buy: - "))
                price = float(input("Enter the price of the stock: - "))
                print_trade_summary(symbol, quantity, price)
            except:
                print("Please enter the correct input")
        case 11:
            try:
                def daily_ROI(daily_profit, daily_investment):
                    print(f"The daily ROI is :- {float(daily_profit/daily_investment)}")
            except:
                print("Please enter the correct input")
        case 12:
            try:
                def avg_price(num,symbol):
                    sum=0
                    for i in range(num):
                        sum+=float(input(f"Enter the price of the stock {symbol} at {i+1} time: - "))
                    print(f"The average price of the stock {symbol} is {sum/num}")
            except:
                print("Please enter the correct input")
        case 13:
            try:
                c=[]
                def compare_price(n,m):
                    for i in range(n):
                        b=float(input(f"Enter the price of the stock {i+1}: - "))
                        c.append(b)
                    print(f"The summary of the stock {m} is :- \nThe highest price among the given prices is {max(c)}, while the lowest price is {min(c)} .\nThe average price of the stock is {sum(c)/n}.\n The final ordered Stock Price is {sorted(c)}")
                n=int(input("Enter the number of stock  prices you want to enter: - "))
                m=input("Enter the stock symbol: - ")
                compare_price(n,m)
            except:
                print("Please enter the correct input")
        case 14:
            try:
                def break_even_price(stock_price, fees,symbol):
                    print(f"The break-even price of the stock {symbol} is {stock_price+fees}")
                stock_price = float(input("Enter the stock price: - "))
                fees = float(input("Enter the fees: - "))
                symbol = input("Enter the stock symbol: - ")
                break_even_price(stock_price, fees,symbol)
                    
            except:
                print("Please enter the correct input")
        case 15:
            try:
                def stock_change_predictor(yesterday_price, today_price,symbol):
                    difference = today_price-yesterday_price
                    print(f"The change in the stock price of {symbol} is {today_price-yesterday_price} and the percentage change is {((today_price-yesterday_price)/yesterday_price)*100}%")
                yesterday_price = float(input("Enter the yesterday's stock price: - "))
                today_price = float(input("Enter the today's stock price: - "))
                symbol = input("Enter the stock symbol: - ")
                stock_change_predictor(yesterday_price, today_price,symbol)
            except:
                print("Please enter the correct input")
        case 16:
            try:
                def cal_margin(trade_size, margin_rate):
                    print(f"The required margin for the trade is {trade_size*margin_rate}")
                trade_size = float(input("Enter the trade size: - "))
                margin_rate = float(input("Enter the margin rate: - "))
                cal_margin(trade_size, margin_rate)
            except:
                print("Please enter the correct input")
        case 17:
            try :
                def currency_converter(amount, conversion_rate):
                        print(f"The converted amount is {amount*conversion_rate}")
                amount = float(input("Enter the amount in USD: - "))
                conversion_rate = float(input("Enter the conversion rate: - "))
                currency_converter(amount, conversion_rate)
            except:
                print("Please enter the correct input")
            
        case 18:
            try:
                def avg_st_stk(num,name):
                    b,d=[],[]
                    for i in range(num):
                        a=float(input(f"Enter the price {i+1} of the stock {name} : - "))
                        b.append(a) 
                        c=float(input(f"Enter the weight {i+1} of the stock {name} : - "))
                        d.append(c)
                    print(f"The weighted average price of the stock {name} is {(sum([b[i]*d[i]  for i in range(num)]))/sum(d)} \n The Stock Prices are {b} \n The Stock Weights are {d}")
                name = input("Enter the stock symbol: - ")
                num = int(input(f"Enter the number of stock prices you want to enter of {name}: - "))
                
                avg_st_stk(num,name)
            except:
                print("Please enter the correct input")
        case 19:
            try:
                def stock_quantity(current_quantity, buy_quantity, sell_quantity):
                    print(f"The new total of the stock is {current_quantity+buy_quantity-sell_quantity}")
                current_quantity = int(input("Enter the current number of stocks: - "))
                buy_quantity = int(input("Enter the number of stocks you want to buy: - "))
                sell_quantity = int(input("Enter the number of stocks you want to sell: - "))
                stock_quantity(current_quantity, buy_quantity, sell_quantity)
            
            except:
                print("Please enter the correct input")     
        case _:
            print("Please enter the correct input")           
except Exception as e:
    print(f" Please enter the correct Input\n The input you gave  {(e)}  is not as per the demanded question")
