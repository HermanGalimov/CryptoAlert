# CryptoAlert

A simple FastAPI service to monitor cryptocurrency prices using the CoinGecko API.  
Users can set alert rules (above/below thresholds or percentage changes), and the bot will send notifications via Telegram or Discord.

## Features
- Add rules for crypto price alerts.
- Rules types: above X, below Y, percentage change over a lookback window.
- Periodic polling of CoinGecko API with APScheduler.
- Send alerts via Telegram or Discord.
- Cooldown to prevent spam.

## Quickstart
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/crypto-alert.git
   cd crypto-alert
