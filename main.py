import requests
from bs4 import BeautifulSoup

def get_stock_news(ticker):
    url = f"https://finance.yahoo.com/quote/{ticker}/news/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
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
        print("Failed to get data.")
        return

    soup = BeautifulSoup(response.content, 'html.parser')
    
    print(f"\nMajor Holders Info for {ticker}:")
    print("--------------------------------")
    rows = soup.find_all('tr', class_='majorHolders yf-1toamfi')
    for row in rows:
        cells = row.find_all('td')
        if len(cells) >= 2:
            value = cells[0].text.strip()
            label = cells[1].text.strip()
            print(value + ": " + label)

    institutional_section = soup.find('section', {'data-testid': 'holders-top-institutional-holders'})
    if institutional_section:
        print("\nTop 5 Institutional Holders:")
        print("----------------------------")
        table = institutional_section.find('table')
        if table:
            rows = table.find_all('tr', class_='yf-idy1mk')[1:6]
            for row in rows:
                cells = row.find_all('td')
                if len(cells) >= 4:
                    holder = cells[0].text.strip()
                    percentage = cells[3].text.strip()
                    print(f"{holder}: {percentage}")
        else:
            print("Institutional holders data not available")
    else:
        print("\nNo institutional holders information found")

def get_full_summary(ticker):
    get_stock_data(ticker)
    
    sector, industry = get_sector_industry(ticker)
    print(f"\nSector: {sector}")
    print(f"Industry: {industry}")
    
    get_dividend_info(ticker)
    get_earnings_info(ticker)
    
    get_holders_info(ticker)
    
    get_stock_news(ticker)


def stock_summary_menu():
    ticker = input("Enter stock ticker (e.g., AAPL): ").upper()
    print(f"\nWhat would you like to see for {ticker}?")
    print("1) Stock Data")
    print("2) Dividend Info")
    print("3) Earnings Date")
    print("4) Major Holders")
    print("5) Latest News")
    print("6) Full Summary")
    
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
    elif choice == "6":
        get_full_summary(ticker)
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
                first_col = cols[0]
                ticker_div = first_col.find('div', class_='ticker-area')
                title_div = first_col.find('div', class_='title-area')
                
                if ticker_div and title_div:
                    ticker = ticker_div.get_text(strip=True)
                    company_name = title_div.get_text(strip=True)
                    company = f"{ticker} - {company_name}"
                else:
                    company = first_col.get_text(strip=True)
                
                date = cols[1].get_text(strip=True)
                print(f"{company}: Earnings Call on ({date})")

def get_sector_industry(ticker):
    url = f"https://finance.yahoo.com/quote/{ticker}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    
    sector = "N/A"
    industry = "N/A"
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        overview_section = soup.find('section', {'data-testid': 'company-overview-card'})
        
        if overview_section:
            info_sections = overview_section.find_all('div', class_='infoSection yf-1ja4ll8')
            for section in info_sections:
                header = section.find('h3', class_='yf-1ja4ll8')
                if header:
                    if header.text.strip() == 'Sector':
                        sector_tag = section.find('p', class_='yf-1ja4ll8') or section.find('a')
                        sector = sector_tag.text.strip() if sector_tag else "N/A"
                    elif header.text.strip() == 'Industry':
                        industry_tag = section.find('p', class_='yf-1ja4ll8') or section.find('a')
                        industry = industry_tag.text.strip() if industry_tag else "N/A"
    
    return sector, industry

def upcoming_events_menu():
    ipo_info()
    earnings_info()

def trending_stocks():
    url = "https://finance.yahoo.com/markets/stocks/trending/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("Failed to get trending stocks.")
        return

    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', class_='yf-1570k0a')
    
    if not table:
        print("No trending stocks found.")
        return

    stocks = []
    rows = table.find_all('tr', class_='row yf-1570k0a')[:5]
    
    for row in rows:
        symbol_tag = row.find('a', {'data-testid': 'table-cell-ticker'})
        name_tag = row.find('div', class_='leftAlignHeader yf-362rys enableMaxWidth')
        
        if symbol_tag and name_tag:
            symbol = symbol_tag.text.strip()
            name = name_tag.text.strip()
            sector, industry = get_sector_industry(symbol)
            stocks.append((symbol, name, f"{sector}/{industry}"))
    
    if not stocks:
        print("No trending stocks data available.")
        return

    print("\nTop 5 Trending Stocks:")
    print("-----------------------")
    for i, (symbol, name, sector_industry) in enumerate(stocks, 1):
        print(f"{i}. {symbol} - {name} - {sector_industry}")
    
    while True:
        choice = input("\nSelect a stock (1-5) to see news, or '0' to return back: ")
        if choice.lower() == '0':
            break
        try:
            index = int(choice) - 1
            if 0 <= index < len(stocks):
                selected_symbol = stocks[index][0]
                get_stock_news(selected_symbol)
            else:
                print("Invalid choice. Please enter a number between 1-5.")
        except ValueError:
            print("Invalid input. Please enter a number or '0' to quit.")

def main():
    while True:
        print("\n>>> Stock Market Dashboard <<<")
        print("1) Your Stock Summary")
        print("2) Trending Now Stocks")
        print("3) Market Movers (Top Gainers / Losers)")
        print("4) Market Overview (Indexes)")
        print("5) Upcoming Market Events")
        print("0) Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            stock_summary_menu()
        elif choice == "2":
            trending_stocks()
        elif choice == "3":
            market_movers_menu()
        elif choice == "4":
            market_overview_menu()
        elif choice == "5":
            upcoming_events_menu()
        elif choice == "0":
            print("Goodbye")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
