import time
import requests
from web3 import Web3

print("Starting Auto-Bounce Momentum Bot...")

# ==========================================
# USER CONFIGURATION (FILL THIS IN)
# ==========================================
USER_WALLET_ADDRESS = "YOUR_WALLET_ADDRESS"
USER_PRIVATE_KEY = "YOUR_PRIVATE_KEY"
SYMBOL_TO_TRADE = "BTCUSDT"
THRESHOLD = -5.0

# ==========================================
# L402 M2M DATA ENGINE (DO NOT MODIFY)
# ==========================================
BSC_RPC = "https://bsc-dataseed.binance.org/"
API_ENDPOINT = "https://rpc.cascadespec.com/api/v1/momentum"
DATA_PROVIDER_WALLET = "0x080a85599429398521ebad3ba5835c9e1a41edc6"
PAYMENT_AMOUNT_BNB = 0.00005  # Micro-fee for ultra-fast signal processing

w3 = Web3(Web3.HTTPProvider(BSC_RPC))

def pay_for_signal():
    """Send micro-payment to Data Provider to unlock the L402 API."""
    print("[1] Paying L402 M2M Invoice for real-time data...")
    nonce = w3.eth.get_transaction_count(USER_WALLET_ADDRESS)
    tx = {
        'nonce': nonce,
        'to': DATA_PROVIDER_WALLET,
        'value': w3.to_wei(PAYMENT_AMOUNT_BNB, 'ether'),
        'gas': 21000,
        'gasPrice': w3.to_wei('1', 'gwei'),
        'chainId': 56
    }
    
    signed_tx = w3.eth.account.sign_transaction(tx, USER_PRIVATE_KEY)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print(f"[*] Payment sent! TxHash: {w3.to_hex(tx_hash)}")
    
    # Wait for blockchain confirmation
    time.sleep(3)
    return w3.to_hex(tx_hash)

def fetch_momentum_data(tx_hash):
    """Retrieve processed signal using the TxHash as the access key."""
    print("[2] Requesting AI Momentum Signal...")
    headers = {"x-l402-payment": tx_hash}
    params = {"symbol": SYMBOL_TO_TRADE, "threshold": THRESHOLD}
    
    response = requests.get(API_ENDPOINT, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.text}")
        return None

def main():
    while True:
        try:
            receipt_hash = pay_for_signal()
            signal_data = fetch_momentum_data(receipt_hash)
            
            if signal_data and signal_data.get("signal") == "STRONG_BOUNCE_POTENTIAL":
                print(f"[!] DANGER/OPPORTUNITY: {SYMBOL_TO_TRADE} is crashing past {THRESHOLD}%!")
                print("[!] -> EXECUTE BUY ORDER HERE <-")
            else:
                print(f"[-] Market neutral. No action required for {SYMBOL_TO_TRADE}.")
                
            print("Waiting 1 hour for next analysis...\n")
            time.sleep(3600)
            
        except Exception as e:
            print(f"Bot encountered an error: {e}")
            time.sleep(60)

if __name__ == "__main__":
    main()
