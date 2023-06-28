import pytest
from app import HomePage, fetchFeaturedJobs, fetchCategories

def test_homepage_render():
    homepage = HomePage()
    assert homepage.render() is not None

def test_fetch_featured_jobs():
    featured_jobs = fetchFeaturedJobs()
    assert len(featured_jobs) > 0

def test_fetch_categories():
    categories = fetchCategories()
    assert len(categories) > 0
