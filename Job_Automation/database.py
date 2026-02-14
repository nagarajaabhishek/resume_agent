import json
import os
from datetime import datetime

class LocalDatabase:
    """
    A simple JSON-based database for the MVP.
    Easily swappable with GoogleSheetsClient later.
    """
    def __init__(self, db_path="jobs_database.json"):
        self.db_path = db_path
        self._ensure_db_exists()

    def _ensure_db_exists(self):
        if not os.path.exists(self.db_path):
            with open(self.db_path, 'w') as f:
                json.dump([], f)

    def load_jobs(self):
        with open(self.db_path, 'r') as f:
            return json.load(f)

    def save_jobs(self, jobs):
        with open(self.db_path, 'w') as f:
            json.dump(jobs, f, indent=4)

    def add_jobs(self, new_jobs_list):
        current_jobs = self.load_jobs()
        existing_urls = {job['url'] for job in current_jobs}
        
        added_count = 0
        for job in new_jobs_list:
            if job['url'] not in existing_urls:
                # Add metadata fields
                job['status'] = 'NEW'
                job['date_added'] = datetime.now().isoformat()
                job['ats_score'] = 0
                job['pdf_path'] = ""
                
                current_jobs.append(job)
                added_count += 1
        
        self.save_jobs(current_jobs)
        print(f"Added {added_count} new jobs to local DB.")

    def get_jobs_by_status(self, status):
        jobs = self.load_jobs()
        return [j for j in jobs if j.get('status') == status]

    def update_job_status(self, job_url, status, **kwargs):
        jobs = self.load_jobs()
        for job in jobs:
            if job['url'] == job_url:
                job['status'] = status
                for k, v in kwargs.items():
                    job[k] = v
                break
        self.save_jobs(jobs)
