# Complex String Manipulation with Loops
# Question: Given a string of mixed data containing symbols and prices like "AAPL100GOOG200MSFT300", write a script to extract and print each symbol with its corresponding price on separate lines.
# Using Break and Continue in Data Cleaning (This topic is covered in the next session 4)
# Question: You are processing log data from trades. Stop processing if you encounter "ERROR" in the logs and skip any logs that start with "#".
# String Slicing and Indexing
# Question: Given a long string of security transaction details formatted as "Buy100AAPLSell200GOOG", where each segment starts with a transaction type followed by the amount and the ticker, print each transaction detail on a new line.
# Nested Loops with String Functions
# Question: Create a nested loop that reads a string of stock symbols separated by commas, then prints each symbol and its reverse.
# Advanced String Manipulation
# Question: Given a block of text representing a financial report, replace any instance of financial terms with their uppercase counterparts. The terms are "revenue", "cost", "profit".
# Complex Data Extraction
# Question: Extract stock symbols and their respective share counts from a string like "Buy 50 AAPL and sell 30 GOOG", ensuring that only valid transactions (Buy/Sell) are processed.
# Iterative Data Cleaning with Strings
# Question: Given a list of raw financial data points like " 
# 3,000 ", clean the data by removing spaces, dollar signs, and commas, then convert them to integers.
# String and Loop Integration
# Question: From a formatted string containing dates and prices like "20210101
# 200", extract and print the date and price pairs.
# String Parsing and Control Flow
# Question: Parse a string "High: 100, Low: 90, Open: 95, Close: 98" and print each value only if it is higher than 95.

# Advanced String Processing
# Question: Convert a string representation of an options trade from "Call100AAPL20240101Put200GOOG20240102" into a structured report indicating each trade's type, volume, symbol, and date.


# print("Enter yur choice: ")
choise=int(input("Enter your choice as per the question given above: "))
match choise:
    case 1:
        print("You have choosen question no 1")
        try: 
            print("GIVEN STRING: AAPL100GOOG200MSFT300")
            data = "AAPL100GOOG200MSFT300"
            i = 0
            for i in range(0,len(data),7):
                symbol_price = data[i:i+4]
                price_each=data[i+4:i+7]
                print(symbol_price, price_each)        
        except Exception as e:
            print("Error: ", e)
    case 2:
        print("You have choosen question no 2")
        try:
            def processing_logs(logs):
                for log in logs:
                    if log.startswith("#"):
                        continue
                    if "ERROR" in log:
                        break
                    print(log)
            logs = ["#INFO: Trade completed", "ERROR: Trade failed", "INFO: Trade completed"]
            processing_logs(logs)

        except Exception as e:
            print("Error: ", e)
    case 3:
        print("You have choosen question no 3")
        print("You have chosen question no 3")
        # Given string of security transaction details
        data = "BUY100AAPLSell200GOOG"

        # Convert to uppercase to handle inconsistent casing
        data = data.upper()
        a=data.find("S")
        # Iterate over the string in chunks of 9 characters
        for i in range(0, len(data), 9):
            transc_type = data[i:i+3]  # First 3 characters for transaction type
            amount = data[i+3:i+6]      # Next 3 characters for amount
            ticker = data[i+6:i+10] 
            
                 # Last 3 characters for ticker symbol
            print(f"{transc_type} {amount} {ticker} {a}")
    case 4:

        print("You have choosen question no 4")
        try:
            def read_stk(num):
                for i in range(num):
                    stk = input("Enter the stock symbols separated by commas: ")
                    print("in order | reverse order")
                    for s in stk.split(","):

                        print(F"  {s}  |  {s[::-1]}  ")
            # Read the number of stocks
                pass
            num =int(input("Enter the number of stocks: "))
            read_stk(num)
        except Exception as e:
            print("Error: ", e)
    case 5:
        print("You have choosen question no 5")
        try:

            def replace_text():
                text= input("Enter the text: ")
                text = text.replace("revenue", "REVENUE")
                text = text.replace("cost", "COST")
                text = text.replace("profit", "PROFIT")
                print(text)
            replace_text()

        except Exception as e:
            print("Error: ", e)
    case 6:
        print(f"You have choosen question no 6 \n")
        try:
            def valid_transaction():
                num = int(input("Enter the number of transactions: "))
                print("The format for transaction is Buy 100 AAPL ")
                space_index,transc_details=[],[]
                for i in range(num):
                    transc_details.append(input(f"\nEnter the transaction details number {i+1}: "))

                    space_index =   [ j    for j, char in enumerate(transc_details[i])    if char ==" " ]
                    for transc in transc_details:
                            if "BUY" in transc.upper():
                                print( "BUY -:Signal ")
                                print((transc[space_index[0]:space_index[1]]),":- No of Shares")
                                print(transc[space_index[1]:]," :- Stock Signal or Symbol")
                            elif "SELL" in transc.upper():
                                print( "SELL -:Signal ")
                                print((transc[space_index[0]:space_index[1]])," -:  No of Shares")
                                print(transc[space_index[1]:]," -:  Stock Signal or Symbol")
                            else:
                                print("Invalid Transaction")          
            valid_transaction()                      
        except Exception as e:
            print(" Error", e)
    case 7:
        print("You have choosen question no 7")
        try:
            def num_check(num):
                a,b,c=" ",0,[]
                match num:
                    case "1": a= True
                    case "2": a= True
                    case "3": a= True
                    case "4": a= True
                    case "5": a= True
                    case "6": a= True
                    case "7": a= True
                    case "8": a= True
                    case "9": a= True
                    case "0": a= True
                    case "_": a=False
                return a
                 
            def print_data(actual_entry,refined_entry):
                print(f"Original Entry:- {actual_entry}")
                prin
                pass
            
            def cleaning_input():
                num = int(input("Enter the number of data you want to give as input go fot future cleaning purpose: "))
                print(f"Format is stock price,stock name,stock price currency. \nExample:- 1000AAPL$2500KOEuro")
                semicolen_index,data=[],[]
                for i in range(num):
                    data.append(input(f"Enter the data number {i+1} :- "))
                    data_loc_1=data[i]
                    # num_check(data[i])                    
                    for j in range(data[i].length()):
                        b=[]
                        if num_check(data_loc_1[0])==False:
                            print("please start with a Numerical value at the begining to get a good result.\n")
                            break
                        else:
                            if num_check(data_loc_1[j]) == True:
                                b.append(data_loc_1[j])
                            else:
                                if j>0 and b[j-1]!=",":
                                    b.append(",")
                    print_data(data[i],b)
                    semicolen_index =   [ k    for k, char in enumerate(b)    if char =="," ]
                    
                

                
            cleaning_input()
        except Exception as e:
            print("Error :- ", e)

    case 8:
        print("You have choosen question no 8")
    case 9:
        print("You have choosen question no 9")
    case 10:
        print("You have choosen question no 10")
    case _:
        print("Invalid Choice")




