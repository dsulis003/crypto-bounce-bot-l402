# 🚀 Crypto Auto-Bounce Momentum Bot (L402 M2M Powered)

An autonomous, plug-and-play Python trading bot that detects extreme market capitulation (crashes) and executes bounce strategies automatically.

Instead of running heavy calculations and managing local databases, this bot delegates the heavy lifting to the **Cascadespec M2M API Engine**. It uses a cutting-edge L402 pay-per-ping micro-transaction model on the Binance Smart Chain (BSC). 

## ⚡ Features
- **Zero Heavy Processing:** Logic is handled by a remote, high-speed VPS.
- **Dynamic Thresholds:** Set your own crash parameters (e.g., -5% or -10%).
- **Multi-Asset:** Supports any pair on Binance (BTCUSDT, SOLUSDT, etc.).
- **L402 Integration:** Automatically handles micro-payments (0.00005 BNB per ping) to unlock enterprise-grade data without monthly subscriptions.

## ⚙️ How to Run
1. Clone this repository.
2. Install requirements: `pip install web3 requests`
3. Open `bot.py` and insert your BSC Public Address and Private Key.
4. Run the bot: `python bot.py`

*Note: The bot autonomously sends a micro-fee on the BSC network to the data provider for every signal pull. Ensure you have a small amount of BNB for gas and fees.*