from flask import Flask, Response, jsonify
from flask_cors import CORS
import csv

app = Flask(__name__)
CORS(app) #enable CORS

@app.route('/get_json')
def get_json():
  # Path to TSV file
  tsv_file = 'demo.tsv'

  try:
    # Read data from the TSV file with the specified encoding
    with open(tsv_file, 'r', newline='', encoding='utf-8') as file:
      tsv_data = list(csv.DictReader(file, delimiter='\t'))

    # Return TSV data as JSON
    return jsonify(tsv_data)
  except UnicodeDecodeError:
    return jsonify({"error": "Unable to decode file due to encoding issues."})

if __name__ == '__main__':
  app.run(debug=True)