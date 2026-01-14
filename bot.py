import os
import logging
from binance.client import Client
from binance.exceptions import BinanceAPIException
from dotenv import load_dotenv

logging.basicConfig(
    filename='trading_bot.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

load_dotenv()
API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_SECRET_KEY")


class BasicBot:
    def __init__(self):
        print("Connecting to Binance Testnet...")
        # 2. Connect to Testnet (Requirement: Use Testnet URL)
        self.client = Client(API_KEY, API_SECRET, testnet=True)
        logging.info("Bot initialized and connected to Testnet.")
        print("Connected successfully!")

    def place_order(self, symbol, side, order_type, quantity, price=None):
        """
        Places an order on Binance Futures.
        """
        try:
            logging.info(f"Attempting to place order: {side} {quantity} {symbol} @ {order_type}")
            
            params = {
                'symbol': symbol,
                'side': side,
                'type': order_type,
                'quantity': quantity,
            }

            if order_type == 'LIMIT':
                if not price:
                    raise ValueError("Price is required for LIMIT orders.")
                params['timeInForce'] = 'GTC'  # Good Till Cancelled
                params['price'] = price

            # API Call
            response = self.client.futures_create_order(**params)
            
            # Success Log
            logging.info(f"Order Success: {response['orderId']}")
            print(f"\n SUCCESS! Order ID: {response['orderId']}")
            print(f"Status: {response['status']}")
            return response

        except BinanceAPIException as e:
            # Error Log (Requirement: Log errors)
            logging.error(f"Binance API Error: {e.message}")
            print(f"\n API ERROR: {e.message}")
        except Exception as e:
            logging.error(f"System Error: {str(e)}")
            print(f"\n ERROR: {str(e)}")

    def get_balance(self):
        """Optional helper to check fake money balance"""
        try:
            account = self.client.futures_account()
            for asset in account['assets']:
                if asset['asset'] == 'USDT':
                    print(f"\n Wallet Balance: {asset['walletBalance']} USDT")
        except Exception as e:
            print(f"Error fetching balance: {str(e)}")

# 3. CLI Interface (Requirement: Command-line interface)
def main():
    if not API_KEY:
        print("Error: API Keys not found in .env file.")
        return

    bot = BasicBot()

    while True:
        print("\n--- ANKUSH'S TRADING BOT ---")
        print("1. Check Balance")
        print("2. Place MARKET Order")
        print("3. Place LIMIT Order")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ")

        if choice == '1':
            bot.get_balance()

        elif choice in ['2', '3']:
            symbol = input("Enter Symbol (e.g., BTCUSDT): ").upper()
            side = input("Enter Side (BUY or SELL): ").upper()
            qty = float(input("Enter Quantity (e.g., 0.01): "))

            if choice == '2':
                bot.place_order(symbol, side, 'MARKET', qty)
            elif choice == '3':
                price = float(input("Enter Limit Price: "))
                bot.place_order(symbol, side, 'LIMIT', qty, price)

        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid selection.")

if __name__ == "__main__":
    main()