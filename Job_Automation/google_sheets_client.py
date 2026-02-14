import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import pandas as pd

class GoogleSheetsClient:
    def __init__(self, credentials_path="credentials.json", sheet_name="Resume_Agent_Jobs"):
        self.credentials_path = credentials_path
        self.sheet_name = sheet_name
        self.client = None
        self.sheet = None

    def connect(self):
        """Authenticates with Google Sheets API."""
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        
        try:
            creds = ServiceAccountCredentials.from_json_keyfile_name(self.credentials_path, scope)
            self.client = gspread.authorize(creds)
            
            try:
                self.sheet = self.client.open(self.sheet_name).sheet1
                print(f"Connected to sheet: {self.sheet_name}")
            except gspread.exceptions.SpreadsheetNotFound:
                print(f"Sheet '{self.sheet_name}' not found. Creating it...")
                self.sheet = self.client.create(self.sheet_name).sheet1
                # Initialize headers matching the approved spec
                headers = [
                    "Status",        # A
                    "Role Title",    # B
                    "Company",       # C
                    "Location",      # D
                    "Job Link",      # E
                    "Source",        # F
                    "Fits Policy?",  # G
                    "Reason",        # H
                    "Resume PDF Path", # I
                    "ATS Score",     # J
                    "Date Added"     # K
                ]
                self.sheet.append_row(headers)
                
        except FileNotFoundError:
            raise FileNotFoundError(f"Credentials file not found at {self.credentials_path}. Please place your Google Service Account JSON key here.")

    def get_all_jobs(self):
        """Fetches all jobs from the sheet."""
        if not self.sheet:
            self.connect()
        return self.sheet.get_all_records()

    def get_existing_urls(self):
        """Returns a set of all Job Links currently in the sheet to prevent duplicates."""
        if not self.sheet:
            self.connect()
        # Assuming 'Job Link' is column E (index 5, but records are by header name)
        records = self.sheet.get_all_records()
        return set(r['Job Link'] for r in records if 'Job Link' in r)

    def add_jobs(self, jobs_list):
        """
        Adds a list of new jobs to the sheet.
        jobs_list: List of dicts matching the schema.
        """
        if not self.sheet:
            self.connect()
            
        existing_links = self.get_existing_urls()
        new_rows = []
        
        for job in jobs_list:
            if job['url'] not in existing_links:
                row = [
                    "NEW",                  # A: Status
                    job.get('title', ''),   # B: Role Title
                    job.get('company', ''), # C: Company
                    job.get('location', ''),# D: Location
                    job.get('url', ''),     # E: Job Link
                    job.get('source', 'Unknown'), # F: Source
                    "",                     # G: Fits Policy?
                    "",                     # H: Reason
                    "",                     # I: Resume PDF Path
                    "",                     # J: ATS Score
                    datetime.now().strftime("%Y-%m-%d %H:%M:%S") # K: Date Added
                ]
                new_rows.append(row)
        
        if new_rows:
            self.sheet.append_rows(new_rows)
            print(f"Added {len(new_rows)} new jobs.")
        else:
            print("No new jobs to add.")

if __name__ == "__main__":
    # Test script
    client = GoogleSheetsClient()
    try:
        client.connect()
        print("Connection successful.")
    except Exception as e:
        print(f"Connection failed: {e}")
