import gspread
import os
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

class GoogleSheetsService:
    def __init__(self):
        self.scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        self.creds_path = os.getenv("CREDS_FILE", "m3gan_credentials.json")
        self.sheet_name = os.getenv("SHEET_NAME", "M3GAN AI")
        self.client = self._authenticate()
        self.sheet = self.client.open(self.sheet_name).sheet1

    def _authenticate(self):
        creds = ServiceAccountCredentials.from_json_keyfile_name(self.creds_path, self.scope)
        return gspread.authorize(creds)

    def append_inquiry(self, inquiry_data):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        row = [
            inquiry_data.name,
            inquiry_data.email,
            inquiry_data.country,
            inquiry_data.mobile,
            inquiry_data.message,
            timestamp
        ]
        return self.sheet.append_row(row)

# Create a single instance to be used across the app
gs_service = GoogleSheetsService()