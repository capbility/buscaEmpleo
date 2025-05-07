import csv
from pathlib import Path
from browser_use import ActionResult, Controller
from pydantic import BaseModel
from typing import Optional

import datetime

controller = Controller()
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
JOBS_CSV = Path.cwd() / f'jobs_{timestamp}.csv'


class Job(BaseModel):
    title: str
    link: str
    company: str
    fit_score: float
    location: Optional[str] = None
    salary: Optional[str] = None

@controller.action('Save jobs to file', param_model=Job)
def save_jobs(job: Job):
    with JOBS_CSV.open('a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([job.title, job.company, job.link, job.salary, job.location])
    return 'Saved job to file'


