import snsql
from flask import Flask, request
from app.api_key_validator import ApiKeyValidator
from app.query_validator import validate_query
from app.db_connector import DBConnector
from app.private_query_runner import PrivateQueryRunner
from app.configuration import Configuration

# Load the config file
CONFIG = Configuration()

# Get database connection and metadata
DB_CONN = DBConnector.get_database_connection()
DB_METADATA = DBConnector.get_database_metadata()

# Create a private reader object using the SmartNoise library
READER = snsql.from_connection(DB_CONN, privacy=CONFIG.privacy, metadata=DB_METADATA)

app = Flask(__name__)

@app.route('/', methods=['POST'])
def query_db():
    # Validate the API key
    api_key = request.headers.get('X-API-Key')
    validator = ApiKeyValidator(api_key)
    if not validator.validate():
        return {'error': 'Invalid API key'}, 401

    #Gets the query from the request and checks if it is valid.
    data = request.json

    if 'query' not in data:
        return {'error': 'Missing: query'}, 400

    query = data['query']
    
    if not validate_query(query.upper(), CONFIG.allowed_sql_functions):
        return {'error': 'Unsupported query type'}, 400
    
    return PrivateQueryRunner.run_query(query, READER)

if __name__ == '__main__':
    app.run(port="5050",debug=True)
