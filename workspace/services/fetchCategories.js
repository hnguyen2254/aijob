const fetchCategories = async () => {
  // Fetch job categories from the server
  // Replace the URL with your API endpoint
  const response = await fetch('https://api.example.com/categories');
  const data = await response.json();
  return data;
};

export default fetchCategories;
