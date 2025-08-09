# Telegram Finance Tracker Bot

A Telegram bot to log expenses into Google Sheets.  

---

## Features
- Adding expenditures
- Google Sheets append via service account
- Secure config with `.env`

---

## Prerequisites
- Python 3.10+ recommended
- A Google Cloud **service account** JSON key
- A Google Sheet shared with the service account (Editor access)

#### Note: If you are unsure of how to set up the Google Cloud and sheet, click [here](GoogleCloudSetup.md).

---

## Quick Start

#### 1. Install the specified requirements
`pip install -r requirements.txt`

#### 2. Clone and install

`git clone https://github.com/<your-username>/finance-tracker.git`

#### 3. Change directory to tracker
`cd finance-tracker`

#### 4. Create .env file in the directory
```bash
# Telegram
TOKEN=123456789:ABC-xyz_ExampleToken
BOT_USERNAME=@your_bot_username

# Google Sheets
GOOGLE_SA_KEY_FILE=./service_account.json
SHEET_NAME=YourSheetName
WORKSHEET=Sheet1
