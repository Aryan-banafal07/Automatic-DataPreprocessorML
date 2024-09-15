from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import pandas as pd
from sklearn.preprocessing import StandardScaler
import io
import traceback

app = Flask(__name__)
CORS(app)

def read_csv_with_fallback(file):
    encodings = ['utf-8', 'ISO-8859-1', 'latin1']
    for encoding in encodings:
        try:
            # Reset file pointer to the beginning
            file.seek(0)
            return pd.read_csv(file, encoding=encoding)
        except pd.errors.EmptyDataError:
            continue
        except UnicodeDecodeError:
            continue
        except pd.errors.ParserError:
            continue
    raise ValueError("Unable to read the file with the provided encodings or format issues")

@app.route('/')
def index():
    return "Welcome to the Data Preprocessing Platform"

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    try:
        # Read the dataset into a pandas DataFrame with fallback encodings
        df = read_csv_with_fallback(file)
        
        if df.empty:
            return jsonify({"error": "Uploaded file is empty or does not contain valid data"}), 400

        # Example preprocessing: Remove missing values
        cleaned_df = df.dropna()

        # Example: Standardization of numerical columns
        numerical_cols = cleaned_df.select_dtypes(include=['float64', 'int64']).columns
        if numerical_cols.empty:
            return jsonify({"error": "No numerical columns found for standardization"}), 400
        
        scaler = StandardScaler()
        scaled_data = scaler.fit_transform(cleaned_df[numerical_cols])
        scaled_df = pd.DataFrame(scaled_data, columns=numerical_cols)
        
        # Save the processed data to a CSV in memory
        csv_buffer = io.StringIO()
        scaled_df.to_csv(csv_buffer, index=False)
        csv_buffer.seek(0)

        # Return the CSV as a file download
        return send_file(
            io.BytesIO(csv_buffer.getvalue().encode('utf-8')),
            mimetype='text/csv',
            as_attachment=True,
            download_name='processed_data.csv'
        )
    
    except Exception as e:
        print("Error occurred while processing the file:")
        traceback.print_exc()  # Print the full error traceback to see what went wrong
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
