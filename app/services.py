import os
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv

load_dotenv()

class GoogleSheetsService:
    def __init__(self):
        self.scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        self.sheet_name = os.getenv("SHEET_NAME", "M3GAN AI")
        self.client = self._authenticate()
        self.sheet = self.client.open(self.sheet_name).sheet1

    def _authenticate(self):
        # Read from Env Var (Vercel) or Fallback to File (Local)
        creds_json = os.getenv("GOOGLE_CREDS_JSON")
        
        if creds_json:
            # Parse the string into a dictionary
            creds_info = json.loads(creds_json)
            creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_info, self.scope)
        else:
            # Fallback for local development
            creds = ServiceAccountCredentials.from_json_keyfile_name("m3gan_credentials.json", self.scope)
            
        return gspread.authorize(creds)