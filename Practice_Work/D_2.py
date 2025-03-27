print("""Enter the Question No you want to run
      1. Operators and Logical Expressions
Question: You have a list of stock prices over 30 days. Write a logical expression that will identify consecutive price drops over three days or more.
       For instance, [120, 118, 115, 110] would qualify, but [120, 118, 120, 110] would not.
      2. If-Else Statements
Question: You are designing an algorithm to trade stocks. If the current price of a stock is above the 30-day moving average, print "Buy Signal"; otherwise, print "Sell Signal". 
      Assume you have a list of daily prices and that the moving average can be calculated.
      3. Modules (pandas)
Question: Use the pandas library to load a CSV file containing historical trading data and 
      calculate the daily percentage change of closing prices over a period of time.
      4. While Loop
Question: Create a loop that repeatedly checks a stock price from a real-time source every 10 seconds until the stock falls below a threshold value.
       In this scenario, print "Threshold Exceeded" when the threshold is crossed.
      5. For Loop
Question: You have data on the opening and closing prices of multiple stocks in a portfolio. 
      Using a for loop, calculate and print the total daily gain or loss for each stock in the portfolio.
      6.Nested Loops
Question: Create a nested loop that simulates a simple market-making strategy by placing buy and sell orders over a range of prices and volumes.
       Assume bid prices range from 90 to 100 and ask prices range from 101 to 110.
      7. Complex If-Else Logic
Question: You have a complex trading rule where a "Strong Buy" signal is given if the stock price is above
       both the 30-day and 50-day moving averages, a "Buy" signal is given if only above the 30-day, a "Hold" signal if above the 50-day, and a "Sell" signal otherwise. 
      Calculate the signals assuming you have daily prices for at least 50 days.
      8. Modules (numpy)
Question: Use the numpy module to calculate the rolling average for a window of 5 days over a numpy array containing 20 stock prices.
      9. Optimization with Loops
Question: Calculate the best day to buy and the best day to sell to maximize profit within a list of daily prices using a single pass of nested loops.
      10. Scenario Analysis
Question: Given that a certain algorithm follows a strategy where every time a stock gains 5% in value from the last recorded price, the program places a sell order. 
      Track the hypothetical prices over 15 days and identify when sell orders should be triggered.""")
try :
      n = int(input("Please Enter Your choise :- "))
      match n:
            case 1:
                  try: 
                        print("You have selected the 1st question")
                        def check_consecutive_drop(symbol,num_of_stock):
                              stock_prices = []
                              for i in range(num_of_stock):
                                    stock_prices.append(float(input(f"Please Enter the day {i+1} stock price of {symbol} :- ")))
                              print(f"All the stock prices of {symbol} which was given as input is :- {stock_prices}")
                              count = 0
                              for i in range(1,num_of_stock):
                                    if stock_prices[i] < stock_prices[i-1]:
                                          count+=1
                                          if count == 2:
                                                print(f"The stock prices of {symbol} has consecutive drop for 3 days or more")
                                                print(f"The stock prices of {symbol} which has consecutive drop for 3 days or more is :- {stock_prices[i-2:i+1]}. \n As the code has seen the drop for 3 days or more it will not check for the rest of the days")
                                                break
                                    else:
                                          count = 0
                              if count < 2:
                                    print(f"The stock prices of {symbol} does-not have consecutive drop for 3 days or more")

                              
                        symbol =input("Enter the symbol of the stock :- ")
                        num_of_stock=int(input(f"Please Enter the Number of stock values(i.e. the no of days) you want to enter of the stock {symbol} :- "))
                        
                        check_consecutive_drop(symbol,num_of_stock)
                  except Exception as e:
                        print(f"Their is an error in the input given by you. \n The error is {e}")

            case 2:
                  print("You have selected the 2nd question")
                  try:
                        def trade_stock(symbol,num_of_days,current_price):
                              daily_prices = []
                              weight_stk=[]
                              a=[]
                              for i in range(num_of_days):
                                    daily_prices.append(int(input(f"Please Enter the day {i+1} stock price of {symbol} :- ")))
                                    weight_stk.append(float(input(f"Please Enter the weight of the stock price of {symbol} on day {i+1} :- ")))
                                    a.append(daily_prices[i]*weight_stk[i])
                              print(f"All the stock prices of {symbol} which was given as input is :- {daily_prices} \n The weight of the stock prices of {symbol} which was given as input is :- {weight_stk} \n The calulated daily weightage of the stock prices of {symbol} is :- {a}\n The moving Average of the stock prices of {symbol} is :- {sum(a)/(sum(weight_stk)*num_of_days)}")
                              if current_price > sum(a)/sum(weight_stk):
                                    print("Buy Signal")
                              else:
                                    print("Sell Signal")
                        symbol =input("Enter the symbol of the stock :- ")
                        num_of_days=int(input(f"Please Enter the Number of total no of differnet days you want to enter of the stock {symbol} :- "))
                        current_price = int(input(f"Please Enter the current price of the stock {symbol} :- "))
                        trade_stock(symbol,num_of_days,current_price)
                  except Exception as e:
                        print(f"Their is an error in the input given by you. \n The error is {e}")

            case 3:
                  print("You have selected the 3rd question")
                  try:
                        import pandas as pd
                        def calculate_daily_percentage_change(file_path):
                              data = pd.read_excel(file_path)
                              data['Daily Percentage Change'] = data['Close'].pct_change()*100
                              print(f"The data of the file {file_path} is :- \n {data}")
                        file_path = input("Please Enter the file path of the file which you want to read :- ")
                        calculate_daily_percentage_change(file_path)

                  except Exception as e:
                        print(f"Their is an error in the input given by you. \n The error is {e}")
            
            case 4:
                  print("You have selected the 4th question")
                  try:
                        import yfinance as yf
                        import time

                        # Get user input
                        ticker = input("Enter stock symbol (e.g., AAPL): ").upper()
                        start_date = input("Enter start date (YYYY-MM-DD): ")
                        end_date = input("Enter end date (YYYY-MM-DD): ")
                        threshold = float(input("Enter threshold value: "))

                        def check_stock_price():
                              """Fetches the latest stock closing price within the given date range."""
                              stock = yf.Ticker(ticker)
                              stock_data = stock.history(start=start_date, end=end_date)

                              if stock_data.empty:
                                    print("No stock data available for the given date range.")
                                    return None  # Return None if no data is found
                              
                              return stock_data["Close"].iloc[-1]  # Get the last available closing price

                        # Continuous monitoring loop
                        while True:
                              current_price = check_stock_price()
                        
                              if current_price is not None:
                                    print(f"Current {ticker} price: ${current_price:.2f}")

                                    # Check if the price is below the threshold
                                    if current_price < threshold:
                                          print(f"⚠️ ALERT: {ticker} has dropped below the threshold of ${threshold:.2f} ⚠️")
                                          break  # Exit the loop when threshold is exceeded

                        # Wait 10 seconds before checking again
                        time.sleep(10)



                  except Exception as e:
                        print("Their is an error in the input given by you. \n The error is {e}")
            
            case 5:
                  print("You have selected the 5th question")
                  # Ask the user for the number of stocks
                  num_stocks = int(input("Enter the number of different stocks: "))

                  # Initialize an empty dictionary to store stock data
                  stocks = {}

                  # Loop to take input for each stock
                  def calculate_gain_loss(num_stocks):
                        for i in range(num_stocks):
                              stock_name = input(f"\nEnter name of stock {i+1}: ").upper()
                              opening_price = float(input(f"Enter opening price of {stock_name}: "))
                              closing_price = float(input(f"Enter closing price of {stock_name}: "))

                              stocks[stock_name]={
                                    "Opening Price": opening_price,
                                    "Closing Price": closing_price
                              }
                        
                        for stock, data in stocks.items():
                              gain_loss = data["Closing Price"] - data["Opening Price"]
                              print(f"\n{stock} Daily Gain/Loss: ${gain_loss:.2f}")
                        
                  calculate_gain_loss(num_stocks)

                        
            case 6:
                  print("You have selected the 6th question")
                  try:
                        def market_making_strategy():
                              bid_prices = range(90, 101)
                              price = range(101, 111)
                              for bid in bid_prices:
                                    for ask in price:
                                          print(f"Buy Order: {bid} | Sell Order: {ask}")
                        market_making_strategy()
                  except Exception as e:
                        print(f"Their is an error in the input given by you. \n The error is {e}")

            case 7:
                  print("You have selected the 7th question")
                  def complex_strategy(num):
                        stocks_prices = []
                        for i in range(num,stock_prc):
                              stocks_prices.append(float(input(f"Please Enter the day {i+1} stock price :- ")))
                        print(f"All the stock prices which was given as input is :- {stocks_prices}")
                        avg_30 = sum(stocks_prices[:30])/30
                        avg_50 = sum(stocks_prices[:50])/50
                        if stock_prc > avg_30 and stock_prc > avg_50:
                              print("Strong Buy Signal")
                        elif stock_prc > avg_30:
                              print("Buy Signal")
                        elif stock_prc > avg_50:
                              print("Hold Signal")
                        else:
                              print("Sell Signal")                                    
                  num=int(input("Enter the number of days for which you want to calculate the moving average :- "))
                  stock_prc=float(input("Enter the number of stock prices you want to enter :- "))
                  complex_strategy(num)


            case 8:
                  print("You have selected the 8th question")
                  import numpy as np
                  def calculate_rolling_average():
                        stock_prices = np.random.randint(50, 200, 20)
                        print(f"Stock Prices: {stock_prices}")
                        rolling_avg = np.convolve(stock_prices, np.ones(5)/5, mode='valid')
                        print(f"Rolling Average: {rolling_avg}")
                  calculate_rolling_average()

            case 9:
                  print("You have selected the 9th question")
                  def optimized_sale_stock(num,):
                        stock_prices = []
                        for i in range(num):
                              stock_prices.append(float(input(f"Please Enter the day {i+1} stock price :- ")))
                        print(f"All the stock prices which was given as input is :- {stock_prices}")
                        a,b=max(stock_prices),min(stock_prices)
                        max_profit = 0    
                        for i in range(num):
                              for j in range(i+1,num):
                                    if stock_prices[j]-stock_prices[i] > max_profit:
                                          max_profit = stock_prices[j]-stock_prices[i]
                                          buy_day = i+1
                                          sell_day = j+1
                        print(f"Best day to buy: Day {buy_day}")
                        print(f"Best day to sell: Day {sell_day}")
                        print(f"Maximum Profit: ${max_profit:.2f}")
                        

                  num = int(input("Enter the number of days for which you want to calculate the best day to buy and sell :- "))

                  optimized_sale_stock(num)


            case 10:
                  print("You have selected the 10th question")
                  def senario_analysis(num):
                        stock_prc = []
                        for i in range(num):
                              stock_prc.append(float(input(f"Please Enter the day {i+1} stock price :- ")))
                        print(f"All the stock prices which was given as input is :- {stock_prc}")
                        for i in range(num):
                              for j in range(i+1,num):
                                    if stock_prc[j] >= stock_prc[i]*1.05:
                                          print(f"\nSell order triggered on day {j+1} at price ${stock_prc[j]:.2f}.\nThe profit is ${stock_prc[j]-stock_prc[i]:.2f}\n")
                                          break

                        
                              
                  num=int(input("Enter the number of days for which you want to calculate the senario analysis :- "))
                  senario_analysis(num)
            case _:
                  print("You have selected the wrong option")

except Exception as e:
      print(f"Their is an error in the input given by you. \n The error is {e}")