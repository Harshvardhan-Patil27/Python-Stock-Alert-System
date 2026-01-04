import smtplib  # Tool to send emails
import requests # Tool to fetch data
import time     # Tool to wait/sleep

# --- CONFIGURATION (Change these!) ---
EMAIL_ADDRESS = "abcd@gmail.com"  # Your email
EMAIL_PASSWORD = "mtwb iwsa bnzf poyu"  # Your 16-letter App Password
TARGET_PRICE = 3500                     # The price you want to buy at
STOCK_SYMBOL = "TCS.NS"                 # Stock symbol (TCS, RELIANCE, etc.)

def get_live_price(symbol):
    # This is the logic from Day 18
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        # Navigate the dictionary to find the price
        price = data['chart']['result'][0]['meta']['regularMarketPrice']
        return price
    except Exception as e:
        print(f"Error fetching price: {e}")
        return None

def send_email_alert(price):
    # 1. Connect to Gmail's Server (The Post Office)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls() # Secure the connection (Encrypt the data)
    
    try:
        # 2. Login
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        
        # 3. Write the Email
        subject = f"ALERT: Buy {STOCK_SYMBOL} Now!"
        body = f"Good News! {STOCK_SYMBOL} has dropped to {price}.\n\nThis is your Python Bot."
        msg = f"Subject: {subject}\n\n{body}"
        
        # 4. Send the Email
        # (From Address, To Address, Message)
        server.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg)
        print("✅ Email Alert Sent Successfully!")
        
    except Exception as e:
        print(f"❌ Email Failed: {e}")
    finally:
        server.quit() # Always disconnect from the server

# --- MAIN LOGIC ---
print(f"--- Checking {STOCK_SYMBOL} ---")
current_price = get_live_price(STOCK_SYMBOL)

if current_price:
    print(f"Current Price: {current_price}")
    
    # THE DECISION MAKER
    if current_price < TARGET_PRICE:
        print("📉 Price is low! Sending alert...")
        send_email_alert(current_price)
    else:
        print(f"Waiting... Price needs to drop below {TARGET_PRICE}")
else:
    print("Could not fetch price.")