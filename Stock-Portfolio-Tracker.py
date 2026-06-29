# Step 1: Define the hardcoded stock prices using a dictionary
stock_prices = {
    "AAPL": 180.00,
    "TSLA": 250.00,
    "GOOG": 150.00,
    "AMZN": 175.00,
    "MSFT": 400.00
}

# Step 2: Initialize variables
portfolio = {}       # Dictionary to store what the user buys (e.g., {"AAPL": 10})
total_value = 0.0    # Variable to track the grand total investment

print("📊 Welcome to the Stock Portfolio Tracker 📊")
print("Available stocks to track:", list(stock_prices.keys()))
print("-" * 45)

# Step 3: Main loop to get user input
while True:
    # Ask user for the stock ticker
    ticker = input("\nEnter stock ticker symbol (or type 'exit' to calculate total): ").upper().strip()
    
    # Check if the user wants to quit the loop
    if ticker == 'EXIT':
        break
        
    # Check if the stock exists in our database
    if ticker not in stock_prices:
        print(f"❌ '{ticker}' is not in our system. Please choose from: {list(stock_prices.keys())}")
        continue
        
    # Get the quantity from the user with basic error handling
    try:
        quantity = int(input(f"How many shares of {ticker} do you own? "))
        if quantity < 0:
            print("❌ Quantity cannot be negative.")
            continue
    except ValueError:
        print("❌ Invalid input. Please enter a whole number for shares.")
        continue
        
    # Add or update the stock in the user's portfolio
    if ticker in portfolio:
        portfolio[ticker] += quantity  # If they already added it, add more shares
    else:
        portfolio[ticker] = quantity   # If it's new, add it to the portfolio
        
    print(f"✅ Added {quantity} shares of {ticker} to your tracker.")

# Step 4 & 5: Calculate values and display the final summary
print("\n" + "="*15 + " PORTFOLIO SUMMARY " + "="*15)

# Line to store the text format for our file saving later
summary_text = "📊 STOCK PORTFOLIO REPORT 📊\n" + "-"*35 + "\n"

for ticker, shares in portfolio.items():
    current_price = stock_prices[ticker]
    stock_total_value = shares * current_price  # Arithmetic: Shares * Price
    total_value += stock_total_value            # Add to grand total
    
    # Format line for display and file
    line = f"{ticker}: {shares} shares @ ${current_price:.2f} each = ${stock_total_value:.2f}\n"
    print(line.strip())
    summary_text += line

summary_text += "-"*35 + f"\n📈 Total Investment Value: ${total_value:.2f}\n"

print("-" * 49)
print(f"📈 Total Investment Value: ${total_value:.2f}")
print("=" * 49)

# Step 6: Save the results to a text file
try:
    with open("portfolio_report.txt", "w") as file:
        file.write(summary_text)
    print("\n💾 Success! Your portfolio summary has been saved to 'portfolio_report.txt'.")
except Exception as e:
    print(f"\n⚠️ Could not save file due to an error: {e}")