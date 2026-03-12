import os
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

class GoogleSheetsService:
    def __init__(self):
        self.client = None
        self.sheet = None
        self.scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

    def connect(self):
        """Authenticates with Google on server startup."""
        creds_json = os.getenv("GOOGLE_CREDS_JSON")
        sheet_name = os.getenv("SHEET_NAME", "M3GAN AI")

        print('=============creds_json===============', creds_json, type(creds_json))
        try:
            if creds_json:

                try:
                    # local environment - read files
                    with open(creds_json, 'r') as file:
                        creds_info = json.load(file)

                    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_info, self.scope)
                except:
                    
                    creds_json = json.loads(creds_json)
                    # Use environment variable (Production/Vercel)
                    # vercel {} format accept
                    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_json, self.scope)
            else:
                # Use local file (Development)
                creds = ServiceAccountCredentials.from_json_keyfile_name("m3gan_credentials.json", self.scope)
            
            self.client = gspread.authorize(creds)
            self.sheet = self.client.open(sheet_name).sheet1
            print(f"✅ Connected to Google Sheet: {sheet_name}")
        except Exception as e:
            print(f"❌ Failed to connect to Google Sheets: {e}")
            raise e

    def append_inquiry(self, data:dict):
        """Appends a new row to the spreadsheet."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        row = [data.name, data.email, data.country, data.mobile, data.message, timestamp]
        self.sheet.append_row(row)

# Create the instance for export
gs_service = GoogleSheetsService()