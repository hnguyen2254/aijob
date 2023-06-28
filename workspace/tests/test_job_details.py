import pytest
from app import JobDetails, fetchJobDetails

def test_job_details_render():
    job_details = JobDetails()
    assert job_details.render() is not None

def test_fetch_job_details():
    job_id = 1
    job_details = fetchJobDetails(job_id)
    assert job_details is not None
