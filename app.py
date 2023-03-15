import json
from flask import Flask, request, jsonify
import sqlite3
from opendp.smartnoise.sql import PrivateReader
from query_validator import validate_query

app = Flask(__name__)

#loading the config file
config = json.load(open('config.json'))

# Define the list of allowed query regexes
allowed_queries_regex_list = config['allowed_queries']

# Define the privacy parameters for the SmartNoise reader
epsilon = config['epsilon']
delta = config['delta']

# Create a connection to the SQLite database
conn = sqlite3.connect('data/db/employees.db')

# Create a private reader object using the SmartNoise library
reader = PrivateReader.from_connection(conn, epsilon=epsilon, delta=delta)

@app.route('/', methods=['POST'])
def query_db():
    # Get the query from the request
    data = request.json
    query = data['query']
    
    # Check if the query matches the allowed pattern
    if not validate_query(allowed_queries_regex_list, query):
        return jsonify({'error': 'Invalid query type'})
    
    # Run the query using the SmartNoise reader
    result = reader.execute(query)
    
    # Return the query result as JSON
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
