import pytest
from app import JobListings, fetchJobListings, renderPagination

def test_job_listings_render():
    job_listings = JobListings()
    assert job_listings.render() is not None

def test_fetch_job_listings():
    category = "Machine Learning"
    page = 1
    job_listings = fetchJobListings(category, page)
    assert len(job_listings) > 0

def test_render_pagination():
    pagination = renderPagination()
    assert pagination is not None
