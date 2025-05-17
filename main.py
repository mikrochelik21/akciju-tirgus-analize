import requests
from bs4 import BeautifulSoup

def get_stock_data(ticker):
    pass

def get_stock_news(ticker):
    pass

def get_dividend_info(ticker):
    pass

def get_earnings_info(ticker):
    pass

def get_holders_info(ticker):
    pass

def stock_summary_menu():
    pass

def get_top_gainers():
    pass

def get_top_losers():
    pass

def market_movers_menu():
    pass

def market_overview_menu():
    pass

def ipo_info():
    pass

def earnings_info():
    pass

def upcoming_events_menu():
    pass

def main():
    print("\n>>> Stock Market Dashboard <<<")
    print("1) Your Stock Summary")
    print("2) Market Movers (Top Gainers / Losers)")
    print("3) Market Overview (Indexes)")
    print("4) Upcoming Market Events")
    print("5) Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        stock_summary_menu()
    elif choice == "2":
        market_movers_menu()
    elif choice == "3":
        market_overview_menu()
    elif choice == "4":
        upcoming_events_menu()
    elif choice == "5":
        print("Goodbye")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
