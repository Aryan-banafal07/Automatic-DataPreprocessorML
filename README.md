# DataPreprocessorML

**DataPreprocessorML** is a web application designed to streamline the process of data preprocessing for machine learning. Users can upload their datasets, which are then processed to handle common issues such as missing values and standardization. The processed data is available for download as a CSV file.

## Features

- **File Upload**: Upload CSV files directly through the web interface.
- **Data Preprocessing**: Automatically handles missing values and standardizes numerical columns.
- **Download Processed Data**: Receive the processed data as a downloadable CSV file.

## Technologies Used

- **Flask**: Web framework for building the application.
- **Pandas**: Data manipulation and preprocessing.
- **Scikit-learn**: Standardization of numerical data.
- **Python**: Programming language used.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Aryan-banafal07/DataPreprocessorML.git
   cd DataPreprocessorML
Set Up a Virtual Environment

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install Dependencies

bash
Copy code
pip install -r requirements.txt
Run the Application

bash
Copy code
python app.py
Access the Application

Open your web browser and navigate to http://127.0.0.1:5000.

Usage
Go to the home page of the application.
Upload a CSV file using the provided upload form.
The application will preprocess the data and provide a link to download the processed CSV file.
Troubleshooting
Error Handling: If you encounter errors during file processing, check the server logs for detailed error messages.
File Format Issues: Ensure that the uploaded file is a valid CSV with correct encoding.
Contributing
Feel free to open issues or submit pull requests if you have suggestions or improvements.


Contact
For questions or feedback, please contact aryanbanafal7.com.
