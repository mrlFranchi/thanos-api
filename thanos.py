from flask import Flask, Response
import csv

app = Flask(__name__)

@app.route('/get_tsv')
def get_tsv():
  # Path to TSV file
  tsv_file = 'demo.tsv' #Demo File, change to your file

  try:
    # Read data from the TSV file with the specified encoding
    with open(tsv_file, 'r', newline='', encoding='utf-8') as file:
      tsv_data = file.read()
    
    # Return TSV as plain text as a response
    return Response(
      tsv_data,
      mimetype='text/plain'
    )
  except UnicodeDecodeError:
    return "Error: Unable to decode file due to encoding issues."

if __name__ == '__main__':
  app.run(debug=True)