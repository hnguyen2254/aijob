import pytest
from app import JobCategories, fetchJobsByCategory

def test_job_categories_render():
    job_categories = JobCategories()
    assert job_categories.render() is not None

@pytest.mark.parametrize("category", ["Machine Learning", "Data Science", "AI Engineering"])
def test_fetch_jobs_by_category(category):
    jobs = fetchJobsByCategory(category)
    assert len(jobs) > 0
