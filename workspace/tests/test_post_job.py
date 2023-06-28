import pytest
from app import PostJob, handleSubmit, validateForm

def test_post_job_render():
    post_job = PostJob()
    assert post_job.render() is not None

def test_handle_submit():
    form_data = {
        "title": "Test Job",
        "company": "Test Company",
        "description": "Test job description",
        "skills": "Python, Machine Learning",
        "location": "Worldwide",
        "contact": "test@example.com"
    }
    result = handleSubmit(form_data)
    assert result is True

def test_validate_form():
    form_data = {
        "title": "",
        "company": "",
        "description": "",
        "skills": "",
        "location": "",
        "contact": ""
    }
    errors = validateForm(form_data)
    assert len(errors) > 0
