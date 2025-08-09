# Google Cloud Setup for Telegram Finance Tracker Bot

This guide covers how to create and configure a Google Cloud **Service Account** so the bot can write to Google Sheets.

---

## 1. Create or select a Google Cloud project
1. Go to [Google Cloud Console](https://console.cloud.google.com/).
2. At the top, click the **project selector** → **New Project** (or select an existing one).
3. Give it a name (e.g. `FinanceBotSheets`) and click **Create**.

---

## 2. Enable required APIs
You must enable:
- **Google Sheets API**
- **Google Drive API**

**Steps:**
1. In the top search bar, type "Google Sheets API" → click → **Enable**.
2. Repeat for "Google Drive API".

---

## 3. Create a service account
1. Search for: **IAM & Admin → Service Accounts**. 
2. Click **+ Create Service Account**.
3. Fill in:
   - Name: `my-finance-bot`
   - Description: _optional_
4. Click **Create and Continue**.
5. (Optional) Assign role: **Editor** (or leave blank — Sheets sharing will control access).
6. Click **Done**.

---

## 4. Generate and download the JSON key
1. Click your new service account in the list.
2. Go to the **Keys** tab.
3. Click **Add key → Create new key**.
4. Select **JSON** → **Create**.
5. Save the file (e.g. `service_account.json`) to your project folder.

---

## 5. Share your Google Sheet with the service account
1. Open your target Google Sheet.
2. Click **Share**.
3. Paste the service account’s email (from the JSON file, looks like: your-sa-name@your-project-id.iam.gserviceaccount.com)
4. Give it **Editor** access.
5. Save.

## 6. Update `.env`
In your bot’s `.env` file:
```env
GOOGLE_SA_KEY_FILE=./service_account.json
SHEET_NAME=FinanceTracker
WORKSHEET=Sheet1
