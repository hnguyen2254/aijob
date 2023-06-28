import React, { useEffect, useState } from 'react';
import fetchFeaturedJobs from '../services/fetchFeaturedJobs';
import fetchCategories from '../services/fetchCategories';

const HomePage = () => {
  const [featuredJobs, setFeaturedJobs] = useState([]);
  const [categories, setCategories] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const jobs = await fetchFeaturedJobs();
      const cats = await fetchCategories();
      setFeaturedJobs(jobs);
      setCategories(cats);
    };
    fetchData();
  }, []);

  return (
    <div>
      {/* Render featured jobs and categories */}
    </div>
  );
};

export default HomePage;
