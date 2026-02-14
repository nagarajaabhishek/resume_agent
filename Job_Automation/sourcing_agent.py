from jobspy import scrape_jobs
from google_sheets_client import GoogleSheetsClient
import pandas as pd

import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

class SourcingAgent:
    def __init__(self, sheets_client):
        self.sheets_client = sheets_client

    def scrape(self, queries=["Software Engineer", "Machine Learning Engineer"], locations=["United States", "Remote"], results_wanted=10):
        """
        Scrapes jobs from LinkedIn, Indeed, Glassdoor using JobSpy.
        """
        all_jobs = []
        
        for query in queries:
            for location in locations:
                print(f"Scraping for '{query}' in '{location}'...")
                try:
                    jobs = scrape_jobs(
                        site_name=["linkedin", "indeed", "glassdoor"],
                        search_term=query,
                        location=location,
                        results_wanted=results_wanted,
                        hours_old=24, # Daily run
                        country_indeed='USA'
                    )
                    
                    if not jobs.empty:
                        # Convert DataFrame to list of dicts
                        jobs_dict = jobs.to_dict('records')
                        all_jobs.extend(jobs_dict)
                        print(f"Found {len(jobs_dict)} jobs for {query}.")
                    else:
                        print(f"No jobs found for {query}.")
                        
                except Exception as e:
                    print(f"Error scraping for {query}: {e}")
                    
        return all_jobs

    def normalize_and_save(self, raw_jobs):
        """
        Normalizes job data and saves to Google Sheets.
        """
        clean_jobs = []
        for job in raw_jobs:
            # JobSpy returns: title, company, job_url, location, description, site
            clean_job = {
                'title': job.get('title'),
                'company': job.get('company'),
                'url': job.get('job_url'),
                'location': job.get('location'),
                'source': job.get('site'),
                'description': job.get('description'), # Important for future steps, though strict schema didn't save it. 
                # Note: Schema doesn't have a 'Description' column. 
                # We typically rely on re-scraping JD text later or should likely add it.
                # For now, following strict schema (Columns A-K).
            }
            clean_jobs.append(clean_job)
            
        self.sheets_client.add_jobs(clean_jobs)

if __name__ == "__main__":
    # Test script
    client = GoogleSheetsClient()
    agent = SourcingAgent(client)
    
    # Run a small test scrape
    raw_jobs = agent.scrape(queries=["AI Engineer"], locations=["Remote"], results_wanted=5)
    agent.normalize_and_save(raw_jobs)
