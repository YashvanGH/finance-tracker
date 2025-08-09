import os

# Module for splitting strings the way a shell (like bash or PowerShell)
# Quoted text will stay together after a split call
import shlex

# For writing to google sheets
import gspread

from datetime import datetime

# Allows loading of env variables / .env file
from dotenv import load_dotenv

from typing import Final

from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

# To get the service account linked to the finance tracker
from google.oauth2.service_account import Credentials

load_dotenv()

# Load .env variables
TOKEN:Final = os.getenv("TOKEN") 
BOT_USERNAME:Final = os.getenv("BOT_USERNAME")
GOOGLE_SA_KEY_FILE: Final = os.getenv("GOOGLE_SA_KEY_FILE")
SHEET_NAME: Final = os.getenv("SHEET_NAME")
WORKSHEET: Final = os.getenv("WORKSHEET")

# Google sheet helpers
# Tells Google Auth which permissions the bot is requesting when authenticating
_scopes = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

def get_worksheet():
    creds = Credentials.from_service_account_file(GOOGLE_SA_KEY_FILE, scopes = _scopes)
    google_client = gspread.authorize(creds)
    sheet = google_client.open(SHEET_NAME)
    return sheet.worksheet(WORKSHEET)

def append_expense(amount: float, category: str, note: str):
    worksheet = get_worksheet()
    worksheet.append_row(
        [
            datetime.now().strftime("%d-%m-%Y"),
            category,
            round(float(amount), 2),
            note
        ], value_input_option="USER_ENTERED"
    )
    
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Please track your expenses!")

async def add_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        parts = shlex.split(update.message.text)
        
        if len(parts) < 3:
            return await update.message.reply_text(
                "Please use the format: /add <amount> <category> <note>\nExample: /add 12.50 lunch chicken rice"
            )
        
        amount = float(parts[1])
        category = parts[2]
        note = " ".join(parts[3:]) if len(parts) > 3 else ""

        append_expense(amount, category, note)
        await update.message.reply_text("Ok! Expense has been tracked! Anything else? 💳")
    except ValueError:
        pass

if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()
    
    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler("add", add_command))
    app.run_polling(poll_interval=5)