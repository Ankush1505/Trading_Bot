#  Binance Futures Trading Bot (Testnet)

A Python-based CLI trading bot that interacts with the Binance Futures Testnet API. This bot allows users to check balances and place Market/Limit orders using the `python-binance` library.

## -- Features
* **Authentication:** Securely loads API keys using `.env` variables.
* **Order Management:** Supports **MARKET** and **LIMIT** orders for Futures trading.
* **Account Info:** Real-time wallet balance checking (USDT).
* **Robust Logging:** Tracks all requests, order IDs, and errors in `trading_bot.log`.
* **Error Handling:** Gracefully handles API exceptions (e.g., insufficient funds, network issues).

## -- Prerequisites
* Python 3.8+
* Binance Futures Testnet Account

## -- Installation

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/Ankush1505/Trading_Bot.git](https://github.com/Ankush1505/Trading_Bot.git)
    cd Trading_Bot
    ```

2.  **Create and Activate Virtual Environment**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Mac/Linux
    # venv\Scripts\activate   # On Windows
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

## -- Configuration

1.  Create a `.env` file in the root directory.
2.  Copy the structure from `.env.example`:
    ```bash
    cp .env.example .env
    ```
3.  Add your **Binance Futures Testnet** keys to the `.env` file:
    ```env
    BINANCE_API_KEY=your_testnet_api_key_here
    BINANCE_SECRET_KEY=your_testnet_secret_key_here
    ```

> **Note:** Get your keys from [testnet.binancefuture.com](https://testnet.binancefuture.com/en/futures/BTCUSDT). Ensure you are NOT using Spot keys.

##  Usage

Run the bot:
```bash
python bot.py
```

## -- Menu Options:

Check Balance: Displays current USDT Testnet balance.

Place MARKET Order: Instantly buys/sells at the current market price.

Place LIMIT Order: Places an order at a specific price target.

Exit: Closes the application.

## -- Logs & Troubleshooting
Logs: All activities are saved to trading_bot.log. Check this file for detailed error messages or order IDs.

Known Issue (Error -2015): If you see APIError(code=-2015): Invalid API-key, IP, or permissions, this typically indicates that the keys were generated on the wrong Testnet (Spot vs Futures) or are being restricted by region/IP. 
The bot logic is functional, but the connection is refused by Binance security.

## --- Note: 
This repository includes a .gitignore file to ensure sensitive .env credentials and log files are never uploaded to GitHub.



