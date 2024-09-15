import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [file, setFile] = useState(null);

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await axios.post('http://127.0.0.1:5000/upload', formData, {
        responseType: 'blob',  // Important: to handle binary data (file download)
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

      // Create a Blob URL for the downloaded file
      const blob = new Blob([response.data], { type: 'text/csv' });
      const url = window.URL.createObjectURL(blob);

      // Create a link element and trigger the download
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute('download', 'processed_data.csv');  // File name
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);  // Clean up

    } catch (error) {
      console.error("There was an error processing the file!", error);
    }
  };

  return (
    <div className="App">
      <h1>Data Preprocessing Platform</h1>
      <form onSubmit={handleSubmit}>
        <input type="file" onChange={handleFileChange} />
        <button type="submit">Upload and Process</button>
      </form>
    </div>
  );
}

export default App;
