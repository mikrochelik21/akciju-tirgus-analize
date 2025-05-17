import requests
from bs4 import BeautifulSoup

def get_stock_news(ticker):
    url = f"https://finance.yahoo.com/quote/{ticker}/news/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200: ## if !200
        soup = BeautifulSoup(response.content, 'html.parser')
        news_containers = soup.find_all('div', class_='content')

        headlines = []
        for container in news_containers[:5]: 
            headline_tag = container.find('h3', class_='clamp')
            if headline_tag:
                headlines.append(headline_tag.text.strip())
        
        print(f"\nTop 5 Recent News Headlines for {ticker}:")
        for i, headline in enumerate(headlines, 1):
            print(f"{i}. {headline}")
    else:
        print(f"Fail. Status code: {response.status_code}")

def get_stock_data(ticker):
    url = f"https://finance.yahoo.com/quote/{ticker}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Fail. Status code: {response.status_code}")
        return

    soup = BeautifulSoup(response.content, 'html.parser')
    
    price_tag = soup.find("span", {"data-testid": "qsp-price"})
    price = price_tag.text if price_tag else "N/A"
    
    percent_tag = soup.find("span", {"data-testid": "qsp-price-change-percent"})
    percent = percent_tag.text if percent_tag else "N/A"
    
    previous_close_tag = soup.find('fin-streamer', {"data-field": "regularMarketPreviousClose"})
    previous_close = previous_close_tag.text if previous_close_tag else "N/A"

    day_range_tag = soup.find('fin-streamer', {"data-field": "regularMarketDayRange"})
    day_range = day_range_tag.text if day_range_tag else "N/A"
    
    fiftytwo_week_range_tag = soup.find('fin-streamer', {"data-field": "fiftyTwoWeekRange"})
    fiftytwo_week_range = fiftytwo_week_range_tag.text if fiftytwo_week_range_tag else "N/A"
    
    market_cap_tag = soup.find('fin-streamer', {"data-field": "marketCap"})
    market_cap = market_cap_tag.text if market_cap_tag else "N/A"
    
    pe_ratio_tag = soup.find('fin-streamer', {"data-field": "trailingPE"})
    pe_ratio = pe_ratio_tag.text if pe_ratio_tag else "N/A"
    
    avg_volume_tag = soup.find('fin-streamer', {"data-field": "averageVolume"})
    avg_volume = avg_volume_tag.text if avg_volume_tag else "N/A"
    
    print(f"\nStock Data for {ticker}:")
    print("----------------------------")
    print(f"Current Price: {price}")
    print(f"Change: {percent}")
    print(f"Previous Close: {previous_close}")
    print(f"Day Range: {day_range}")
    print(f"52-Week Range: {fiftytwo_week_range}")
    print(f"Market Cap: {market_cap}")
    print(f"PE Ratio : {pe_ratio}")
    print(f"Average Volume: {avg_volume}")

def get_dividend_info(ticker):
    url = f"https://finance.yahoo.com/quote/{ticker}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Fail. Status code: {response.status_code}")
        return

    soup = BeautifulSoup(response.content, 'html.parser')

    label = soup.find('span', string="Forward Dividend & Yield")
    label2 = soup.find('span', string="Ex-Dividend Date")
    dividend = "N/A"
    ex_dividend = "N/A"

    if label:
        parent_li = label.find_parent('li')
        if parent_li:
            value_span = parent_li.find('span', class_='value yf-1jj98ts')
            if value_span:
                dividend = value_span.text.strip()
    if label2:
        parent_li2 = label2.find_parent('li')
        if parent_li2:
            value_span2 = parent_li2.find('span', class_='value yf-1jj98ts')
            if value_span2:
                ex_dividend = value_span2.text.strip()

    print(f"\nDividend Info for {ticker}:")
    print("----------------------------")
    print(f"Forward Dividend & Yield: {dividend}")
    print(f"Ex-Dividend Date: {ex_dividend}")

def get_earnings_info(ticker):
    url = f"https://finance.yahoo.com/quote/{ticker}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Fail. Status code: {response.status_code}")
        return

    soup = BeautifulSoup(response.content, 'html.parser')
    label = soup.find('span', string="Earnings Date")
    label2 = soup.find('span', string="EPS (TTM)")
    date = "N/A"
    eps = "N/A"

    if label:
        parent_li = label.find_parent('li')
        if parent_li:
            value_span = parent_li.find('span', class_='value yf-1jj98ts')
            if value_span:
                date = value_span.text.strip()
    if label2:
        parent_li2 = label2.find_parent('li')
        if parent_li2:
            value_span2 = parent_li2.find('span', class_='value yf-1jj98ts')
            if value_span2:
                eps = value_span2.text.strip()


    print(f"\nEarnings Info for {ticker}:")
    print("----------------------------")
    print(f"Earnings Date: {date}")
    print(f"EPS: {eps}")

def get_holders_info(ticker):
    url = f"https://finance.yahoo.com/quote/{ticker}/holders"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("Fail.")
        return

    soup = BeautifulSoup(response.content, 'html.parser')
    rows = soup.find_all('tr', class_='majorHolders yf-1toamfi')

    print(f"\nMajor Holders Info for {ticker}:")
    print("--------------------------------")

    for row in rows:
        cells = row.find_all('td')
        if len(cells) >= 2:
            value = cells[0].text.strip()
            label = cells[1].text.strip()

            print(value + ": " + label)

def stock_summary_menu():
    ticker = input("Enter stock ticker (e.g., AAPL): ").upper()
    print(f"\nWhat would you like to see for {ticker}?")
    print("1) Stock Data")
    print("2) Dividend Info")
    print("3) Earnings Date")
    print("4) Major Holders")
    print("5) Latest News")
    #print("6) Full Summary")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        get_stock_data(ticker)
    elif choice == "2":
        get_dividend_info(ticker)
    elif choice == "3":
        get_earnings_info(ticker)
    elif choice == "4":
        get_holders_info(ticker)
    elif choice == "5":
        get_stock_news(ticker)
    else:
        print("Invalid choice.")
def get_top_gainers():
    url = "https://finance.yahoo.com/markets/stocks/gainers/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Fail. Status code: {response.status_code}")
        return
    
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table')

    rows = table.find_all('tr')[1:]

    print("\nTop 5 Gainers:")
    print("-------------------")
    for row in rows[:5]:
        cols = row.find_all('td')
        if len(cols) >= 7:
            symbol = cols[0].text.strip()
            name = cols[1].text.strip()
            percent_change = cols[5].text.strip()
            print(f"{symbol} - {name}: {percent_change}")
def get_top_losers():
    url = "https://finance.yahoo.com/markets/stocks/losers/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Fail. Status code: {response.status_code}")
        return
    
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table')

    rows = table.find_all('tr')[1:]

    print("\nTop 5 Losers:")
    print("-------------------")
    for row in rows[:5]:
        cols = row.find_all('td')
        if len(cols) >= 7:
            symbol = cols[0].text.strip()
            name = cols[1].text.strip()
            percent_change = cols[5].text.strip()
            print(f"{symbol} - {name}: {percent_change}")

def market_movers_menu():
    get_top_gainers()
    get_top_losers()

def market_overview_menu():
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    
    indexes = {
        "S&P 500": "^GSPC",
        "Dow Jones": "^DJI",
        "NASDAQ": "^IXIC"
    }

    print("\nMarket Overview:")
    print("------------------")
    
    for name, ticker in indexes.items():
        url = f"https://finance.yahoo.com/quote/{ticker}"
        response = requests.get(url, headers=headers)
        
        if response.status_code != 200:
            print(f"Fail. Status code: {response.status_code}")
            continue
    
        soup = BeautifulSoup(response.content, 'html.parser')
    
        price_tag = soup.find('span', {'data-testid': 'qsp-price'})
        percent_tag = soup.find('span', {'data-testid': 'qsp-price-change-percent'})

        price = price_tag.text if price_tag else "N/A"
        percent = percent_tag.text if percent_tag else "N/A"

        print(f"{name} ({ticker}): Price: {price}, Change: {percent}")

def ipo_info():
    url = "https://www.iposcoop.com/ipo-calendar/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Fail. Status code: {response.status_code}")
        return

    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table')

    rows = table.find_all('tr')[1:]
    print("\nTop 5 Upcoming IPOs:")
    print("-----------------------------")

    count = 0
    for row in rows:
        if count >= 5:
            break
        cols = row.find_all('td')
        if len(cols) >= 9:
            company_name = cols[0].text.strip()
            ticker = cols[1].text.strip()
            trade_date = cols[-3].text.strip()
            print(f"{ticker} - {company_name}: Expected to Trade on ({trade_date})")
            count += 1
def earnings_info():
    url = "https://www.marketbeat.com/earnings/conference-calls/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Fail. Status code: {response.status_code}")
        return
    print("\nUpcoming Earnings Calls:")
    print("-------------------------")

    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table')

    if table:
        rows = table.find_all('tr')[1:6]
        for row in rows:
            cols = row.find_all('td')
            if len(cols) >= 2:
                company = cols[0].get_text(strip=True)
                date = cols[1].get_text(strip=True)
                print(f"{company}: Earnings Call on ({date})")

def upcoming_events_menu():
    ipo_info()
    earnings_info()

def main():
 ##while True:
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
        ##break
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
